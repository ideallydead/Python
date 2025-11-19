import re
s=input().strip()
l=len(s)
match1=re.match(r'if\s|if[(]|for\s|while\s|def\s',s)
if match1:
    if(re.search(r':$',s)):
        print("syntax verified successfully")
    else:
        print(f"syntax error at {l+1}th position")
elif(re.search(r'[^:]$',s)):
    print("syntax verified successfully")
else:
    print(f"syntax error at {l}th position")