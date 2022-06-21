subjects = ["國文","英文","微積分","體育","程式設計"]
score = [] 
max = 5
while len(score) < max:
    s = input("請依序輸入國文,英文,微積分,體育,程式設計成績")
    score.append(s)
    print (score)
for i in range(max) :
    dict = {subjects:score}
    dict[subjects]
print(dict[subjects[0]])
dict.sort()
a = score[3]
print("最高分為科目為",dict[4],':',score[4])


