a = input("輸入一句子:").split()
r = []
d = 1
for i in range(len(a)//2):
    r = a[i]
    a[i] = a[i-d]
    a[i-d] = r
    d += 2
print(a)


