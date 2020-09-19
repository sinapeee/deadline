# viết chương trình in ra chữ xin chàochào
print("Xin chào...!")

# tính tổng bình phương 2 số nguyên nhập từ bàn phím
print("nhập số thứ nhất:",end="")
a = input()
print("nhập số thứ haihai:",end="")
b = input()
a= int(a)
b= int(b)
tong = pow(a,2) + pow(b,2)
print(int(tong))

# tiền lương (lương chính=((tiền lương cơ bản + phụ cấp)/22)) * số ngày đi làm))
print("tiền lương cơ bản: ",end="")
a = int(input())
print("Phụ cấp: ",end="")
b = int(input())
print("số ngày đi làm: ",end="")
c = int(input())
tong = ((a+b)/22)*c
print(int(tong))

# tính chu vi và dien tich hinh tron
PI=3.14
print("nhap chieu dai ban kinh r:",end="")
a=int(input())
chuvi = a*2*PI
print("ket qua chu vi="+str (a*2*PI))
dientich = a*a*PI
print("ket qua dien tich+"+str (a*a*PI))

# in ra số hàng chục và hàng đơn vịvị
print("nhap so co hai chu so:",end="")
a=int(input())
if a > 10:
    chuc = a // 10
    donvi = a % 10
print("hang chuc la: "+str (chuc))
print("hang don vi la: "+str(donvi))

# nhap thong tin va kiem tra kieu du lieu
print("Nhap Ten:",end="")
ten=input()
print(type(ten))
print("Nhap Ma So Sinh Vien: ",end="")
mssv=int (input())
print(type(mssv))
print("Nhap Tuoi: ",end="")
tuoi=int (input())
print(type(tuoi))

# ki tu thu nhat trong chuoichuoi
print("Nhap ten:",end="")
ten=input()
len(ten)
print("ky tu thu nhat trong chuoi la: "+format(ten[1]))

# ngich dao 2 soso
print("nhap so can nghich dao: ",end="")
so=int(input())
print(str(so)[::-1])