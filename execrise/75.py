i = 0
while True:
  a = input("代辦事項:(輸入end結束)")
  i += 1
  print("%d. %s"%(i,a))
  if a == "end":
    break