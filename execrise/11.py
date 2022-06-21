M = int(input("請輸入月份"))
D = int(input("請輸入日期"))

def get_constellation(month, date):
    dates = (21, 20, 21, 21, 22, 22, 23, 24, 24, 24, 23, 22)
    signs = ("摩羯座", "水瓶座", "雙魚座", "牡羊座", "金牛座", "雙子座", "巨蟹座", "獅子座", "處女座", "天秤座", "天蝎座", "射手座", "魔羯座")
    if date < dates[month-1]:
        return signs[month-1]
    else:
        return signs[month]

print ('星座為:',(get_constellation(M,D)))