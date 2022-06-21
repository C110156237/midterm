a = input('請輸入一組四位數字(中間以空白鍵隔開)').split()
a = list(map(int,a))
a[0] *= 1000
a[1] *= 100
a[2] *= 10
a[3] *= 1

for i in range(4):
  a[i] += 7
  a[i] *= 0.1

r = 0
a[0] = r
r = a[2]
a[2] = a[0]

a[1] = r
r = a[3]
a[3] = a[1]

print(a[0],a[1],a[2],a[3])
