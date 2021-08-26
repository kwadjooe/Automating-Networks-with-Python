import getpass
import telnetlib

IP= input("Enter the IP Address: ")
user= input("Enter your Username: ")
password= getpass.getpass()
tn = telnetlib.Telnet(IP)


tn.read_until(b"Username: ")
tn.write(user.encode('ascii') + b"\n")

if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

tn.write(b"enable\n")
tn.write(b"cisco\n")
#tn.write(b"config terminal\n")
tn.write(b"show version\n")
tn.write(b"end\n")


print(tn.read_all().decode('ascii'))
