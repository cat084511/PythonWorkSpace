
while 1:
    e = input()
    if e=="":
        break
    elif e.isdigit():
        print("数字")
    elif e.isalpha()
        print("アルファベット")
    elif e.isalnum():
        print("数字とアルファベット")
    else:
        print("その他")