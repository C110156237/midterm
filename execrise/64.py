c = 2
a = []
for i in range (2):
  n = int(input('輸入一個正整數:'))
  while c < n:
      if n % c == 0:
          print('不是質數')
          break
      c += 1
  if c == n:
    a.append(n)
if a[0] > a[1]:
  s = a[0] - a[1]
  if s == 2:
    print("Y")
  else:
    print("N")
else:
  s = a[1] - a[0]
  if s == 2:
    print("Y")
  else:
    print("N")