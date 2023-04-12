# Middleware com RabbitMQ para ativar sistema de incêndio

Middleware cliente-servidor, que utiliza o protocolo AMQP para troca de mensagens.

Existem 4 programas em execução nesse sistema:

- `producer.py`: programa que relata a temperatura da CPU para o consumer
- `consumer.py`: programa que recebe a temperatura da CPU e ativa o sistema de incêndio caso ela exceda 70ºC
- `fire_consumer.py`: programa que ativa o sistema de incêndio caso receba uma mensagem do consumer
- `main_consumer.py`: programa que recebe as mensagens do fire_consumer e as imprime no terminal

Logo, o sistema apresenta uma hierarquia muito clara:

```mermaid
graph LR;
    producer --> consumer;
    consumer --> fire_consumer;
    fire_consumer --> main_consumer;
```

**OBS: funcionando apenas no Linux**

## Imports Necesários

- os
- pika
- time
- psutil

## Possíveis melhorias

- Acrescentar um logger
- Resolver o problema de não conseguir fechar o programa com Ctrl+C