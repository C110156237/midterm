a = int(input("please enter a numberA."))
b = int(input("please enter a numberB."))
c = int(input("please enter a numberC."))
x1 = (-b + ((b ** 2 - 4*a*c) ** 0.5)) / a*2 
x2 = (-b - ((b ** 2 - 4*a*c) ** 0.5)) / a*2 

D = (b ** 2) - (4 * a * c)
if D > 0:
  print(x1, x2)
elif D == 0:
  print(x1)
else:
  print("無解")
