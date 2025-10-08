li=[]
n=int(input("Enter the range:\n"))

for i in range(0,n):
  a=int(input("Enter the number\n"))
  li.append(a)
done=[]
c=0
for el in li:
  if el not in done:
    c=li.count(el)
    print(el, "appears in the list", c, "times")
    done.append(el) 
   