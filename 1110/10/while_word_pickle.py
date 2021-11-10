import pickle
import os
words=[]
i = "@"
if os.path.getsize("word.pkl") > 0: 
    with open("word.pkl","rb") as f:
        words = pickle.load(f)
while i!="":
    print("単語を入力して下さい : ",end="")
    i=input()
    if i == "LIST":
        print("単語リスト : ",words)
    elif i not in words:
        words.append(i)
    else:
        print("すでに登録済です")
print("これまでに覚えた単語 : ",words)
with open("word.pkl","wb") as f:
    pickle.dump(words[::-1], f)