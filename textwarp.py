import textwarp 
def wrap(string, max_width):
    if(0<len(string)<1000):
        if(0<max_width<len(string)):
            result=""
            for i in range(0,len(string),max_width):
                result=result+string[i:i+max_width]+"\n"
            return result
        

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)