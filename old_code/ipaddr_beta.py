ip = "192.168.10.50"

IPaddr = ip.split(".",maxsplit =-1)
if int(IPaddr[0]) == 192 and int(IPaddr[1]) == 168:
	print("This is Class C IP address")
else:
    print("This is not Class C")
