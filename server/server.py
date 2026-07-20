import sys
import os
import grpc
from concurrent import futures

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import suporte_pb2
import suporte_pb2_grpc
import data
import mom_rpc_client


class SuporteService(suporte_pb2_grpc.ServicoSuporteServicer):

    def AbrirChamado(self, request, context):
        if request.id == 0:
            request.id = data.gerar_novo_id()

        print(f"Recebendo cadastro: ID {request.id}, Cliente: {request.cliente}")

        data.salvar_chamado(request)

        return suporte_pb2.StatusResponse(
            sucesso=True,
            mensagem=f"Chamado {request.id} registrado com sucesso!"
        )

    def ConsultarChamado(self, request, context):
        print(f"Consultando ID: {request.id}")

        chamado = data.buscar_chamado(request.id)

        if chamado:
            return chamado
        else:
            context.abort(grpc.StatusCode.NOT_FOUND, f"Chamado com ID {request.id} não encontrado.")

    def ListarChamados(self, request, context):
        print("Listando todos os chamados...")
        lista = data.listar_todos()
        return suporte_pb2.ListaChamados(chamados=lista)

    def AtualizarChamado(self, request, context):
        print(f"Atualizando chamado ID {request.id}")

        sucesso = data.atualizar_chamado(request)

        if sucesso:
            return suporte_pb2.StatusResponse(
                sucesso=True,
                mensagem=f"Chamado {request.id} atualizado com sucesso!"
            )
        else:
            context.abort(grpc.StatusCode.NOT_FOUND, f"Chamado com ID {request.id} não encontrado.")

    def ResolverChamado(self, request, context):
        chamado = data.buscar_chamado(request.id)

        if not chamado:
            context.abort(grpc.StatusCode.NOT_FOUND, f"Chamado com ID {request.id} não encontrado.")
            return

        print(f"Enviando chamado {chamado.id} para o MOM")

        try:
            rpc_client = mom_rpc_client.MomRpcClient()
            resposta = rpc_client.call({
                "id": chamado.id,
                "cliente": chamado.cliente,
                "descricao": chamado.descricao,
            })
            rpc_client.close()
        except TimeoutError as e:
            context.abort(grpc.StatusCode.DEADLINE_EXCEEDED, str(e))
            return
        except Exception as e:
            context.abort(grpc.StatusCode.UNAVAILABLE, f"Erro ao comunicar com o MOM: {e}")
            return

        chamado.status = resposta.get("status", "Fechado")
        data.atualizar_chamado(chamado)

        print(f"Chamado {chamado.id} resolvido via MOM: {resposta.get('mensagem')}")

        return suporte_pb2.StatusResponse(
            sucesso=True,
            mensagem=resposta.get("mensagem", f"Chamado {chamado.id} fechado.")
        )


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    suporte_pb2_grpc.add_ServicoSuporteServicer_to_server(SuporteService(), server)

    port = '50051'
    server.add_insecure_port(f'[::]:{port}')
    print(f"Servidor gRPC iniciado na porta {port}...")
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
