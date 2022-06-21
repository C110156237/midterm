# xxx
n, m = input('請輸入N*M(中間以空白鍵隔開)').split(' ')
if (n == '0' and m =='0'):
  print('結束迴圈')
  exit
else:
  first = input('請輸入第一行數字(中間以空白鍵隔開)').split(' ')
  second = input('請輸入第二行數字(中間以空白鍵隔開)').split(' ')

i = 0
j = 0
for i,j in range(len(n)):
  firsta = first[i,j]
print(firsta)

