ans = [1,2,3,4]
A = B = C = 0                            
while A!=4:                             
    A = B = C = 0                        
    a = list(input('輸入四個數字：'))   
    for i in a:                      
        if int(a[C]) == ans[C]:    
            A += 1                       
        else:
            if int(i) in ans:        
                B += 1                   
        C += 1                          
    print('%dA%dB'%(A,B))
print('答對了！')
