# Def menggunakan lambda
cek_angka = lambda x, y, z: True if (x!=y!=z and (z + y == z or y+z == x or z+y == y)) else False

a = 15
b = 12

print("test_case: ")
print(f"(1, 2, 3){cek_angka(1,2,3)}")
print(f"(1, 2, 3){cek_angka(1,3,3)}")
print(f"(1, 2, 3){cek_angka(3,2,3)}")
print(f"(1, 2, 3){cek_angka(3,3,2)}")

print("Hasil yang benar")
print(True)
print(False)
print(False)
print(False)