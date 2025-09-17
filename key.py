li=[]
n=int(input("Enter the range\n"))
for i in range(0,n):
  a=int(input("Enter the number\n"))
  li.append(a)
key=int(input("Enter the key\n"))
if key in li:
  print("Present")
else:
  print("Not present")