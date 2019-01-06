l=["Banana","apple","Orange","Mango"]
def fun(x,y):
	if x.lower()>y.lower():
		return 1
	else:
		return -1
l.sort(cmp=fun)
print(l)