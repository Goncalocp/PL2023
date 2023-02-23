
def toNumber(list):
     
    s = [str(i) for i in list]
    res = int("".join(s))
     
    return(res)
 
def sum(list):
    count = 0
    for i in list:
        count += i
    
    return count

def prog(string):
    i = 0
    j = 0
    flag = 0

    values = []
    length = len(string)-1

    while i <= length:
        if string[i].casefold() == 'o':
            if (i<=length-2):
                if((string[i+1].casefold() == 'f' and string[i+2].casefold() == 'f')):
                    flag = 1
                elif(string[i+1].casefold() == 'n'):
                    flag = 2
        if(flag == 0 or flag == 2): #flag=2 -> on; flag=1 -> off
            if string[i].isdigit():
                list = []
                j = i
                while(j <= length and string[j].isdigit()):
                    list.append(int(string[j]))
                    j += 1
                values.append(toNumber(list))
                list = []
                if(j > length): break
                i = j-1
            elif string[i] == '=':
                print("Soma:",sum(values))
        i += 1

def main():
    text = input("")
    print("\n")
    prog(text)
    print("\n")

if __name__ == "__main__":
    main()
