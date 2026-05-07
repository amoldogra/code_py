import socket

HOST, PORT = '127.0.0.1', 65432
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()

with conn:
    print("connected:", addr)
    conn.sendall(b'Hello, socket!')

