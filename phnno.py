import re
mob=input("Enter the mobile number:")
x=re.findall(r"^[1-9]\d{9}$",mob)
if x:
    print("Valid Mobile number")
else:
    print("Invalid Mobile number!")

