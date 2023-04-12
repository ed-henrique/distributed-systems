import os
import pika

def connect_to_rabbitmq():
    try:
        connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        channel = connection.channel()
        channel.queue_declare(queue='fire_queue')
        
        return channel
    except:
        print('Erro ao conectar ao RabbitMQ')

def callback(ch, method, properties, body):
    print('\033[0;31m' + 'Fire in progress!' + '\033[0m')
    os.system('speaker-test -t sine -f 1000 -l 1')

if __name__ == "__main__":
    try:
        channel = connect_to_rabbitmq()
        
        channel.basic_consume(queue='fire_queue', on_message_callback=callback, auto_ack=True)
        
        print('Aguardando fogo...')
        channel.start_consuming()
    except:
        print('Erro ao executar o programa')