# Servidor Web

# Importar la bib socket
import socket

# Definiendo parametros
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Asociar ip y puerto
server_socket.bind(('localhost', 8080))

# Se levanta y escucha el puerto
server_socket.listen(1)
print("Servidor ejecutandose...")

# Acepta la conexion
conn, addr = server_socket.accept()
print("Esperando conexiones en el puerto {addr}")

# Recepcion de los paquetes
data = conn.recv(1024)
print("Mensaje recibido: ", data.decode())

conn.sendall(b"Hola desde el servidor!")
conn.close()