import pika
import json

def on_message_received(ch, method, properties, body):
    print(f"received new message: {json.loads(body)}" )

connection_parameters = pika.ConnectionParameters('localhost')

connection = pika.BlockingConnection(connection_parameters)

channel = connection.channel()

channel.queue_declare(queue='databox')

channel.basic_consume(queue='databox', auto_ack=True,
    on_message_callback=on_message_received)

print("Starting Consuming")

channel.start_consuming()