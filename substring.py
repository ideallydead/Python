import textwrap

def count_substring(string,sub_string):
    if(len(string)>=0 or len(string)<=200):
        count=0
        for i in range(len(string)):
            sub=string[i:i+len(sub_string)]
            if(sub==sub_string):
                count=count+1
        return count
    else:
        print("Invalid")


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)