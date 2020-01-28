#!/usr/bin/env python
import pika
import sys

def new_task():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    c=channel.queue_declare(queue='hello')
    print(c)

    message = ' '.join(sys.argv[1:]) or "Hello World!....."
    channel.basic_publish(exchange='',routing_key='hello',body=message)

    print(" [x] Sent %r" % message)
    connection.close()
