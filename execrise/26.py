while True:
  a = input('請輸入一段字串(輸入end結束)')
  if a != 'end':
    b = input('檢測的字為:')
    c = set(a)
    d = a.count(b)
    if b in c:
      print("字元%s出現次數為:%d"%(b, d))
    else:
      print("%s不再在%s中"%(b, a))
  elif a == 'end':
      print('檢測結束')
      break
  
  
    
