import os
import sys

import pika


def receive():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))
    channel = connection.channel()
    channel.queue_declare(queue="hello")

    def callback(ch, method, properties, body):
        print(body.decode())

    channel.basic_consume(queue="hello", on_message_callback=callback, auto_ack=True)
    print("Waiting for your hello!")
    channel.start_consuming()


if __name__ == "__main__":
    try:
        receive()
    except KeyboardInterrupt:
        print("Interrupted")
    try:
        sys.exit(0)
    except SystemExit:
        os._exit(0)
