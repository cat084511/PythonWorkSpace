words=[]
i = "@@"
while i!="":
    print("単語を入力して下さい : ",end="")
    i=input()
    if i == "LIST":print("単語リスト : ",words)
    elif i not in words: words.append(i)
    else:print("すでに登録済です")
print("これまでに覚えた単語 : ",words[:-1])