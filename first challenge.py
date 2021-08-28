import telnetlib
import getpass


IP = input("Enter the IP Address: ")
user = input("Enter your Username: ")
password = getpass.getpass()

tn = telnetlib.Telnet(IP)

tn.read_until(b"Username: ")
tn.write(user.encode('ascii') + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

tn.write(b"enable\n")
tn.write(b"cisco\n")
tn.write(b"conf t\n")
tn.write(b"no vlan 10\n")
tn.write(b"no int vlan 10\n")
tn.write(b"int lo2\n")
tn.write(b"ip add 3.3.3.3 255.255.255.255\n")
tn.write(b"username admin secret cisco\n")
tn.write(b"end\n")
tn.write(b"sh run\n")
tn.write(b"\n")
tn.write(b"exit")

print(tn.read_all().decode('ascii'))
