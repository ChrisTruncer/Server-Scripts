#!C:\Python27

# Import our required libraries
import os
import re
import socket

network = '192.168.1.102'
port = 6667

ids_to_trigger = [4625]
for id in ids_to_trigger:
	os.system('wevtutil qe Security "/q:*[System [(EventID=' + str(id) +')]]" /f:text > eventlog.txt' )

# Just a different way to do the command above
# Use the OS command to dump the event log for the event id we need
# os.system('wevtutil qe Security "/q:*[System [(EventID=4625)]]" /f:text > eventlog.txt')

# Open our files we will be reading from and writing to
file = open('eventlog.txt','r')
file2 = open('targets.txt','w')

# Loop that "greps" for the IP address and writes it to a file
for line in file:
	if re.search('Source Network Address', line):
		line = line.split("\t")[2]
		file2.write(line)

file.close()
file2.close()

targetfile = open('targets.txt','r')
lines = sorted(set(targetfile.readlines()))
targetfile.close()

for line in lines:
	line = line.replace('\n','')
	if line == '127.0.0.1':
		print 'Not Localhost!'
	else:
		os.system('netsh advfirewall firewall add rule name=\"' + line + ' Blocked\" action=block dir=in remoteip=' + line + '')
		irc = socket.socket ( socket.AF_INET, socket.SOCK_STREAM )
		irc.connect ( ( network, port ) )
		irc.recv ( 4096 )
		irc.send ( 'NICK tester\r\n' )
		irc.send ( 'USER tester completely real :Jxxx\r\n' )
		irc.send ( 'JOIN #test\r\n' )
		irc.send ( 'PRIVMSG #test :Blocked ' + line + '\r\n' )
		irc.send ( 'QUIT :Testing message\r\n' )
		irc.close()

os.system('del eventlog.txt')
os.system('del targets.txt')
print 'Done!'
