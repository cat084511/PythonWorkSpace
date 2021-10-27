import re
while 1:
    e = input()
    if e=="":
        break
    elif e.isdigit():
        print("数字")
    elif re.match('^[a-zA-Z]+$',e):
    #e.isalpha()は日本語もTrueになる
        print("アルファベット")
    else:
        print("その他")