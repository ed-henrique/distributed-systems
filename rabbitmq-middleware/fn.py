#!/usr/bin/env python3

import pika
import psutil

def connect_to_rabbitmq(queue_name):
    try:
        connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        channel = connection.channel()
        channel.queue_declare(queue=queue_name)
        return channel
    except:
        print('Erro ao conectar ao RabbitMQ')

def consume_from_rabbitmq_queue(queue_name, callback):
    try:
        channel = connect_to_rabbitmq(queue_name)
        channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)
        channel.start_consuming()
    except:
        print('Erro ao consumir da fila do RabbitMQ')

def get_cpu_temperature_as_str():
    try:
        devices_temperatures = psutil.sensors_temperatures()
        cpu_cores_temperatures = devices_temperatures['coretemp']
        current_cpu_temperature = cpu_cores_temperatures[0].current
        return str(current_cpu_temperature)
    except:
        print('Erro ao obter temperatura da CPU')

def report_fire(channel):
    try:
        print('\033[0;31m' + 'Fogo detectado!' + '\033[0m')

        channel.queue_declare(queue='fire_queue')
        channel.basic_publish(exchange='', routing_key='fire_queue', body='')

        channel.queue_declare(queue='my_queue')
    except:
        print('Erro ao reportar fogo')

def report_fire_to_main(channel):
    try:
        channel.queue_declare(queue='alert_queue')
        channel.basic_publish(exchange='', routing_key='alert_queue', body='')

        channel.queue_declare(queue='fire_queue')
    except:
        print('Erro ao reportar fogo')