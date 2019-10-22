print("Masukkan uang Jessica : ", end = '')
uangJeje = int(input())
hargaIP11 = int(20)
hargaSam10 = int(8)
hargaNok3310 = int(6)
tipeHP = str()
if (uangJeje >= hargaIP11):
	if (uangJeje >= hargaIP11+hargaSam10):
		kembalian = uangJeje-(hargaIP11+hargaSam10)
		tipeHP = "iPhone 11 dan Samsung S10"
	else:
		kembalian = uangJeje-hargaIP11
		tipeHP = "iPhone 11"
elif (uangJeje >= hargaSam10):
	kembalian = uangJeje-hargaSam10
	tipeHP = "Samsung S10"
elif (uangJeje >= hargaNok3310):
	kembalian = uangJeje-hargaNok3310
	tipeHP = "Nokia 3310"
else:
	kembalian = uangJeje
	tipeHP = "Jessica tidak membeli HP apapun"

print("kembalian yang didapat Jessica : ", kembalian, "juta\n", "HP yang dibeli Jessica : ", tipeHP)
