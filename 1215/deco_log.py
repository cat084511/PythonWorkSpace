import datetime
def log_file(func):
    def funcname(*args,**kwargs):
        out = f"{datetime.datetime.now()} function:{func.__name__} args:{str(args)} kwargs:{str(kwargs)}\n"
        with open("python.log","a") as f: f.write(out)
        func(*args,**kwargs)
    return funcname
# main
@log_file
def test(n):
    print(f'test->{n}')
# 呼出
test(100)
# 呼出
for i in range(5):
    test(i)