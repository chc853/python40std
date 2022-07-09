import socket
import requests
import re


in_addr1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
in_addr1.connect(("www.google.co.kr",443))
print("내부 IP : ",in_addr1.getsockname()[0])

req = requests.get("http://ipconfig.kr")
#print(req.text)
out_addr = re.search(r'IP Address : (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', req.text)[1]
print("외부 IP : ", out_addr)
