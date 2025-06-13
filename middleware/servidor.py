# Servidor Web
import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost',12345))

# Escucha las conexiones entrantes
server_socket.listen(1)
print("Esperando conexión ...")

# Acepta una conexión entrante
conn, addr = server_socket.accept()
print(f"Conectado por {addr}")

# El tamaño del buffer es 1024 bytes, no tan grande para evitar problemas de memoria, no tan pequeño para no fragmentar mensajes grandes
data = conn.recv(1024)
print("Mensaje recibido:", data.decode())

conn.sendall(b"Hola desde el servidor!")
conn.close()