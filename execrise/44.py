a = int(input("請輸入有幾個班級"))
b = []
while a > 0:
  s = int(input("請依序輸入每班多少學生"))
  b.append(s)
  b.sort()
  b.reverse()
  a -= 1
print("共需要買%d台電腦"%int(b[0]))
