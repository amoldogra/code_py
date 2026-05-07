import socket

target = "192.168.1.21"
for port in range(1,1025):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    result =s.connect_ex((target,port))
    if result == 0:
        print(f"Port: {port}")
s.close        

