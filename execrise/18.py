a = input('請輸入五張牌(包含A,J,Q,K且用空白鍵隔開)').split(' ')

for i in range(5):
  if a[i] == 'A':
    a[i] = 1
  elif a[i] == 'J':
    a[i] = 11
  elif a[i] == 'Q':
    a[i] = 12
  elif a[i] == 'K':
    a[i] = 13 
a = list(map(int,a))

total = 0
for i in range(5):
  total += a[i]
print('總值為:', total)
