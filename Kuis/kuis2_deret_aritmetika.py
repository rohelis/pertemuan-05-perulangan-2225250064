# kuis/kuis2_deret_aritmetika.py

print("Deret Aritmetika")
a = float(input("Suku pertama a: "))
d = float(input("Beda d: "))
n = int(input("Banyak suku n: "))

# Validasi input n (n harus berupa integer positif > 0)
while n <= 0:
    n = int(input("Banyak suku n: "))

total = 0

# Iterasi untuk menghitung setiap suku dan akumulasi total
for i in range(n):
    suku = a + i * d
    total += suku
    print(f"Suku ke-{i + 1}: {suku}")

# Menampilkan hasil jumlah total dengan dua angka di belakang koma
print(f"Jumlah = {total:.2f}")