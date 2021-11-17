def str2int(a):
    return int(a) if str(a).isdigit() else 0

def list2int(s):
    if(type(s) is list):
        for i in range(0,len(s)):
            s[i] = str2int(s[i])
        return(s)
    elif(type(s) is str):
        return(str2int(s))

print(list2int(['5','ab','100',10,1]))
print(list2int('100'))
print(list2int('xyz'))