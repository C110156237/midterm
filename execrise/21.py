a = [['學號','姓名','系別'],['123','Tom','DTGD'],['456','Cat','CSIE'],['789','Nana','ASIE'],['321','Lim','DBA'],['654','Won','FDD']]

i = input('欲查詢學號:')
if i == '123':
    a1 = a[1]
    str1 = " ".join(a1)
    print('學生資料為:',str1)
elif i == '456':
    a2 = a[2]
    str2 = " ".join(a2)
    print('學生資料為:',str2)
elif i == '789':
    a3 = a[3]
    str3 = " ".join(a3)
    print('學生資料為:',str3)
elif i == '321':
    a4 = a[4]
    str4 = " ".join(a4)
    print('學生資料為:',str4)
elif i == '654':
    a5 = a[5]
    str5 = " ".join(a5)
    print('學生資料為:',str5)
else:
    print('查無資料')


