a = input("請輸入一個字串(請以空白鍵隔開)").split()
b = input("請輸入欲尋找字串")

for i in range(1):
  if b in a:
    print("YES")
  else:
    print("NO")
