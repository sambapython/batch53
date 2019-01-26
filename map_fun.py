def fun(x):
    return "%s,EVEN"%x if x%2==0 else "%s,ODD"%x 
l=[10,23,45,2,4,67,89]
res=map(fun,l)
print(res)