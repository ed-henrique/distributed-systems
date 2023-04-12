#!/usr/bin/env python3

# Recebe mensagens relativas à ativação do sistema de incêndio no RabbitMQ pelo fire_consumer.py

import fn

def callback(ch, method, properties, body):
    print("O sistema de incêndio foi ativado!")

if __name__ == "__main__":
    try:
        fn.consume_from_rabbitmq_queue(queue_name='alert_queue', callback=callback)
    except:
        print('Erro ao executar o programa')