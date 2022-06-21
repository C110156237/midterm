a = input('甲方數字:').split()
b = input('乙方數字:').split()
a = list(map(int,a))
b = list(map(int,b))
c = ''
for i in range(len(a)):
  if a[i] == b[i]:
    c += "和"
  elif a[i] == 5 and b[i] == 1:
    c += "輸"
  elif a[i] == 1 and b[i] == 5:
    c += "贏"
  elif a[i] > b[i]:
    c += "贏"
  elif a[i] < b[i]:
    c += "輸"
print(c)




