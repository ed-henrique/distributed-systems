# Atividade: Criando uma aplicação de controle remoto com gRPC

## Objetivo

Criar cliente e servidor gRPC para criar uma aplicação de controle remoto de uma máquina Linux. O objetivo é permitir que o cliente envie comandos em formato de string para o servidor, que irá executar esses comandos em uma máquina Linux e retornar o resultado para o cliente.

## Descrição

A aplicação deverá ser composta por um servidor e um cliente, implementados usando gRPC e Python. O servidor deve estar configurado para receber comandos em formato de string do cliente e executá-los em uma máquina Linux. O cliente deve permitir que o usuário insira os comandos que deseja executar e exibir o resultado da execução.

## Requisitos

### Essencias (solicitados pelo professor)

- [x] O servidor deve ser capaz de receber comandos em formato de string do cliente e executá-los em uma máquina Linux;
- [x] O cliente deve permitir que o usuário insira os comandos que deseja executar no servidor e exibir o resultado da execução;
- [ ] O código deve ser modularizado e organizado em pacotes e módulos;
- [x] Deve ser possível executar o servidor e o cliente em máquinas diferentes;
- [x] O servidor e o cliente devem ser implementados usando gRPC e Python.

### Opcionais (eu quero implementar)

- [ ] Criar containers diferentes para cliente e servidor;

> Nunca fiz isso. Se tomar muito tempo, vou acabar deixando para outra hora.

- [ ] Permitir que o usuário passe um arquivo `.sh` para o servidor para execução;

> Esse com certeza é muito mais fácil do que parece. O motivo principal para fazer isso é dar sentido ao uso do click, já que posso criar uma flag para passar o `PATH` do script.

## Dicas

- [x] Utilize a biblioteca subprocess para executar comandos bash no servidor;
- [x] Utilize a biblioteca grpc para implementar a comunicação entre o cliente e o servidor;
- [ ] Utilize a biblioteca click para implementar a interface de linha de comando do cliente;
- [ ] Organize o código em pacotes e módulos para facilitar a manutenção e reutilização.

> Essa tem sido a parte mais difícil, por se tratar de um código tão pequeno. Mas acredito que conforme for adicionando novas coisas, isso será necessário para manter o [SRP](https://en.wikipedia.org/wiki/Single-responsibility_principle).

## Bônus

Implemente alguma funcionalidade adicional na aplicação, como por exemplo:

- [ ] Autenticação e autorização de usuários;

> Parece bem fácil, baseado na [documentação](https://grpc.io/docs/guides/auth/#python), vou começar por aqui.

- [ ] Execução de comandos em múltiplas máquinas ao mesmo tempo;

> Somente vai ser possível implementar e testar isso depois de criar um container para o servidor, pelo menos.

- [ ] Implementação de um sistema de logs para armazenar as informações de execução;

> Pensei em usar o RabbitMQ que foi estudado anteriormente, mas sinceramente, não sei se vale a complexidade que vai adicionar ao sistema. Vou optar por salvar os logs em arquivo de texto na máquina do servidor.

- [ ] Utilização de criptografia para garantir a segurança na comunicação entre o cliente e o servidor.

> Pelo que entendi, ao incluir a autenticação no gRPC, os dados serão encriptogrados, então vou focar na autenticação.