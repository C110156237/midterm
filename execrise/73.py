a = int(input("請輸入時間1(時)"))
b = int(input("請輸入時間1(分)"))
c = int(input("請輸入時間1(秒)"))
aa = int(input("請輸入時間2(秒)")) 
a1 = a
b1 = b
while True:
  b1 *= 60
  a1 *= 60*60
  sec = a1 + b1 + c
  print("%d時:%d分:%d秒轉換後為%d秒"%(a,b,c,sec))
  min = aa / 60
  sec1 = aa % 60
  hour = min / 60
  min %= 60
  print("%d秒轉換後為%d時:%d分:%d秒"%(aa,hour,min,sec1))
  break


  
