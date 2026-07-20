import json
import time

import pika


def callback(ch, method, properties, body):
    chamado = json.loads(body)
    print(f" [x] Atendente recebeu chamado #{chamado['id']} de {chamado['cliente']}: {chamado['descricao']}")

    time.sleep(15)

    resposta = {
        "id": chamado["id"],
        "status": "Fechado",
        "mensagem": f"Chamado {chamado['id']} resolvido e fechado pelo atendente (MOM).",
    }

    if properties.reply_to:
        ch.basic_publish(
            exchange="",
            routing_key=properties.reply_to,
            properties=pika.BasicProperties(correlation_id=properties.correlation_id),
            body=json.dumps(resposta),
        )

    print(f" [x] Chamado #{chamado['id']} processado e finalizado.")
    ch.basic_ack(delivery_tag=method.delivery_tag)


connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='fila_suporte')

channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='fila_suporte', on_message_callback=callback)

print(' [*] Atendente aguardando chamados. Para sair, pressione CTRL+C')
channel.start_consuming()
