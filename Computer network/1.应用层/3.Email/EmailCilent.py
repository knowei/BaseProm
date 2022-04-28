import base64
from socket import *

# 邮箱标题
msg = "\r\n I love computer networks!"
endmsg = "\r\n.\r\n"
# Choose a mail server (e.g. Google mail server) and call it mailserver
# 登入QQ邮箱的服务器
mailserver = 'smtp.qq.com'
# 邮箱账号
mailUser = "2994172661"
# 你的邮箱的账号
mailFromAddress = "2994172661@qq.com"
# 登入邮箱的授权码(有关授权码自行百度即可)
mailPass = "wgezhgjhsorydgeb"
# 目的邮箱
mailToAddress = "748354158@qq.com"

msg = 'FROM: ' + mailFromAddress + '\r\n'
msg += 'TO: ' + mailToAddress +  '\r\n'
msg += 'Subject: ' + 'test' +  '\r\n'
# 需要发送的内容，可自行改变
msg += "\r\n I love computer networks!"
endmsg = "\r\n.\r\n"
# Create socket called clientSocket and establish a TCP connection with mailserver
clientSocket = socket(AF_INET, SOCK_STREAM)
# 使用25端口
clientSocket.connect((mailserver, 25))

recv = clientSocket.recv(1024)
recv = recv.decode()
print(recv)
if recv[:3] != '220':
    print
    '220 reply not received from server.'

# Send HELO command and print server response.
# 想服务器问好
heloCommand = 'HELO lizhan\r\n'
while True:
    clientSocket.send(heloCommand.encode())
    recv = clientSocket.recv(1024)
    recv = recv.decode()
    print(recv)
    if recv[:3] == '250':
        break


# Send MAIL FROM command and print server response.
# Fill in start
loginCommand = "auth login\r\n"
while True:
    clientSocket.send(loginCommand.encode())
    recv = clientSocket.recv(1024)
    recv = recv.decode()
    if recv[:3] == '334':
        break

# Fill in end

userCommand = base64.b64encode(mailFromAddress.encode()) + b'\r\n'
while True:
    clientSocket.send(userCommand)
    recv = clientSocket.recv(1024)
    recv = recv.decode()
    print(recv)
    if recv[:3]=='334':
        break

passCommand = base64.b64encode(mailPass.encode()) + b'\r\n'
while True:
    clientSocket.send(passCommand)
    recv = clientSocket.recv(1024)
    recv = recv.decode()
    print(recv)
    if recv[:3]=='235':
        break

MFCommand = "MAIL FROM:<" + mailFromAddress +'>\r\n'
while True:
    clientSocket.send(MFCommand.encode())
    recv = clientSocket.recv(1024)
    recv = recv.decode()
    print(recv)
    if recv[:3] == '250':
        break

RECommand = "rcpt to:<" + mailToAddress + '>\r\n'
while True:
    clientSocket.send(RECommand.encode())
    recv = clientSocket.recv(1024)
    recv = recv.decode()
    print(recv)
    if recv[:3] == '250':
        break

DaCommand = 'data\r\n'
while True:
    clientSocket.send(DaCommand.encode())
    recv = clientSocket.recv(1024)
    recv = recv.decode()
    print(recv)
    if recv[:3] == '354':
        break

clientSocket.send(msg.encode())
while True:
    clientSocket.send(endmsg.encode())
    recv = clientSocket.recv(1024)
    recv = recv.decode()
    print(recv)
    if recv[:3] == '250':
        break