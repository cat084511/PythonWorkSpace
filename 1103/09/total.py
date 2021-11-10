with open("test.csv","r",encoding="utf-8") as f:
    l = f.read().splitlines()
for i in l[1:]:
    a = i.split(",")
    print(f"{a[0]} {sum([int(b) for b in a[1:]])}")