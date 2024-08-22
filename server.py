from socket import *

# Porta do servidor
PortaServidor = 12000

# Criação do socket UDP e configuração do servidor
SocketServidor = socket(AF_INET, SOCK_DGRAM)
SocketServidor.bind(('', PortaServidor))  # Vincula o socket à porta especificada
SocketServidor.settimeout(1000)  # Define um timeout de 1000 segundos para o socket

# Dicionário para armazenar o estado de cada cliente
chats = {}

# Definição dos estados do diálogo
MENU = "MENU"
TELEFONE = "TELEFONE"
INTERNET = "INTERNET"
ENCERRAR = "ENCERRAR"

# Mensagem inicial enviada ao cliente quando ele se conecta
mensagem_inicial = "Bom dia, clique: 1 para telefone, 2 para internet ou 3 para encerrar."

print("Server Ready")

# Loop principal do servidor
while True:
    try:
        # Recebe a mensagem do cliente
        Palavra, EnderecoCliente = SocketServidor.recvfrom(1024)
        mensagem_recebida = Palavra.decode('utf-8')
        print(f"Recebido do cliente: {EnderecoCliente}", mensagem_recebida)

        # Verifica se o cliente já está no dicionário de chats
        if EnderecoCliente not in chats:
            # Se não estiver, adiciona o cliente ao dicionário com o estado inicial MENU
            chats[EnderecoCliente] = {"estado": MENU, "historico": []}
            print("Cliente adicionado")
            # Envia a mensagem inicial ao cliente
            SocketServidor.sendto(mensagem_inicial.encode('utf-8'), EnderecoCliente)
            continue  # Pula para a próxima iteração do loop

        # Armazena a mensagem recebida no histórico do cliente
        chats[EnderecoCliente]["historico"].append(mensagem_recebida)

        # Obtém o estado atual do cliente
        estado_atual = chats[EnderecoCliente]["estado"]
        resposta = ""

        # Lógica de estados
        if estado_atual == MENU:
            if mensagem_recebida == "1":
                resposta = "Você escolheu telefone. Digite 3 para retornar ao menu."
                chats[EnderecoCliente]["estado"] = TELEFONE  # Transição para o estado TELEFONE
                
            elif mensagem_recebida == "2":
                resposta = "Você escolheu internet. Digite 1 para consumo, 2 para valor da fatura, ou 3 para retornar ao menu."
                chats[EnderecoCliente]["estado"] = INTERNET  # Transição para o estado INTERNET
                
            elif mensagem_recebida == "3":
                chats[EnderecoCliente]["estado"] = ENCERRAR  # Transição para o estado ENCERRAR
                resposta = "\n\tEncerrando o chat. Obrigado!"
                
            else:
                resposta = "Opção inválida. Por favor, digite 1 para telefone, 2 para internet, ou 3 para encerrar."

        elif estado_atual == TELEFONE:
            if mensagem_recebida == "3":
                chats[EnderecoCliente]["estado"] = MENU  # Volta para o estado MENU
                resposta = mensagem_inicial  # Envia a mensagem inicial novamente
            else:
                resposta = "Opção inválida. Digite 3 para voltar ao menu."

        elif estado_atual == INTERNET:
            if mensagem_recebida == "1":
                resposta = "Seu consumo atual é de 50GB. Digite 3 para voltar ao menu."
                
            elif mensagem_recebida == "2":
                resposta = "O valor da sua fatura atual é R$ 120,00. Digite 3 para voltar ao menu."
                
            elif mensagem_recebida == "3":
                chats[EnderecoCliente]["estado"] = MENU  # Volta para o estado MENU
                resposta = mensagem_inicial  # Envia a mensagem inicial novamente
                
            else:
                resposta = "Opção inválida. Digite 1 para consumo, 2 para valor da fatura, ou 3 para voltar ao menu."

        elif estado_atual == ENCERRAR:
            resposta = "\n\tEncerrando o chat. Obrigado!"
            SocketServidor.close()  # Fecha o socket do servidor ao encerrar o chat

        # Envia a resposta ao cliente
        SocketServidor.sendto(resposta.encode('utf-8'), EnderecoCliente)

        # Exibe o histórico de mensagens com o cliente no terminal
        print(f"Histórico com {EnderecoCliente}: {chats[EnderecoCliente]['historico']}")

    except timeout:
        # Tratamento de timeout, indicando que nenhuma mensagem foi recebida dentro do tempo limite
        print("Timeout. Nenhuma mensagem recebida do cliente.")
