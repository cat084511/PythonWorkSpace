import sys
print(f"引数：{(v:=sys.argv)}")
[print(f"--{a}--")or[print(f"{l:04}:{z.splitlines()[0]}") for l,z in enumerate(open(a,'r'),1)] for a in v[1:]]