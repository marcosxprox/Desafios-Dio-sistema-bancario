# Sistema Bancário - Desafios DIO

Este repositório contém o código do projeto de um sistema bancário desenvolvido como parte dos desafios da plataforma DIO (Digital Innovation One). O sistema é composto por funcionalidades que permitem realizar operações bancárias básicas, como cadastro de clientes, criação de contas correntes, depósitos, saques e exibição de extratos.

## Versões do Sistema

### Versão 1.0 - Implementação Inicial

- **Funcionalidades:**
  - Cadastro de clientes e validação de CPF.
  - Criação de conta corrente.
  - Realização de depósitos e saques.
  - Exibição de extrato das transações realizadas.

- **Tecnologias Utilizadas:**
  - Python
  - Orientação a Objetos
  - Arquivos separados para estruturação do código.

- **Observações:**
  - Primeira versão focada em implementar a estrutura básica do sistema bancário.

### Versão 1.1 - Melhoria na Validação de CPF

- **Funcionalidades:**
  - Implementação da validação do CPF de forma mais robusta ao cadastrar um cliente.
  - Melhorias no controle de saldo e histórico de transações.

- **Tecnologias Utilizadas:**
  - Python
  - Estrutura de dados mais organizada.

- **Observações:**
  - Refatoração do código para garantir a segurança e integridade dos dados inseridos no sistema.

### Versão 1.2 - Inclusão de Classes para Transações

- **Funcionalidades:**
  - Adição de classes `Depositar` e `Saque` para representar transações.
  - Melhoria na exibição de extratos.
  - Adição de um menu interativo com opções para realizar as operações bancárias.

- **Tecnologias Utilizadas:**
  - Python
  - Arquitetura mais modular com classes separadas para cada operação.

- **Observações:**
  - O sistema agora possui transações como objetos, o que facilita futuras expansões.

### Versão 1.3 - Sistema Bancário Modularizado

- **Funcionalidades:**
  - Modularização do código em diferentes arquivos como `pessoa_fisica.py`, `historico.py`, `interface_transacao.py`, e `conta_corrente.py`.
  - Melhorias no código para facilitar a manutenção e expansão do sistema.

- **Tecnologias Utilizadas:**
  - Python
  - Modularização com Arquivos Separados.

- **Observações:**
  - O código agora é mais organizado e fácil de manter. Também facilita a adição de novas funcionalidades.
