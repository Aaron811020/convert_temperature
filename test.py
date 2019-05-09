#溫度轉換

option = input("1.攝氏轉華氏 2.華氏轉攝氏")


if option == "1":
	old_degree = float(input("請輸入攝氏溫度"))
	new_degree = old_degree * 1.8 + 32
else:
	old_degree = float(input("請輸入華氏溫度"))
	new_degree = (old_degree - 32) * 5 / 9

print("溫度:", new_degree)
