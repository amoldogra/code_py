
import socket
import struct
import os

if not os.path.exists('iplist.txt'):
    print("Error: 'iplist.txt' file not found.")
    exit()

with open('iplist.txt', 'r') as file:
    monitored_ips = [line.strip() for line in file.readlines()]

host = socket.gethostbyname(socket.gethostname())
s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_RAW)
s.bind((host, 0))
s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

while True:
    packet, addr = s.recvfrom(65565)
    ip_header = packet[0:20]
    iph = struct.unpack('!BBHHHBBH4s4s', ip_header)
    
    version_ihl = iph[0]
    ihl = version_ihl & 0xF
    iph_length = ihl * 4

    src_addr = socket.inet_ntoa(iph[8])
    dst_addr = socket.inet_ntoa(iph[9])

    if src_addr in monitored_ips:
        print(f"Alert: Incoming connection for blacklisted IP {src_addr}!")

    if dst_addr in monitored_ips:
        print(f"Alert: Outgoing connection for blacklisted IP {dst_addr}!")
