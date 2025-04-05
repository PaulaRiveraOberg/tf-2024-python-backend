import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))
channel = connection.channel()

channel.exchange_declare(exchange="business_events", exchange_type="fanout")

message = "BUYER_ARRIVED_ID"
channel.basic_publish(exchange="business_events", routing_key="", body=message)
print(message, "happened.")
connection.close()
