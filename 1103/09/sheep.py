import time
print("何匹数えますか？",end="")
i = int(input())
for s in range(1,i+1):
    time.sleep(1+0.5*s)
    print("羊が"+str(s)+"匹")
    if s>100:break