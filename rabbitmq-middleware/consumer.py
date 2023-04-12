import pika

def report_fire(channel):
    print('\033[0;31m' + 'Fogo detectado!' + '\033[0m')

    channel.queue_declare(queue='fire_queue')
    channel.basic_publish(exchange='', routing_key='fire_queue', body='')

    channel.queue_declare(queue='my_queue')

def connect_to_rabbitmq():
    try:
        connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        channel = connection.channel()
        channel.queue_declare(queue='my_queue')
        
        return channel
    except:
        print('Erro ao conectar ao RabbitMQ')

def callback(ch, method, properties, body):
    temperature_str = body.decode('ascii')
    temperature = float(temperature_str)

    print("Temperatura atual do cliente: ", end="")
    
    if temperature > 70.0:
        print('\033[0;31m' + temperature_str + '\033[0m') # Red
        report_fire(ch)
    else:
        print('\033[0;32m' + temperature_str + '\033[0m') # Green

if __name__ == "__main__":
    try:
        channel = connect_to_rabbitmq()
        
        channel.basic_consume(queue='my_queue', on_message_callback=callback, auto_ack=True)
        
        print('Aguardando tarefas...')
        channel.start_consuming()
    except:
        print('Erro ao executar o programa')