M = int(input("請輸入今月月份："))
D = int(input("請輸入今日日期："))
S = (M*2+D)%3

if S == 0:
  print('普通')
elif S == 1:
  print("吉")
else:
  print("大吉")