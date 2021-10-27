import re
import unicodedata

def is_japanese(string):
    for ch in string:
        name = unicodedata.name(ch) 
        if "CJK UNIFIED" in name \
        or "HIRAGANA" in name \
        or "KATAKANA" in name \
            return True
    return False

while 1:
    e = input()
    if e=="":
        break
    elif is_japanese(e):
        print("jap")
    elif e.isdigit():
        print("数字")
    elif re.match('^[a-zA-Z]+$',e):
    #e.isalpha()は日本語もTrueになる
        print("アルファベット")
    elif e.isalnum():
        print("数字とアルファベット")
    else:
        print("その他")
