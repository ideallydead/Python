import re
n=int(input("Enter the number of strings:"))
for i in range(n):
    s=input()
    x=re.fullmatch(r"^[Aa][A-Za-z]*[Aa]$",s)
    if x:
        print(s)