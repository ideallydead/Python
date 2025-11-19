import re
pan=input("Enter the Pan number:")
x=re.findall(r"^[A-Z]{3}[PCHFATBLJG][A-Z]\d{4}[A-Z]$",pan)
if x:
    print("Valid PAN number")
else:
    print("Invalid PAN number!")
