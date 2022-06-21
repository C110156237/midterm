a = int(input('欲購買幾組'))

i = 0
while a > 0:
  o = input('請依序輸入全票及半票張數(中間以空白鍵隔開)').split()
  o = list(map(int,o))
  o[0] *= 250 
  o[1] *= 175
  total = o[0] + o[1]
  a -= 1
  print('第',i+1,'組共',total,'元')
  i += 1
 
