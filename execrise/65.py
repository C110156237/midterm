a = input("A的好友").split()
b = input("B的好友").split()
c = []
for i in range(len(a)):
  if a[i] in b:
    c += a[i]
    j = "".join(dict.fromkeys(c)) 
print("AB共同好友數量為",len(c))