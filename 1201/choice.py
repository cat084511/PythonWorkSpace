def odd():
    print("奇数")
def even():
    print("偶数")
def choice_func(number):
    return odd if int(number)%2 else even
# main
while True:
    num = input("数字を入力してください。（0：終了）")
    if num=="0":break
    choice_func(num)()