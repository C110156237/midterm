s = {"Dog":"狗","Cat":"貓","Bear":"熊","Snake":"蛇"}
a = input("輸入欲查詢單字:")
b = s.get(a)
if b == None:
  print("請輸入一英文單字")
else:
  print("您所查詢的%s中文為%s"%(a,s[a]))
