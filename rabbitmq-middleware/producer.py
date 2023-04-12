#!/usr/bin/env python3

# Manda a cada 5 segundos a temperatura da CPU no RabbitMQ para o consumer.py

import fn
from time import sleep

if __name__ == "__main__":
    try:
        channel = fn.connect_to_rabbitmq(queue_name='my_queue')

        while True:
            channel.basic_publish(exchange='', routing_key='my_queue', body=fn.get_cpu_temperature_as_str())
            sleep(5)
    except:
        fn.print_with_time('Erro ao executar o programa')