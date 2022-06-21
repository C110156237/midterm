a = "春 眠 不 覺 曉 ， ， 處 處 聞 啼 鳥 。 夜 來 風 雨 聲 ， 花 落 知 多 少 。"
lista = a.split(" ")
b = "紅 豆 生 南 國 ， ， 春 來 發 幾 枝 ？ 願 君 多 採 摘 ， 此 物 最 相 思 。"
listb = b.split(" ")
c = []
for i in range(len(lista)):
    if lista[i] in listb:
      c += lista[i]
      j = "".join(dict.fromkeys(c))
n = c.count("。")
m = c.count("，")
while n > 0:
  c.remove("。")
  n -= 1
while m > 0:
  c.remove("，")
  m -= 1
print(c)