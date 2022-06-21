a = int(input('欲檢測資料量'))

while a > 0:
  o = input('請依序輸入父親、母親及你的血型(大寫且中間以空白鍵隔開)').split()
  if o[0] =='O' or o[1] =='O':
    if o[0] =='O' or o[1] =='O':
      if o[2] =='O':
        print("POSSIBLE")
      elif o[2] =='A' or o[2] =='B' or o[2] =='AB':
        print("IMPOSSIBLE")
    elif o[0] =='B' or o[1] =='B':
      if o[2] =='O':
        print("POSSIBLE")
      elif o[2] =='A' or o[2] =='AB':
        print("IMPOSSIBLE")
    elif o[0] =='A' or o[1] =='A':
      if o[2] =='O' or [2] =='A':
        print("POSSIBLE")
      elif o[2] =='B' or o[2] =='AB':
        print("IMPOSSIBLE")
    elif o[0] =='B' or o[1] =='B':
      if o[2] =='O' or [2] =='B':
        print("POSSIBLE")
      elif o[2] =='A' or o[2] =='AB':
        print("IMPOSSIBLE")
    elif o[0] =='AB' or o[1] =='AB':
      if o[2] =='B' or [2] =='A':
        print("POSSIBLE")
      elif o[2] =='O' or o[2] =='AB':
        print("IMPOSSIBLE")
  elif o[0] =='A' or o[1] =='A':
    if o[0] =='A' or o[1] =='A':
      if o[2] =='O' or o[2] =='A':
        print("POSSIBLE")
      elif o[2] =='B' or o[2] =='AB':
        print("IMPOSSIBLE")
    elif o[0] =='B' or o[1] =='B':
      if o[2] =='O' or o[2] =='A'or o[2] =='B' or o[2] =='AB':
        print("POSSIBLE")
    elif o[0] =='AB' or o[1] =='AB':
      if o[2] =='B' or [2] =='A' or [2] =='AB':
        print("POSSIBLE")
      elif o[2] =='O':
        print("IMPOSSIBLE")
  elif o[0] =='B' or o[1] =='B':
    if o[0] =='B' or o[1] =='B':
      if o[2] =='O' or o[2] =='B':
        print("POSSIBLE")
      elif o[2] =='A' or o[2] =='AB':
        print("IMPOSSIBLE")
    elif o[0] =='AB' or o[1] =='AB':
      if o[2] =='A' or o[2] =='B' or o[2] =='AB' :
        print("POSSIBLE")
      elif o[2] =='O':
        print("IMPOSSIBLE")
  elif o[0] =='AB' or o[1] =='AB':
    if o[0] =='AB' or o[1] =='AB':
      if o[2] =='A' or o[2] =='B' or o[2] =='AB':
        print("POSSIBLE")
      elif o[2] =='O':
        print("IMPOSSIBLE")
  a -= 1