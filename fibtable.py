def num_input():
    x=int(input())
    if x<1:
        print("Enter valid choice")
        exit()
    return x

def fib(n):
    l=[0,1]
    a=l[0]
    b=l[1]
    for i in range(n):
        l.append(l[a]+l[b])
        a=a+1
        b=b+1
    print(l[n-1])
        
        
n=num_input()
fib(n)
        