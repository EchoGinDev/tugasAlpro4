def cek_digit_belakang(a, b, c):
    if a == b or a == c or b == c:
        return(True)
    else:
        return(False)

a = input("nilai_pertama = ")
b = input("nilai_kedua = ")
c = input("nilai_ketiga = ")

print(cek_digit_belakang(a[-1], b[-1], c[-1]))