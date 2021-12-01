# 関数を辞書で渡し、実行する
def func1():
    print("Hello")

def func2():
    print("Goodbye")
    
# main
run_list = {'a': func1, 'b': func2}

while a:=input("a=>Hello,b=>Goodbye\nどちらを実行しますか？:"):
    run_list[a]() if a in run_list else print("どちらかを入力して下さい")