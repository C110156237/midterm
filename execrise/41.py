t = int(input("共搭乘幾次電梯"))
tol = s = 0
f1 = int(input("你去了?樓"))
for i in range(t-1):
  f = int(input("你去了?樓"))
  if s > f:
    e = s - f
    tol += e * 20
  elif f > s:
    d = f - s
    tol += d * 10
  else:
    tol = tol
s = f
print(tol)

  