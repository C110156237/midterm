X = int(input('請輸入X軸座標'))
Y = int(input('請輸入Y軸座標'))
dis = (X**2) + (Y**2)
if (X != 0 and Y != 0):
    if (X > 0 and Y > 0):
        print('該點位於第一象限，距離原點距離為根號',dis)
    elif (X < 0 and Y > 0):
        print('該點位於第二象限，距離原點距離為根號',dis)
    elif (X < 0 and Y < 0):
        print('該點位於第三象限，距離原點距離為根號',dis)
    elif (X > 0 and Y < 0):
        print('該點位於第四象限，距離原點距離為根號',dis)
elif (X == 0 or Y == 0):
    if (X == 0 and Y > 0):
        print('該點位於上半平面Y軸上，距離原點距離為根號',dis)
    elif (X == 0 and Y < 0):
        print('該點位於下半平面Y軸上，距離原點距離為根號',dis)
    elif (X > 0 and Y == 0):
        print('該點位於右半平面X軸上，距離原點距離為根號',dis)
    elif (X < 0 and Y == 0):
        print('該點位於左半平面X軸上，距離原點距離為根號',dis)
else:
    print('該點在原點')