a=int(input("Enter the number\n"))
f=0
for i in range(2,a):
  if a%i==0:
    f=1
    break
if f==1:
  print("Not a prime number")
else:
  print("It is a prime number")