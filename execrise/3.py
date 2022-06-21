year = int(input('請輸入西元年。'))
dict = {'鼠':'rat',
        '牛':'ox',
        '虎':'tiger', # 6
        '兔':'rabbit',
        '龍':'dragon',
        '蛇':'snake',
        '馬':'horse',
        '羊':'sheep', # 11
        '猴':'monkey',
        '雞':'rooster',
        '狗':'dog',
        '豬':'pig'}

if year%12 == 1:
        print(dict['雞'])
elif year%12 == 2:
        print(dict['狗'])
elif year%12 == 3:
        print(dict['豬'])
elif year%12 == 4:
        print(dict['鼠'])
elif year%12 == 5:
        print(dict['牛'])
elif year%12 == 6:
        print(dict['虎'])
elif year%12 == 7:
        print(dict['兔'])
elif year%12 == 8:
        print(dict['龍'])
elif year%12 == 9:
        print(dict['蛇'])
elif year%12 == 10:
        print(dict['馬'])
elif year%12 == 11:
        print(dict['羊'])
elif year%12 == 0:
        print(dict['猴'])
