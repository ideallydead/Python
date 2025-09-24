l=[]
n=int(input("Enter the range:\n"))

for i in range(0,n):
  a=int(input("Enter the number\n"))
  l.append(a)

point=0


for index in range(len(l)):
  c=0
  for x in range(index+1,len(l)):
    if l[index]<l[x]:
      c+=1
  print("Number of elements greater than",l[index],"are",c)

