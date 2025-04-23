import signal
import sys
import time

import pika


class StagedProducer:
    def __init__(self):
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters("localhost")
        )
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue="hello")
        self.running = True

        # Configurar el manejo de señales
        signal.signal(signal.SIGINT, self.stop)
        signal.signal(signal.SIGTERM, self.stop)

    def stop(self, signum, frame):
        print("\nDeteniendo el envío de mensajes...")
        self.running = False

    def send_staged_messages(self, stages=3, messages_per_stage=3):
        try:
            for stage in range(stages):
                if not self.running:
                    break

                print(f"\nIniciando etapa {stage + 1}")
                for i in range(messages_per_stage):
                    if not self.running:
                        break

                    message = f"Etapa {stage + 1} - Mensaje {i + 1}"
                    self.channel.basic_publish(
                        exchange="", routing_key="hello", body=message
                    )
                    print(f"Enviado: {message}")
                    time.sleep(1)  # Pequeña pausa entre mensajes

                if self.running:
                    print(f"Etapa {stage + 1} completada")
                    time.sleep(2)  # Pausa más larga entre etapas

        finally:
            self.connection.close()


if __name__ == "__main__":
    producer = StagedProducer()
    producer.send_staged_messages()
