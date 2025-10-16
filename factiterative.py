def inputnum():
    x=int(input())
    if x<0 or x>100:
        print("Wrong input")
    return x

def zero(x):
    if x==0:
        print(1)

def fact(x):
    for a in range(1,x+1):
        f=1
        for b in range(1,a+1):
            f=f*b
        print(f)

x=inputnum()
zero(x)
fact(x)


        