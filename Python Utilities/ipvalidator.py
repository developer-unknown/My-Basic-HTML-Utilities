import socket 
IP = '127.0.0.1'
try:
   socket.inet_aton(IP)
   print("The IP address is valid")
except socket.error:
   print("The IP address in invalid")