avg = [0,0,0,0]
with open("test.csv","r",encoding="utf-8") as f:
    l = f.read().splitlines()
print(l[0].split(",")[1:])
for i in l[1:]:
    for j in range(1,5):
        avg[j-1]+=int(i.split(",")[j])/4
print(avg)