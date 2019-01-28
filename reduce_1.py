def fun(x,y):
	return x+y
print(reduce(fun,[1,2,3,4]))
#fun(1,2)-->3
#fun(3,3)-->6
#fun(6,4)-->10
#result as a 10
def fun(x,y):
	return x*y
print(reduce(fun,[1,2,3,4]))
#fun(1,2)-->2
#fun(2,3)-->6
#fun(6,4)-->24
#result as a 24