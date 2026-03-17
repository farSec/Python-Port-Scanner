import socket
import termcolor


def scan(target, ports):
	print('\n' + 'Starting Scan For ' + str(target))
	for port in range(1,ports):
		scan_port(target, port)


def scan_port(ip,port):
	try:
		sock = socket.socket()
		sock.connect((ip,port))
		print("[+] Port Open " + str(port))
		sock.close()
	except:
		pass


targets = input("[*] Enter Targets To Scan(split them by ,): ")
ports = int(input("[*] Enter Ports To Scan: "))
if ',' in targets:
	print(termcolor.colored(("[*] Scanning Multiple Targets"), 'green'))
	for ip_addr in targets.split(','):
		scan(ip_addr.strip(' '), ports)
else:
	scan(targets,ports)
