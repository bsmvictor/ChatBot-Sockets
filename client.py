from socket import *  
from threading import Thread

# Endereço do Servidor
servername = 'localhost'  
serverPort = 12000  
clientSocket: socket = None

def receive_thread_func():
    global clientSocket
    while True:
        try:
            modifiedSentence, serverAddress = clientSocket.recvfrom(1024)  
            print("\n", modifiedSentence.decode('utf-8'))
        except:
            pass

def send_message(message: str):
    global clientSocket
    clientSocket.sendto(message.encode('utf-8'), (servername, serverPort))  
    modifiedSentence, serverAddress = clientSocket.recvfrom(1024)  
    print("\n" + modifiedSentence.decode('utf-8'))

def main():
    global clientSocket
    # Criação do socket INET, STREAM (UDP)
    clientSocket = socket(AF_INET, SOCK_DGRAM)  
    clientSocket.settimeout(1000)  

    # Inicia a thread de recebimento
    receive_thread = Thread(target=receive_thread_func)
    receive_thread.start()

    # Mensagem inicial para o usuário
    input('Pressione qualquer tecla para iniciar a conversa...')  

    # Envia uma mensagem inicial para o servidor, que fará com que ele adicione o cliente e envie a mensagem de boas-vindas
    send_message("")

    # Loop para continuar enviando mensagens
    while True:
        sentence = input('\nDigite sua opção: ')  
        send_message(sentence)

if __name__ == "__main__":
    main()
