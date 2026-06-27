#total = principle * pow((1 + rate / 100), time)
tien = 0
tile = 0
kihan = 0
while True :
    tien = float(input("nhap so tien ban co :"))
    if tien <= 0 :
     print("ban qua ngheo")
    else:
        break

while True :
    tile = float(input("nhap so phan tram ban muon :"))
    if tile <= 0:
      print("tile khong hop le")
    else :
        break

while True:
    kihan = int(input("may nam :"))
    if kihan <= 0:
        print("ki han khong hop le")
    else :
      break

tong = round(tien * pow((1 + tile / 100), kihan),2)
print(f"ban co {tong} sau {kihan} nam")
