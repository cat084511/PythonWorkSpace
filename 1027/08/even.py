print("偶数一覧")
print("=>",end="")
[print(i,end=",") for i in range(2,99)[::2]]

print("\n\n偶数一覧=>",end="")
a = [i for i in range(2,99)[::2]]
print(a)