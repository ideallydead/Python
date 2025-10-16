def binary(i):
    string=""
    while(i):
        rem=i%2
        i=(i//2)
        string=string+str(rem)
    return string[::-1]



def decimal(i):
    string=""
    while(i):
        rem=i%10
        i=(i//10)
        string=string+str(rem)
    return string[::-1]
        

def octal(i):
    string=""
    while(i):
        rem=i%8
        i=(i//8)
        string=string+str(rem)
    return string[::-1]


def hexad(i):
    string=""
    while(i):
        rem=i%16
        if rem==10:
            rem="A"
        elif rem==11:
            rem="B"
        elif rem==12:
            rem="C"
        elif rem==13:
            rem="D"
        elif rem==14:
            rem="E"
        elif rem==15:
            rem="F"       
        i=(i//16)
        string=string+str(rem)
    return string[::-1]


def align(num,width):
    if(len(num)>=width):
        return num
    right=width-len(num)
    spaces=" "*right+num
    return spaces

    

def print_formatted(n):
    if(0<=n<=99):
        for i in range(1,n+1):
            width=len(binary(n))
            bin=align(binary(i),width)
            dec=align(decimal(i),width)
            oct=align(octal(i),width)
            hexa=align(hexad(i),width)
            print(hexa,dec,oct,bin)






n=int(input())
print_formatted(n)