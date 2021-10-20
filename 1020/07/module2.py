import hashlib
while 1:
    print("変換する文字")
    key = input()
    if key=="":
        break
    md5 = hashlib.md5(key.encode()).hexdigest()
    sha256 = hashlib.sha256(key.encode()).hexdigest()
    print("  md5  :",md5)
    print("sha256 :",sha256)