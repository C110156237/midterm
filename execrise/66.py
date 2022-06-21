stra = input("Please enter a stringA ")
strb = input("Please enter a stringB ")
c = []
for i in range(len(stra)):
  if stra[i] in strb:
    c += stra[i]
    j = "".join(dict.fromkeys(c))
    c.sort()    
    print(c)
  if stra[i] not in strb:
    print("NO")


