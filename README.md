[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/TPGyf4AW)

---

This is a simple example to demonstrate how stubs can be used as remote references in RPC systems. The example was extracted from (Tanenbaum and van Steen, 2025).

---

## Funcionamento do programa

descreva o mecanismo demonstrado no exemplo e discuta como ele pode ser generalizado

- `client.py` funciona como um cliente que envia requests para o servidor
- `server.py` interpreta chamadas com formato \[OPERAÇÃO, dados, id_lista\] e armazena as listas do "banco de dados"
- `dbclient.py` funciona como um serviço de banco de dados criando, consultando e fazendo append de listas
- `run.py` simula o envio por 2 clientes para 1 servidor de um criando duas listas, cada uma por um cliente com um identficador "Cliente N". No final a classe Server mostra as duas listas depois da operação de APPEND.
