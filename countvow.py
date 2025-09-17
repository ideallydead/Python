st=input("Enter the string\n")
c=0
for i in st:
  if i in 'aeiouAEIOU':
    c+=1
print("The number of vowels is ",c)