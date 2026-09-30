# Pertemuan 05 Perulangan Python

Nama: Rohelis
NIM: 2225250064
Kelas: 3B

## Tujuan
Menggunakan for dan while untuk menyelesaikan masalah iteratif.

## Cara Menjalankan
python3 kuis/kuis2_deret_aritmetika.py

## Algoritma Kuis 2
1. Membaca input nilai suku pertama (a) dan beda (d) dalam tipe float.
2. Membaca input banyak suku (n) dalam tipe integer.
3. Melakukan validasi menggunakan perulangan `while`: jika `n <= 0`, program meminta input `n` kembali secara berulang sampai dimasukkan bilangan positif (`n > 0`).
4. Menginisialisasi variabel akumulator `total = 0` sebelum perulangan.
5. Melakukan perulangan `for` sebanyak `n` kali (indeks `i` dari `0` sampai `n - 1`).
6. Pada setiap iterasi:
   - Menghitung suku ke-`(i + 1)` dengan rumus: `suku = a + (i * d)`.
   - Menambahkan nilai `suku` ke dalam variabel `total`.
   - Menampilkan nomor suku dan nilainya.
7. Setelah perulangan selesai, menampilkan hasil akumulasi `total` dengan format dua angka di belakang koma (`:.2f`).

## Hasil Pengujian

| Input (a, d, n) | Keluaran yang Diharapkan | Keluaran Aktual | Status |
| :--- | :--- | :--- | :--- |
| `a = 2`, `d = 3`, `n = 5` | Suku: 2, 5, 8, 11, 14<br>Jumlah = 40.00 | Suku: 2, 5, 8, 11, 14<br>Jumlah = 40.00 | Berhasil |
| `a = 10`, `d = -2`, `n = 4` | Suku: 10, 8, 6, 4<br>Jumlah = 28.00 | Suku: 10, 8, 6, 4<br>Jumlah = 28.00 | Berhasil |
| `a = 1.5`, `d = 0.5`, `n = 3` | Suku: 1.5, 2.0, 2.5<br>Jumlah = 6.00 | Suku: 1.5, 2.0, 2.5<br>Jumlah = 6.00 | Berhasil |
| `n = 0` lalu `n = 5` (Validasi) | Menolak `0`, minta input ulang | Menolak `0`, minta input ulang | Berhasil |

## Refleksi Teknis

1. **Bagian mana yang menentukan jumlah iterasi?**
   - Perulangan `range(n)` pada konstruk `for i in range(n):` yang menentukan jumlah iterasi, yaitu persis sebanyak `n` kali.

2. **Mengapa total harus diinisialisasi sebelum loop?**
   - Agar variabel `total` memiliki nilai awal (`0`) untuk menampung hasil penjumlahan akumulatif. Jika tidak diinisialisasi sebelum loop, Python akan menghasilkan error (`NameError`) karena variabel belum terdefinisi saat diakses pertama kali.

3. **Apa akibatnya jika `total = 0` ditempatkan di dalam loop?**
   - Nilai `total` akan selalu tereset kembali menjadi `0` di setiap iterasi, sehingga hasil akhir `total` hanya berisi nilai dari suku terakhir saja (bukan akumulasi seluruh suku).

4. **Mengapa validasi `n` lebih sesuai menggunakan `while`?**
   - Karena kita tidak bisa memprediksi berapa kali pengguna akan memasukkan input yang salah. Perulangan `while` terus berjalan selama kondisi tidak valid (`n <= 0`) terpenuhi, dan baru berhenti setelah menerima input yang benar.

5. **Bagaimana Anda membuktikan bahwa loop berhenti tepat?**
   - Dengan memeriksa fungsi `range(n)` yang menghasilkan urutan dari `0` hingga `n - 1` (total `n` elemen), serta memverifikasi bahwa keluaran jumlah baris/suku yang dicetak sesuai dengan nilai `n` yang dimasukkan.