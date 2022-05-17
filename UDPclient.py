from socket import *
serverName = '192.168.100.4'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
messagetoserver = raw_input('Entrer un Message pour le  Serveur: ')
clientSocket.sendto(messagetoserver, (serverName, serverPort))
messagefromserver, serverAddress = clientSocket.recvfrom(2048)
print 'Reponse du Server: ', messagefromserver
clientSocket.close()
