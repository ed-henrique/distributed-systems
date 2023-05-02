# Echo Reply Reverse

Cliente-servidor onde:

- `client.py`: envia mensagens para o servidor e recebe respostas do mesmo, com as mensagens invertidas. Possui um modo DOS para simular um ataque ao servidor.
- `server.py`: recebe mensagens dos clientes, as inverte e as envia de volta

Ambos operam de forma multithread e se comunicam por socket.

## Imports Necessários

- time
- socket
- threading

## Relatório

Usando as seguintes ferramentas:

- `htop`
- `pidstat`

Foi verificado que o tamanho da mensagem não importava, e que o servidor sempre rodava com menos de 2% de uso de CPU e RAM.

Para verificar a largura de banda, podemos usar a seguinte ferramenta:

- `iftop`
