a = int(input("請輸入一整數"))

while True:
  for i in range(1, a, 2):
    print(i)
  for i in range(1, a, 2):
    print(i, end=' ')
  for i in range(a, 0, -2):
    print(i)
  break
