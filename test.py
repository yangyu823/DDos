import sys
import random
import os
import socket

i = 0
test = random._urandom(1490)
test2 = bytes(512)

os.system("figlet DDos Attack");
# print(test2);
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(bytes(512), ("127.0.0.1", 8888))
ip = socket.gethostbyname("yyan823.herokuapp.com")
# port = 8888
# while i < 1000000:
#     sock.sendto(test, ("127.0.0.1", port))
#     # print(i)
#     i += 1
print(ip)
