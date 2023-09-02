import socket

def send_message(ip, port, message):
    try:
        # Cria um socket TCP
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            # Conecta ao host e porta especificados
            s.connect((ip, port))
            
            # Envia a mensagem para o host remoto
            s.sendall(message.encode())
            
            # Aguarda e exibe a resposta
            data = s.recv(130000)
            print(f"Resposta do host remoto: {data.decode()}")
            data = s.recv(130000)
            print(f" {data.decode()}")
    except Exception as e:
        print(f"Erro: {e}")

print("\x1bc\x1b[44;37m")
if __name__ == "__main__":
    ip = input("Digite o endereço IP do host remoto: ")
    port = int(input("Digite o número da porta: "))
    message = input("Digite a mensagem a ser enviada: ")
    
    send_message(ip, port, message+"\r\n\r\n")
