while True:
    a = input("請輸入一段小寫英文(輸入end結束迴圈)")
    if a == "end":
        print("檢測結束")
        break
    else:
        b = "a"
        f = "e"
        s = "i"
        i = "o"
        p = "u"
        c = "."
        e = a.replace(b, c)
        e = e.replace(f, c)
        e = e.replace(s, c)
        e = e.replace(i, c)
        e = e.replace(p, c)
        print ('取代後的字串為:', e)
        break