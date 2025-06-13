from socket import socket, AF_INET, SOCK_STREAM
from multiprocessing import Process, Queue
import time
import sys

if len(sys.argv) > 1:
    parametro = int(sys.argv[1])
else:
    parametro = 8080

def worker(task_queue):
    while True:
        if not task_queue.get():
            conn, addr = task_queue.get()
            print(f"Procesando la solicitud de {addr}")
            try:
                data = conn.recv(1024)
                print(f"Mensaje recibido de {addr}: {data.decode()}")
                time.sleep(1)
                conn.sendall(b"Respuesta del servidor")
            except:
                time.sleep(.1)

def start_server(host='localhost', port = parametro, num_workers = 3):
    server_socket = socket(AF_INET, SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    print(f"Servidor escuchando en {host} : {parametro}")

    task_queue = Queue()

    workers = [Process(target=worker, args=(task_queue,))]
    for w in workers:
        w.start()
    try:
        while True:
            conn, addr = server_socket.accept()
            print(f"Cliente conectado: {addr}")
            task_queue.put((conn, addr))
    except KeyboardInterrupt:
        print("Servidor detenido manualmente")
    finally:
        server_socket.close()

if __name__ == "__main__":
    start_server()
