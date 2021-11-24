i = 1
val = 1
l = []
flg = 0
while 1:
    print("商品名を入力してください（0:終了）：",end="")
    i=input()
    if i=="0":
        break
    print("金額を入力してください（0:終了）：",end="")
    val=input()
    if val=="0":
        break
    elif int(val)<100:
        flg=1
    l.append([i,val])
print("最低価格を下回った商品があります。" if flg else "全てのデータは問題ありませんでした" )
for k,v in l:
    print(f"{k} : {v}")