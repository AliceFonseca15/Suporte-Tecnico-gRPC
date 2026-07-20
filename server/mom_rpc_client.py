import json
import time
import uuid

import pika


class MomRpcClient:
    def __init__(self, host="localhost", fila="fila_suporte"):
        self.fila = fila
        self.response = None
        self.corr_id = None

        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host=host))
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue=self.fila)

        result = self.channel.queue_declare(queue="", exclusive=True)
        self.callback_queue = result.method.queue

        self.channel.basic_consume(
            queue=self.callback_queue,
            on_message_callback=self._on_response,
            auto_ack=True,
        )

    def _on_response(self, ch, method, properties, body):
        if self.corr_id == properties.correlation_id:
            self.response = body

    def call(self, chamado_dict: dict, timeout: int = 90) -> dict:
        self.response = None
        self.corr_id = str(uuid.uuid4())

        self.channel.basic_publish(
            exchange="",
            routing_key=self.fila,
            properties=pika.BasicProperties(
                reply_to=self.callback_queue,
                correlation_id=self.corr_id,
            ),
            body=json.dumps(chamado_dict),
        )

        inicio = time.time()
        while self.response is None:
            self.connection.process_data_events(time_limit=1)
            if time.time() - inicio > timeout:
                raise TimeoutError(
                    "Tempo esgotado aguardando o atendente (MOM) processar o chamado."
                )

        return json.loads(self.response)

    def close(self):
        try:
            self.connection.close()
        except Exception:
            pass
