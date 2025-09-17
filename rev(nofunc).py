li=[]
n=int(input("Enter the range"))

for i in range(0,n):
  a=int(input("Enter the number\n"))
  li.append(a)
print(li)
print(li[::-1])