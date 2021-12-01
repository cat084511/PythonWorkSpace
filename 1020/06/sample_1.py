while 1:
  print("整数を入力して下さい（終了-> 0) : ",end="")
  x=int(input())
  if x==0:break
  print("偶奇"[x%2::2],"数 です") 
