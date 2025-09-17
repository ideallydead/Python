
li=[]
n=int(input("Enter the range\n"))
for i in range(0,n):
  a=int(input("Enter the number\n"))
  li.append(a)
l=[]
for i in li:
  if i not in l:
    l.append(i)
print(l)

