a = int(input("請輸入第1個數字"))
b = int(input("請輸入第2個數字"))
c = int(input("請輸入第3個數字"))
d = int(input("請輸入第4個數字"))
e = int(input("請輸入第5個數字"))
f = int(input("請輸入第6個數字"))
g = int(input("請輸入第7個數字"))
h = int(input("請輸入第8個數字"))
i = int(input("請輸入第9個數字"))
j = int(input("請輸入第10個數字"))

list = [a,b,c,d,e,f,g,h,i,j]
list.sort()
print('最大的三個數為:',list[9],list[8],list[7])
list.reverse()
print('最小的三個數為:',list[9],list[8],list[7])


