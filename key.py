li=[]
n=int(input("Enter the range\n"))
for i in range(0,n):
  a=int(input("Enter the number\n"))
  li.append(a)
c=0
key=int(input("Enter the key\n"))
for i in range(len(li)):
  c=c+1
  if li[i]==key:
    print("Element",key,"found at",c)
