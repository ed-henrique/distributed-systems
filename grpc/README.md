# Atividade: Criando uma aplicação de controle remoto com gRPC <!-- omit in toc -->

## Índice <!-- omit in toc -->
- [Objetivo](#objetivo)
- [Descrição](#descrição)
- [Requisitos](#requisitos)
  - [Essencias (solicitados pelo professor)](#essencias-solicitados-pelo-professor)
  - [Opcionais (eu quero implementar)](#opcionais-eu-quero-implementar)
- [Dicas](#dicas)
- [Bônus](#bônus)
- [Como rodar o código](#como-rodar-o-código)
  - [Dependências](#dependências)
  - [Comandos](#comandos)
    - [Explicação do que está acontecendo por baixo dos panos](#explicação-do-que-está-acontecendo-por-baixo-dos-panos)


## Objetivo

Criar cliente e servidor gRPC para criar uma aplicação de controle remoto de uma máquina Linux. O objetivo é permitir que o cliente envie comandos em formato de string para o servidor, que irá executar esses comandos em uma máquina Linux e retornar o resultado para o cliente.

## Descrição

A aplicação deverá ser composta por um servidor e um cliente, implementados usando gRPC e Python. O servidor deve estar configurado para receber comandos em formato de string do cliente e executá-los em uma máquina Linux. O cliente deve permitir que o usuário insira os comandos que deseja executar e exibir o resultado da execução.

## Requisitos

### Essencias (solicitados pelo professor)

- [x] O servidor deve ser capaz de receber comandos em formato de string do cliente e executá-los em uma máquina Linux;
- [x] O cliente deve permitir que o usuário insira os comandos que deseja executar no servidor e exibir o resultado da execução;
- [x] O código deve ser modularizado e organizado em pacotes e módulos;
- [x] Deve ser possível executar o servidor e o cliente em máquinas diferentes;
- [x] O servidor e o cliente devem ser implementados usando gRPC e Python.

### Opcionais (eu quero implementar)

- [x] Criar containers diferentes para cliente e servidor;

> Nunca fiz isso. Se tomar muito tempo, vou acabar deixando para outra hora.

- [x] Permitir que o usuário passe um arquivo `.sh` para o servidor para execução;

> Esse com certeza é muito mais fácil do que parece. O motivo principal para fazer isso é dar sentido ao uso do click, já que posso criar uma flag para passar o `PATH` do script.

## Dicas

- [x] Utilize a biblioteca subprocess para executar comandos bash no servidor;
- [x] Utilize a biblioteca grpc para implementar a comunicação entre o cliente e o servidor;
- [x] Utilize a biblioteca click para implementar a interface de linha de comando do cliente;
- [x] Organize o código em pacotes e módulos para facilitar a manutenção e reutilização.

> Essa tem sido a parte mais difícil, por se tratar de um código tão pequeno. Mas acredito que conforme for adicionando novas coisas, isso será necessário para manter o [SRP](https://en.wikipedia.org/wiki/Single-responsibility_principle).

## Bônus

Implemente alguma funcionalidade adicional na aplicação, como por exemplo:

- [x] Autenticação e autorização de usuários;

> Parece bem fácil, baseado na [documentação](https://grpc.io/docs/guides/auth/#python), vou começar por aqui.

- [ ] Execução de comandos em múltiplas máquinas ao mesmo tempo;

> Somente vai ser possível implementar e testar isso depois de criar um container para o servidor, pelo menos.

- [ ] Implementação de um sistema de logs para armazenar as informações de execução;

> Pensei em usar o RabbitMQ que foi estudado anteriormente, mas sinceramente, não sei se vale a complexidade que vai adicionar ao sistema. Vou optar por salvar os logs em arquivo de texto na máquina do servidor.

- [x] Utilização de criptografia para garantir a segurança na comunicação entre o cliente e o servidor.

> Pelo que entendi, ao incluir a autenticação no gRPC, os dados serão encriptogrados, então vou focar na autenticação.

## Como rodar o código

### Dependências

- `git`
- `docker`

### Comandos

```bash
git clone git@github.com:ed-henrique/distributed-systems.git
cd grpc

# Dê permissão de execução para os scripts utilizados
chmod u+x install.sh uninstall.sh

# Instala as imagens e cuida de sincronizar as chaves utilizadas entre elas
./install.sh

### Execução do código usando containers em Docker
# Criar network
docker network create my_network

### OBS: RODE OS DOIS COMANDOS ABAIXO EM TERMINAIS DIFERENTES

# Rodar servidor
docker run --rm -it --name server --network=my_network -p 50051:50051 -v certs:/app/certs server:eduardo_machado

# Rodar cliente
docker run --rm -it --network=my_network -v certs:/app/certs client:eduardo_machado bash

# Quando terminar, use esse código para remover containers, imagens, volumes e networks utilizados
./uninstall.sh
```

#### Explicação do que está acontecendo por baixo dos panos

1. No `install.sh`, o único comando relevante é o `docker compose build`, que realiza o build das imagens.
2. No servidor e cliente, temos as seguintes opções:
  - `--rm`: remove o container após sua execução
  - `-it`: integra o container ao terminal, para que este fique interativo
  - `--network`: passa a network à qual o container deve se conectar
  - `-p`: torna uma porta do container disponível para o host
  - `-v`: passa o volume que o container vai usar
3. No `uninstall.sh`, os comandos relevantes são:
  - `docker rm -f`: foi configurado de uma forma que apenas vai remover os containers que usarem a tag `eduardo_machado`
  - `docker image rm`: foi configurado de uma forma que apenas vai remover as imagens que usarem a tag `eduardo_machado`
  - `docker volume prune -f`: remove todos os volumes não utilizados
  - `docker network prune -f`: remove todas as networks não utilizadas