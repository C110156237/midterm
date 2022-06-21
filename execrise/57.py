a, b = input('請主餐及升級的套餐:(若不升級則填否，且中間以空白鍵隔開)').split()
c = input('是否升級成大杯飲料(y或n)')
d = input('是否換成大薯(y或n)')
tol = 0
if a == '1':
  tol += 72
  if b == 'A':
    tol += 55
  if b == 'B':
    tol += 68
  if c == 'y':
    tol += 7
  if c == 'n' :
    tol *= 1
  if d == 'y':
      tol += 13
  if d == 'n':
      tol *= 1
elif a == '2':
  tol += 62
  if b == 'A':
    tol += 55
  if b == 'B':
    tol += 68
  if c == 'y':
    tol += 7
  if c == 'n' :
    tol *= 1
  if d == 'y':
      tol += 13
  if d == 'n':
      tol *= 1
elif a == '3':
  tol += 82
  if b == 'A':
    tol += 55
  if b == 'B':
    tol += 68
  if c == 'y':
    tol += 7
  if c == 'n' :
    tol *= 1
  if d == 'y':
      tol += 13
  if d == 'n':
      tol *= 1
elif a == '4':
  tol += 44
  if b == 'A':
    tol += 55
  if b == 'B':
    tol += 68
  if c == 'y':
    tol += 7
  if c == 'n' :
    tol *= 1
  if d == 'y':
      tol += 13
  if d == 'n':
      tol *= 1
elif a == '5':
  tol += 60
  if b == 'A':
    tol += 55
  if b == 'B':
    tol += 68
  if c == 'y':
    tol += 7
  if c == 'n' :
    tol *= 1
  if d == 'y':
      tol += 13
  if d == 'n':
      tol *= 1
  print('共%d元' %(tol))


      


