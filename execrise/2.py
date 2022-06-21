bill = int(input('請輸入一個度數(正整數)'))

if (bill <=120):
    sem = bill*2.10
    non = bill*2.10
elif (121<=bill<=330):
    sem = bill*3.02
    non = bill*2.68
elif (331<=bill<=500):
    sem = bill*4.39
    non = bill*3.61
elif (501<=bill<=700):
    sem = bill*4.97
    non = bill*4.01
elif (bill>=701):
    sem = bill*5.63
    non = bill*4.50
print('Summer months:', "{:.2f}".format(sem))
print('Non-Summer months:', "{:.2f}".format(non))

