import pika
import json

connection_parameters = pika.ConnectionParameters('localhost')

connection = pika.BlockingConnection(connection_parameters)

channel = connection.channel()

channel.queue_declare(queue='letterbox')

message = {"id":11, "packet_no":126, "temperature":30, "humidity":60, "tds":1100, "pH":5.0}

channel.basic_publish(exchange='', routing_key='databox', body=json.dumps(message))

print(f"sent message: {json.dumps(message)}")

connection.close()