with open("word.txt","r") as f:
    l = f.read()
a=1
for i in l.split(",")[:-1]:
    print(f"{a:04}:{i}")
    a+=1