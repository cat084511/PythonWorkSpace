import math
input_angle = float(input('角度を入力してください（度）：'))
rad = math.radians(input_angle)
print(input_angle,"度 -> ",rad,"ラジアン")
print("sin(",input_angle,") -> ",math.sin(rad))