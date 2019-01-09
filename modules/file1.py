print("name:",__name__)
a=100
b=200
c=a+b
d=a-b
def fun():
	print("this is fun in file1")
if __name__=="__main__":
	def fun1():
		print("this is fun1")
	print("this is file1")
	fun()
	print(a,b,c,d)
