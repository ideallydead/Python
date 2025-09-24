st=input("Enter the string\n").lower()
if st==st[::-1]:
  print("It is a palindrome")
else:
  print("Not a palindrome")