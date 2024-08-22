from socket import *

# Endereço do Servidor
servername = 'localhost'
serverPort = 12000
clientSocket = None

def send_message(message: str):
    global clientSocket
    clientSocket.sendto(message.encode('utf-8'), (servername, serverPort))
    modifiedSentence, serverAddress = clientSocket.recvfrom(1024)
    resposta = modifiedSentence.decode('utf-8')
    print("\n" + resposta)
    return resposta

def main():
    global clientSocket
    # Criação do socket INET, STREAM (UDP)
    clientSocket = socket(AF_INET, SOCK_DGRAM)
    clientSocket.settimeout(1000)

    # Mensagem inicial para o usuário
    input('Pressione qualquer tecla para iniciar a conversa...')

    # Envia uma mensagem inicial para o servidor, que fará com que ele adicione o cliente e envie a mensagem de boas-vindas
    resposta = send_message("")

    # Loop para continuar enviando mensagens
    while True:
        if "Encerrando o chat. Obrigado!" in resposta:
            break
        
        sentence = input('\nDigite sua opção: ')
        resposta = send_message(sentence)

    clientSocket.close()

if __name__ == "__main__":
    main()
