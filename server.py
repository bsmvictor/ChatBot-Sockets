from socket import *

# Porta do servidor
PortaServidor = 12000

SocketServidor = socket(AF_INET, SOCK_DGRAM)
SocketServidor.bind(('', PortaServidor))
SocketServidor.settimeout(1000)

chats = {}

# Definição dos estados
MENU = "MENU"
TELEFONE = "TELEFONE"
INTERNET = "INTERNET"
ENCERRAR = "ENCERRAR"

mensagem_inicial = "Bom dia, clique: 1 para telefone, 2 para internet ou 3 para encerrar."

print("Server Ready")
while True:
    # Recebe a mensagem do cliente
    Palavra, EnderecoCliente = SocketServidor.recvfrom(1024)
    mensagem_recebida = Palavra.decode('utf-8')
    print(f"Recebido do cliente: {EnderecoCliente}", mensagem_recebida)
    
    # Verifica se o cliente já está no dicionário de chats
    if EnderecoCliente not in chats:
        chats[EnderecoCliente] = {"estado": MENU, "historico": []}
        print("Cliente adicionado")
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
            resposta = "Você escolheu telefone. Digite 3 para encerrar."
            chats[EnderecoCliente]["estado"] = TELEFONE
        elif mensagem_recebida == "2":
            resposta = "Você escolheu internet. Digite 1 para consumo, 2 para valor da fatura, ou 3 para encerrar."
            chats[EnderecoCliente]["estado"] = INTERNET
        elif mensagem_recebida == "3":
            resposta = "Encerrando o chat. Obrigado!"
            chats[EnderecoCliente]["estado"] = ENCERRAR
        else:
            resposta = "Opção inválida. Por favor, digite 1 para telefone, 2 para internet, ou 3 para encerrar."
    
    elif estado_atual == TELEFONE:
        if mensagem_recebida == "3":
            resposta = "Encerrando o chat. Obrigado!"
            chats[EnderecoCliente]["estado"] = ENCERRAR
        else:
            resposta = "Você escolheu telefone. Digite 3 para encerrar."
        
        # Volta para o estado inicial após responder
        chats[EnderecoCliente]["estado"] = MENU
        resposta += "\n" + mensagem_inicial

    elif estado_atual == INTERNET:
        if mensagem_recebida == "1":
            resposta = "Seu consumo atual é de 50GB."
        elif mensagem_recebida == "2":
            resposta = "O valor da sua fatura atual é R$ 120,00."
        elif mensagem_recebida == "3":
            resposta = "Encerrando o chat. Obrigado!"
            chats[EnderecoCliente]["estado"] = ENCERRAR
        else:
            resposta = "Opção inválida. Digite 1 para consumo, 2 para valor da fatura, ou 3 para encerrar."
        
        # Volta para o estado inicial após responder
        if mensagem_recebida in ["1", "2"]:
            chats[EnderecoCliente]["estado"] = MENU
            resposta += "\n" + mensagem_inicial

    elif estado_atual == ENCERRAR:
        resposta = "Conversa já encerrada. Para iniciar uma nova sessão, por favor reconecte."
    
    # Envia a resposta ao cliente
    SocketServidor.sendto(resposta.encode('utf-8'), EnderecoCliente)

    # Exibe o histórico de mensagens com o cliente
    print(f"Histórico com {EnderecoCliente}: {chats[EnderecoCliente]['historico']}")
