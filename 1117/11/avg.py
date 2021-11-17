def list2int(s):
    avg = [0,0,0,0]
    for j in range(1,5):
        avg[j-1]=(sum([int(i.split(",")[j])/4 for i in l[1:]]))
    return avg
with open("test.csv","r",encoding="utf-8") as f:
    l = f.read().splitlines()
print(l[0].split(",")[1:])
list2int(l[1:])
print(list2int(l))