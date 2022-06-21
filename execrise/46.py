a = int(input('金牌'))
b = int(input('銀牌'))
c = int(input('銅牌'))
d = int(input('優牌'))

e = {'金牌':a,'銀牌':b,'銅牌':c,'優牌':d}

for o, num in e.items():
  print( o, '共有', num,'面')


