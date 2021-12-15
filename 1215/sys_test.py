import sys
print(f"引数：{sys.argv}")
for a in sys.argv[1:]:[print(f"{l:04}:{v.splitlines()[0]}") for l,v in enumerate(open(a,'r'),1)]