# Aplicação de Chat Simples via UDP

Este repositório contém uma aplicação de chat simples que utiliza o protocolo UDP (User Datagram Protocol) para permitir a comunicação entre um cliente e um servidor. O projeto demonstra o uso de sockets em Python para criar uma aplicação básica de troca de mensagens, incluindo funcionalidades de estado no servidor para responder a diferentes comandos enviados pelo cliente.

## Estrutura do Projeto

- **Servidor (server.py):** Responsável por receber mensagens do cliente, processar o estado atual da conversa, e enviar respostas adequadas de volta ao cliente.
- **Cliente (client.py):** Envia mensagens ao servidor e exibe as respostas recebidas. O cliente interage com o usuário final para capturar entradas e exibir as respostas do servidor.

## Funcionalidades

- **Estados do Servidor:** O servidor gerencia diferentes estados de uma conversa (MENU, TELEFONE, INTERNET, ENCERRAR) e responde de acordo com as entradas do cliente.
- **Interação Cliente-Servidor:** O cliente envia opções para o servidor, que processa as opções e retorna mensagens apropriadas.
- **Encerramento de Conversa:** O servidor pode encerrar a conversa com o cliente, após o qual o cliente encerrará sua execução.

## Pré-requisitos

Para rodar a aplicação, você precisará de:

- **Python 3.x** instalado na sua máquina.

## Como Utilizar

## 1. Clonar o Repositório

Primeiro, clone este repositório em sua máquina local:

```bash
git clone https://github.com/bsmvictor/ChatBot-Sockets
```

## 2. Navegue até o diretório do projeto

```bash
cd ./ChatBot-Sockets
```

## 3. Iniciar o Servidor

Inicie o servidor executando:

```bash
python server.py
```
O servidor estará pronto para aceitar conexões e exibirá "Server Ready".

## 4. Iniciar o Cliente

Em outro terminal, ainda no diretório do projeto, execute o cliente:

```bash
python client.py
```
O cliente solicitará que você pressione qualquer tecla para iniciar a conversa. Após isso, você poderá interagir com o servidor enviando diferentes opções.

## 5. Interagindo com a aplicação

- Menu Inicial:
  - Opção 1: Seleciona "Telefone".
  - Opção 2: Seleciona "Internet".
  - Opção 3: Encerra a conversa.
  
- Telefone:
  - Opção 3: Retorna ao menu inicial.
  
- Internet:
  - Opção 1: Exibe o consumo atual.
  - Opção 2: Exibe o valor da fatura atual.
  - Opção 3: Retorna ao menu inicial.

## Colaboradores do Projeto

- Victor Boaventura Souza Muniz
- Igor Nogueira Olivio
