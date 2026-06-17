dau = input("dien dau (+ - * /) : ")
a = float(input("nhap so dau tien : "))
b = float(input("nhap so thu hai : "))
if dau == "+" :
    print(round((a+b),2))
elif dau == "-" :
    print(round((a-b),2))
elif dau == "*" :
    print(round((a*b),2))
elif dau == "/" :
    print(round((a/b),2))
else :
    print(f"{dau} la toan tu khong hop le")