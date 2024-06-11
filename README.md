# Sistema Bancário

## Objetivo do Projeto

O objetivo deste projeto é criar um sistema bancário simples que permite aos usuários realizar as operações de sacar, depositar e visualizar o extrato de suas transações.

## Operação de Sacar

- É possível sacar valores positivos.
- Todas as transações de saque são armazenadas para posterior inclusão no extrato.
- O sistema impõe os seguintes limites para saques:
  - Limite de 3 saques diários.
  - Limite de R$ 500,00 por saque.
- Se não houver saldo suficiente para efetuar um saque, uma mensagem será exibida ao usuário informando a impossibilidade da operação.

## Operação de Extrato

- Ao visualizar o extrato, todas as operações realizadas são listadas.
- No final do extrato, é exibido o saldo atual da conta.
- Se não houver transações no extrato, será exibida a mensagem "Não foram realizadas movimentações".

