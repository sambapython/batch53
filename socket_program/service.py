"""
hostname, portnumber
form the url to connect your service
wait for the client request
accept the client request.
need to process the request
send response back to corresponding client
"""
import socket
from time import sleep
host = socket.gethostname()
port=8891
s=socket.socket()
s.bind((host,port))
s.listen(20)
import threading
def req_process():
		ack = b"Hello firefox how are you??"
		client_socket.send(ack)
		req_num=client_socket.recv(3)
		print("requested number:",req_num)
		sleep(30)
		if int(req_num)%2==0:
			resp=b"EVEN"
		else:
			resp=b"ODD"
		client_socket.send(resp)

try:
	while True:
		print("server running in:%s:%s"%(host,port))
		client_socket, client_info = s.accept()
		#ack=bytearray("Hello firefox how are you??","utf-8")
		#len_ack="%s"%len(ack)
		#len_ack = bytearray(len_ack,"utf-8")
		#client_socket.send(len_ack)
		#client_socket.send(ack)
		t = threading.Thread(target=req_process)
		t.start()

except Exception as err:
	print(err)
finally:
	s.close()