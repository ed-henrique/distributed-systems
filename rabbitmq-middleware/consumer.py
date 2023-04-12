#!/usr/bin/env python3

# Recebe a temperatura da CPU, e caso esta ultrapssse 70 graus, manda uma mensagem no RabbitMQ para o fire_consumer.py

import fn

def callback(ch, method, properties, body):
    temperature_str = body.decode('ascii')
    temperature = float(temperature_str)

    fn.print_with_time("Temperatura atual do cliente: ", end="")
    
    if temperature > 50.0:
        print('\033[0;31m' + temperature_str + '\033[0m') # Red
        fn.report_fire(ch)
    else:
        print('\033[0;32m' + temperature_str + '\033[0m') # Green

if __name__ == "__main__":
    try:
        fn.consume_from_rabbitmq_queue(queue_name='my_queue', callback=callback)
    except:
        fn.print_with_time('Erro ao executar o programa')