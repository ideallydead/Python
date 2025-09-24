while(True):
  print("---\n\nLogical operations---\n\n")
  
  print("1.AND operation\n")
  print("2.NOT operation\n")
  print("3.OR operation\n")
  print("4.XOR operation\n")
  print("5.Exit\n")
  ch=int(input("Enter your choice\n"))
  if ch==1:
    a=int(input("Enter the first number\n"))
    b=int(input("Enter the second number\n"))
    c=bool(a and b)
    print(c)
  elif ch==2:
    a=int(input("Enter the number\n"))
    c=not a
    print(c)
  elif ch==3:
    a=int(input("Enter the first number\n"))
    b=int(input("Enter the second number\n"))
    c=bool(a or b)
    print(c)
  elif(ch==4):
    a=int(input("Enter the first number\n"))
    b=int(input("Enter the second number\n"))
    c=bool(a^b)
    print(c)
  elif ch==5:
    break
  else:
    print("Invalid choice")

             

