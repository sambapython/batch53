def fun(x1,x2):
    print("x1=%s, x2=%s"%(x1,x2))
    return x1+x2
l1=[1,2,3,4]
l2=[5,6,7,8,9,10]
list(map(fun,l1,l2))