s=input("Input the sentence:\n").lower().replace(" ","")
print(s)
if s==s[::-1]:
  print("It is a palindrome")
else:
  print("Not a palindrome")