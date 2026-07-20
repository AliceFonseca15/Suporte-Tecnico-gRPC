# Suporte Técnico — Integração gRPC + MOM (RabbitMQ)

Repositório da atividade/estudo de gRPC e MOM para a disciplina de Desenvolvimento Distribuído.

Este projeto integra os dois sistemas de suporte técnico:

- **gRPC** (cliente/servidor síncrono) para cadastro, consulta, listagem e
  atualização de chamados.
- **MOM** (RabbitMQ) para o "atendimento"/resolução assíncrona dos chamados,
  feita por um ou mais consumers (atendentes).



## Como rodar

1. Instalar as dependências:

       pip install -r requirements.txt

2. Subir o RabbitMQ (broker):

       docker run -d --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3-management

   Para retomar um container já criado:

       docker start rabbitmq

   Painel de controle: http://localhost:15672 (usuário/senha: `guest`/`guest`)

3. (Re)gerar os arquivos de contrato, se alterar o `.proto`:

       python -m grpc_tools.protoc -Iproto --python_out=. --grpc_python_out=. proto/suporte.proto

4. Iniciar um ou mais atendentes (consumers) do MOM — cada um em um terminal:

       python mom/consumer.py

5. Iniciar o servidor gRPC (em outro terminal):

       python server/server.py

6. Iniciar o cliente gRPC (em outro terminal):

       python cliente/cliente.py


