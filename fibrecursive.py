def num_input():
    n=int(input())
    if n<1:
        print("Invalid")
        exit()
    return n

def fibo(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)

                
n=num_input()
fib=fibo(n)
print(fib)
    
                
