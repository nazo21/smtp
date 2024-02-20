from socket import *
import ssl
import base64

msg = "\r\n I love computer networks!"
endmsg = "\r\n.\r\n"
# Choose a mail server (e.g. Google mail server) and call it mailserver
mailserver = 'smtp.gmail.com'  #Fill in start #Fill in end
# Create socket called clientSocket and establish a TCP connection with mailserver
#Fill in start
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((mailserver, 587))
#Fillin end
recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '220':
   print('220 reply not received from server.')
# Send HELO command and print server response.
heloCommand = 'EHLO Alice\r\n'
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != '250':
   print('250 reply not received from server.')


#Request an encrypted connection

command = 'STARTTLS\r\n'.encode()
clientSocket.send(command)
recv = clientSocket.recv(1024).decode()
print(recv)

if recv[:3] != '220':
    print ('220 reply not received from server')

#Encrypt the socket
clientSocket = ssl.wrap_socket(clientSocket)

# email and password for authentication
email = (base64.b64encode('##########'.encode())+ ('\r\n').encode())
password= (base64.b64encode('#############'.encode())+ ('\r\n').encode())

#Authentication 
clientSocket.send('AUTH LOGIN \r\n'.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != '334':
    print ('334 reply not received from server')

clientSocket.send(email)
recv1 = clientSocket.recv(1024).decode()
print(recv1)

if recv1[:3] != '334':
    print ('334 reply not received from server')

clientSocket.send(password)
recv1 = clientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != '235':
    print ('235 reply not received from server')


# Send MAIL FROM command and print server response.
# Fill in start
sendmailcommand = 'MAIL FROM: ##########<########>\r\n'
clientSocket.send(sendmailcommand.encode())
recv2 = clientSocket.recv(1024).decode()
print(recv2)
if recv2[:3] != '250':
   print('250 reply not received from server.')

# Fill in end
# Send RCPT TO command and print server response.
# Fill in start
print('test rcptmailcommand')
rcptmailcommand = 'RCPT TO: ######\r\n'
clientSocket.send(rcptmailcommand.encode())
recv2 = clientSocket.recv(1024).decode()
print(recv2)

# Fill in end
# Send DATA command and print server response.
print('test Send_Data')
Send_Data = 'Data\r\n'
clientSocket.send(Send_Data.encode())
recv2 = clientSocket.recv(1024).decode()
print(recv2)

# Send message data.
# Fill in start
print('test msg data')
clientSocket.send(("Subject: #######").encode())
clientSocket.send(("To: ############# \r\n").encode())
clientSocket.send(msg.encode())
print(recv2)

# Fill in end
# Message ends with a single period.
print('test msg period data')
clientSocket.send(endmsg.encode())
recv2 = clientSocket.recv(1024).decode()
print(recv2)
if recv2[:3] != '250':
   print('250 reply not received from server.')
# Send QUIT command and get server response.
# Fill in start
print("Test Send QUIT")
clientSocket.send("QUIT\r\n".encode())
recv2 = clientSocket.recv(1024)
print(recv2.decode())

clientSocket.close()

print("Mail Sent")
# Fill in end
