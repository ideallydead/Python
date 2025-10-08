def num_input():
    x=int(input())
    if x<0 or x>150:
        print("Invalid number")
    return x
    
def fact(x):
    if x==1:
        return 1
    else:
        return x*fact(x-1)

    
def print_fact(x):
    for i in range(1,x+1):
        a=fact(i)
        print(a)

        
def five(p):
    if p==0:
        print(0)
        print(1)
    while(p):
        print(p)
        p-=1
x=num_input()
p=x
five(p)
print_fact(x)
    

    
    