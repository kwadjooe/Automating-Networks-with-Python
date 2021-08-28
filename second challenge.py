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
tn.write(b"no int loo0\n")
tn.write(b"no int loo1\n")
tn.write(b"no int loo2\n")
tn.write(b"no username admin\n")
tn.write(b"\n")
tn.write(b"no username admin1\n")
tn.write(b"\n")
tn.write(b"end\n")
tn.write(b"sh run\n")
tn.write(b"\n")
tn.write(b"exit")

print(tn.read_all().decode('ascii'))
