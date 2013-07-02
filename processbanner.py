#!C:\Python27

# Import our required libraries
import os
import re
import socket

network = '192.168.1.102'
port = 6667

# Use the OS command to dump running processes minus those which are whitelisted within the command
os.system('tasklist /fi \"IMAGENAME ne System Idle Process\" /fi \"IMAGENAME ne System\"  > processes.txt')

# Open our files we will be reading from and writing to
file = open('processes.txt','r')
file2 = open('badprocesses.txt','w')

# Loop that "greps" for the IP address and writes it to a file
for line in file:
		line = line.split(" ")[0]
		file2.write(line + '\n')

file2.close()
file2 = open('badprocesses.txt','r')
processes = file2.readlines()
file3 = open('sanitizedprocess.txt','w')
file3.writelines(processes[4:])

file.close()
file2.close()
file3.close()

os.system('del processes.txt')
os.system('del badprocesses.txt')

filesize = os.lstat("sanitizedprocess.txt")[6]

if filesize == 0:
	print "It's empty"
else:
	os.system('netstat -n > networkconns.txt')
	file4 = open('networkconns.txt','r')
	file5 = open('foreignips.txt','w')
	nextline = file4.readlines()
	file5.writelines(nextline[4:])
	file4.close()
	file5.close()
	os.system('del networkconns.txt')
	file6 = open('foreignips.txt','r')
	file7 = open('ipport.txt','w')
	for badips in file6:
		badips = badips.split(" ")[9]
		file7.write(badips + '\n')
	file6.close()
	file7.close()
	file8 = open('ipport.txt','r')
	file9 = open('badips.txt','w')
	for ips in file8:
		ips = ips.split(":")[0]
		file9.write(ips + '\n')
	file8.close()
	file9.close()
	targetfile = open('badips.txt','r')
	poopoo = sorted(set(targetfile.readlines()))
	targetfile.close()
	#file10 = open('badips.txt','r')
	for ban in poopoo:
		ban = ban.strip()
		command = "netsh advfirewall firewall add rule name=\"Banned " + ban + "\" action=block dir=in remoteip=" + ban
		os.system(command)
		irc = socket.socket ( socket.AF_INET, socket.SOCK_STREAM )
		irc.connect ( ( network, port ) )
		irc.recv ( 4096 )
		irc.send ( 'NICK tester2\r\n' )
		irc.send ( 'USER tester2 completely real :Jxxx\r\n' )
		irc.send ( 'JOIN #test\r\n' )
		irc.send ( 'PRIVMSG #test :Blocked ' + ban + '\r\n' )
		irc.send ( 'QUIT :Testing message\r\n' )
		irc.close()

#9 spaces

os.system('del sanitizedprocess.txt')
os.system('del ipport.txt')
os.system('del foreignips.txt')
os.system('del badips.txt')
print 'Done!'
