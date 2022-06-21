a, b = input('輸入月租費形式及通話時間(以逗號隔開)').split(',')
a1 = int(a)
b1 = float(b)

if (a1 == 186 ):
  b1 *= 0.09
  bill = round(b1)
  bill //= a1
  if (bill <= 1):
    b1 *= 0.9
    bill = round(b1)
    print(bill)
  else:
    b1 *= 0.8
    print(round(b1))

elif (a1 == 386 ):
  b1 *= 0.08
  bill = round(b1)
  bill //= a1
  if (bill <= 1):
    b1 *= 0.8
    bill = round(b1)
    print(bill)
  else:
    b1 *= 0.7
    print(round(b1))

elif (a1 == 586 ):
  b1 *= 0.07
  bill = round(b1)
  bill //= a1
  if (bill <= 1):
    b1 *= 0.7
    bill = round(b1)
    print(bill)
  else:
    b1 *= 0.6
    print(round(b1))

elif (a1 == 986 ):
  b1 *= 0.06
  bill = round(b1)
  bill //= a1
  if (bill <= 1):
    b1 *= 0.6
    bill = round(b1)
    print(bill)
  else:
    b1 *= 0.5
    print(round(b1))


  

