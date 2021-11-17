def str2int(a):
    return int(a) if str(a).isdigit() else 0
print(str2int('a'))
print(str2int('10'))
print(str2int(100))