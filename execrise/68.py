ans = list(input("輸入第一組數字(2~6個數字):"))
A = B = 0
while A!=4:                             
  A = B = 0                        
  a = list(input('輸入第二組數字(2~6個數字)：'))
  i = 0
  for j in a: 
    if int(a[i]) == int(ans[i]):    
      A += 1                       
    else:
        if j in ans:        
          B += 1   
    i += 1                                       
  print('%dA%dB'%(A,B))
print('答對了！')
