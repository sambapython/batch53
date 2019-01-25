import socket
s=socket.socket()
host="khyaathipython"
port=8891
try:
	s.connect((host,port))
	#len_ack=s.recv(2)
	#print(len_ack)
	#len_ack=len_ack.decode("utf-8")
	ack=s.recv(1024)
	print("ack:",ack)
	number = bytearray(input("enter a number:"),"utf-8")
	print(number)
	s.send(number)
	resp=s.recv(1024)
	print(resp)

except Exception as err:
	print(err)
finally:
	s.close()


