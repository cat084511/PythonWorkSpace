fruits = ['バナナ','リンゴ','オレンジ']
while True:
    print("果物をカタカナで入力してください：",end="")
    x = input()
    if x in fruits:
        print(x,"は、知っています！")
    elif x=="":
        break
    else:
        print(x,"は、知りませんでした。覚えておきます。")
        fruits+=[x]
print('知っている果物')
print(fruits)