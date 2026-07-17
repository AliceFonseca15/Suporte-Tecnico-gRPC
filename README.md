# Suporte-Tecnico-gRPC

Repositório da atividade/estudo de gRPC para a disciplina de Desenvolvimento Distribuído.


Implementação de um sistema de suporte utilizando gRPC para comunicação síncrona entre cliente e servidor, permitindo o gerenciamento de chamados via contrato Protocol Buffers.

## Funcionamento:
  O cliente envia os dados do chamado diretamente para o servidor

  O servidor recebe a requisição, processa o chamado de forma síncrona e responde imediatamente se deu certo.

  A comunicação ocorre de forma direta entre cliente e servidor.

  Se o servidor for encerrado, o cliente não conseguirá enviar chamados e receberá um erro de conexão.
  
## Como rodar:

1. Instalar as dependências

        pip install -r requirements.txt

2. Gerar os arquivos de contrato

        python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. suporte.proto

3. Iniciar o Servidor no primeiro Terminal, na pasta server

       python server.py


4. Iniciar o Cliente no segundo Terminal, na pasta cliente

       python cliente.py
   

   
   
