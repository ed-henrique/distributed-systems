#!/usr/bin/env python3

# Ativa o alarme sonoro quando recebe uma mensagem no RabbitMQ vinda do consumer.py e avisa o main_consumer.py

import os
import fn

def callback(ch, method, properties, body):
    cmd = 'speaker-test -t sine -f 1000 -l 1 > /dev/null 2>&1 &'

    fn.print_with_time('\033[0;31m' + 'Fogo em Progresso!' + '\033[0m')
    os.system(cmd)

    fn.report_fire_to_main(ch)

if __name__ == "__main__":
    try:
        fn.consume_from_rabbitmq_queue(queue_name='fire_queue', callback=callback)
    except:
        fn.print_with_time('Erro ao executar o programa')