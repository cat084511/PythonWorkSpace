a="";b=["+","-","*","/"]
while (i:=input("calc :"))!="=":
    if(i.isdecimal() or (i in b and len(a)!=0 and a[len(a)-1]not in b)): a+=i
    else: print("入力が正しくありません。")
print(f"入力した計算式：{a}\n計算結果：{eval(a)}")