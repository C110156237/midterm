a = str(input('請輸入一個整數'))
b = input('請輸入一串數字(中間以空格隔開)').split(' ')
b1 = len(b)

i = 0
zero = 0
if (i == 0):
  for i in range(0, b1):
    if (a == b[i]):
      zero += 1
  print('欲尋找數字:',a,'，共出現',zero,'次')
elif (zero == 0):
    print('找無此數字(數字剛好都出現一次)')
 
  
 
