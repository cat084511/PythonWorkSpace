with open("word.txt","r") as f:
    l = f.read()
words = l.split(",")
i = "@"
while i!="":
    print("単語を入力して下さい : ",end="")
    i=input()
    if i == "LIST":
        print("単語リスト : ",words)
    elif i not in words:
        words.append(i)
    else:print("すでに登録済です")
print("これまでに覚えた単語 : ",words)
with open("word.txt","w") as f:
    for a in words:f.write(a+",")