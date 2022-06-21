g = input('請輸入一整數序列').split()
o = list(map(int,g))
print(o)
for i in range(len(g)):
  a = g.count(g[i])
  if a > len(g)/2:
    print(g[i])

