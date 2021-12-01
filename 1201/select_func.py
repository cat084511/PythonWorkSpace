# 関数を辞書で渡し、実行する
def func1():
    print("Hello")

def func2():
    print("Goodbye")
    
# main
run_list = {'a': func1, 'b': func2}
while 1:
    print("a=>Hello,b=>Goodbye")
    a = input("どちらを実行しますか？:")
    if a in run_list:run_list[a]()