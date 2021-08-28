import telnetlib
import getpass


IP = input("Enter the IP Address: ")
user = input("Enter your Username: ")
password = getpass.getpass()

tn = telnetlib.Telnet(IP)

tn.read_until(b"Username: ")
tn.write(user.encode('ascii') + b"\n")
if password:
    tn.write(password.encode('ascii') + b"\n")

tn.write(b"enable\n")
tn.write(b"cisco\n")
tn.write(b"conf t\n")
tn.write(b"vlan 10\n")
tn.write(b"name LAB\n")
tn.write(b"exit\n")
tn.write(b"int vlan 10\n")
tn.write(b"ip add 10.1.10.1 255.255.255.0\n")
tn.write(b"no shut\n")
tn.write(b"end\n")
tn.write(b"sh ip int brief\n")
tn.write(b'exit\n')

print(tn.read_all().decode('ascii'))
