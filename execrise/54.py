a = float(input("請輸入公里數:"))
a *= 1000
if a <= 250:
  print("所需車資為75元")
elif a >= 1500:
  a -= 1500
  a //= 250
  tol = 80
  for i in range(int(a)):
    tol += 5
  print("所需車資為%d"%tol)



