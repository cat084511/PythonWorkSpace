import time
def run_time(func):
    def funcname(*args,**kwargs):
        st = time.time()
        func(*args,**kwargs)
        print(f"実行関数:{str(func).split()[1]} 実行時間:{time.time()-st}")
    return funcname

# main
@run_time
def test(n):
    for i in range(n):
        time.sleep(i)
test(3)
test(5)