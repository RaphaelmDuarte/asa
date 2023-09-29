import pika
import json
import time

credentials = pika.PlainCredentials('guest', 'guest')
parameters = pika.ConnectionParameters('localhost',
                                   5672,
                                   '/',
                                   credentials)

connection = pika.BlockingConnection(parameters)

channel = connection.channel()

channel.queue_declare(queue='pdfprocess')

i = 1
while(True):
    data = {"id": i, "nome": "Pedro Silva", "endereco": "Rua X, 333"}
    print(json.dumps(data).encode())
    print(json.dumps(data))
    channel.basic_publish(exchange='', routing_key='pdfprocess',
                      body=json.dumps(data).encode())
    print("[x] Message sent to consumer")
    time.sleep(5)  # delays for 5 seconds
    i = i + 1

connection.close()