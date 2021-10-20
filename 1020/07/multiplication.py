multiplication = [i*j for i in range(1, 3) for j in range(1, 10)]
print(multiplication)
#使わないやつ
multiplication2=[]
for i in range(1,3):
    for j in range(1,10):
        multiplication2.append(i*j)
print(multiplication2)