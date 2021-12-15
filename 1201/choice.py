def odd():  print("奇数")
def even(): print("偶数")
def choice_func(number):
    return odd if int(number)%2 else even
while (num:=input("数字を入力してください。（0：終了）"))!="0":
    choice_func(num)() if num.isdecimal() else print("入力が正しくありません") 