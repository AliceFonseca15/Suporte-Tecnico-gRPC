import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import grpc
import suporte_pb2
import suporte_pb2_grpc

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = suporte_pb2_grpc.ServicoSuporteStub(channel)

        while True:
            print("\n--- MENU SUPORTE TÉCNICO ---")
            print("1. Cadastrar Chamado")
            print("2. Consultar Chamado")
            print("3. Listar Chamados")
            print("4. Atualizar Chamado")
            print("5. Enviar Chamado para o MOM (Resolver)")
            print("6. Sair")
            opcao = input("Escolha uma opção: ")

            if opcao == '1':
                try:
                    cliente = input("Nome do Cliente: ")
                    desc = input("Descrição do problema: ")
                    prior = input("Prioridade (Baixa/Média/Alta): ")

                    response = stub.AbrirChamado(suporte_pb2.Chamado(
                        id=0, cliente=cliente, descricao=desc, prioridade=prior
                    ))
                    print(f"\nResposta do Servidor: {response.mensagem}")
                except ValueError:
                    print("Erro: Dados inválidos.")

            elif opcao == '2':
                try:
                    cid = int(input("Digite o ID do chamado para consultar: "))
                    chamado = stub.ConsultarChamado(suporte_pb2.IdRequest(id=cid))
                    print(f"\n--- Detalhes do Chamado ---")
                    print(f"ID: {chamado.id}")
                    print(f"Cliente: {chamado.cliente}")
                    print(f"Descrição: {chamado.descricao}")
                    print(f"Prioridade: {chamado.prioridade}")
                    print(f"Status: {chamado.status}")
                except grpc.RpcError as e:
                    print(f"Erro ao consultar: {e.details()}")

            elif opcao == '3':
                print("\n--- Lista de Chamados ---")
                response = stub.ListarChamados(suporte_pb2.Empty())
                for c in response.chamados:
                    print(f"ID: {c.id} | Cliente: {c.cliente} | Status: {c.status}")

            elif opcao == '4':
                try:
                    cid = int(input("Digite o ID do chamado para atualizar: "))
                    
                    chamado_atual = stub.ConsultarChamado(suporte_pb2.IdRequest(id=cid))

                    cliente = input("Nome do Cliente: ")
                    desc = input("Descrição do problema: ")
                    prior = input("Prioridade (Baixa/Média/Alta): ")

                    response = stub.AtualizarChamado(suporte_pb2.Chamado(
                        id=cid, cliente=cliente, descricao=desc, prioridade=prior,
                        status=chamado_atual.status
                    ))
                    print(f"\nResposta do Servidor: {response.mensagem}")
                except ValueError:
                    print("Erro: O ID deve ser um número inteiro.")
                except grpc.RpcError as e:
                    print(f"Erro ao atualizar: {e.details()}")

            elif opcao == '5':
                try:
                    cid = int(input("Digite o ID do chamado para enviar ao MOM: "))
                    print("\nEnviando chamado para a fila do MOM e aguardando "
                          "um atendente processá-lo... (isso pode levar alguns segundos)")

                    response = stub.ResolverChamado(suporte_pb2.IdRequest(id=cid))
                    print(f"\nResposta do Atendente (via MOM): {response.mensagem}")
                except ValueError:
                    print("Erro: O ID deve ser um número inteiro.")
                except grpc.RpcError as e:
                    print(f"Erro ao resolver via MOM: {e.details()}")

            elif opcao == '6':
                break
            else:
                print("Opção inválida!")

if __name__ == '__main__':
    run()
