a = input('請輸入1~7個數字，中間以空白鍵隔開').split()
# a = list(map(int,a))
b = s = ""
a.sort()
for i in range(len(a)):
  b += a[i]
a.reverse()
for i in range(len(a)):
  s += a[i]
print(int(s) - int(b))


