a = list(input("請輸入自傳(至少十個字)"))
j = "".join(dict.fromkeys(a))
print(j)
b = ''
j = 0
l = 0
for i in range(len(a)):
  if a[j] == a[l]:
    b += a[j]


