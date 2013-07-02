#!C:\Python27

# Import our required libraries
import os
import re
import socket

network = '192.168.1.102'
port = 6667

ids_to_trigger = [1116]
for id in ids_to_trigger:
	os.system('wevtutil qe System "/q:*[System [(EventID=' + str(id) +')]]" /f:text > mselog.txt' )

os.system('ipconfig > ipconfig.txt')

file1 = open('ipconfig.txt','r')
file2 = open('ip.txt', 'w')

for line in file1:
	if re.search('IPv4 Address', line):
		line = line.split(" ")[16]
		file2.write(line)

filesize = os.lstat("mselog.txt")[6]

file1.close()
file2.close()

if filesize == 0:
	print "It's empty"
else:
	file3 = open('ip.txt', 'r')
	for row in file3:
		irc = socket.socket ( socket.AF_INET, socket.SOCK_STREAM )
		irc.connect ( ( network, port ) )
		irc.recv ( 4096 )
		irc.send ( 'NICK mse\r\n' )
		irc.send ( 'USER mse completely real :Jxxx\r\n' )
		irc.send ( 'JOIN #test\r\n' )
		irc.send ( 'PRIVMSG #test :investigate ' + row + '\r\n' )
		irc.send ( 'QUIT :Testing message\r\n' )
		irc.close()
	print "detected something"

os.system('del mselog.txt')
print 'Done!'
