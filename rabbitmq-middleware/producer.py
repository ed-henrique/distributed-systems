import pika
import psutil
from time import sleep

def connect_to_rabbitmq():
    try:
        connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        channel = connection.channel()
        channel.queue_declare(queue='my_queue')
        return channel
    except:
        print('Erro ao conectar ao RabbitMQ')

def get_cpu_temperature_as_str():
    try:
        devices_temperatures = psutil.sensors_temperatures()
        cpu_cores_temperatures = devices_temperatures['coretemp']
        current_cpu_temperature = cpu_cores_temperatures[0].current
        return str(current_cpu_temperature)
    except:
        print('Erro ao obter temperatura da CPU')

if __name__ == "__main__":
    try:
        channel = connect_to_rabbitmq()

        while True:
            channel.basic_publish(exchange='', routing_key='my_queue', body=get_cpu_temperature_as_str())
            sleep(5)
    except:
        print('Erro ao executar o programa')