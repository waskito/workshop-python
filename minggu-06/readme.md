# Error & Exceptions

> NAMA: Yanuar Galih Waskito
> NIM: 155410211

Sampai sekarang pesan kesalahan belum lebih dari yang disebutkan, tetapi jika Anda telah mencoba contohnya, Anda mungkin telah melihat beberapa. Ada (setidaknya) dua jenis kesalahan yang dapat dibedakan: syntax errors dan exceptions.

## 1. Syntax Errors

Juga dikenal sebagai kesalahan penguraian parsing, mungkin merupakan jenis keluhan paling umum yang Anda dapatkan saat Anda masih belajar Python

- Pengurai parser mengulangi baris yang menyinggung dan menampilkan sedikit 'arrow' yang menunjuk pada titik paling awal di baris di mana kesalahan terdeteksi.
- Kesalahan disebabkan oleh (atau setidaknya terdeteksi pada) token preceding panah: dalam contoh, kesalahan terdeteksi pada fungsi print(), karena titik dua (':')) hilang sebelum itu.
- Nama file dan nomor baris dicetak sehingga Anda tahu ke mana harus mencari kalau-kalau masukan berasal dari skrip.

## 2. Exceptions (Pengecualian)

Bahkan jika suatu pernyataan atau ungkapan secara sintaksis benar, itu dapat menyebabkan kesalahan ketika suatu usaha dilakukan untuk mengeksekusinya. Kesalahan yang terdeteksi selama eksekusi disebut exceptions dan tidak fatal tanpa syarat.

## 3. Handling Exceptions

Dimungkinkan untuk menulis program yang menangani exception yang dipilih. Lihatlah contoh berikut, yang meminta masukan dari pengguna sampai integer yang valid telah dimasukkan, tetapi memungkinkan pengguna untuk menghentikan program (menggunakan Control-C atau apa pun yang didukung sistem operasi); perhatikan bahwa gangguan yang dibuat pengguna ditandai dengan munculnya exception `KeyboardInterrupt`.
Pernyataan `try` berfungsi sebagai berikut:

- Pertama, `try` clause (pernyataan(-pernyataan) di antara kata kunci `try` dan `except`) dieksekusi.
- Jika tidak ada exception terjadi, `except` clause dilewati dan eksekusi pernyataan :keyword: `try` selesai.
- Jika exception terjadi selama eksekusi klausa `try`, sisa klausa dilewati. Kemudian jika jenisnya cocok dengan exception yang dinamai dengan kata kunci exception, klausa `except` dioperasikan, dan kemudian eksekusi berlanjut setelah pernyataan `try`.
- Jika terjadi exception yang tidak cocok dengan exception yang disebutkan dalam klausa kecuali, itu diteruskan ke luar pernyataan `try`; jika tidak ada penangan yang ditemukan, ini adalah unhandled exception dan eksekusi berhenti dengan pesan seperti yang ditunjukkan di atas.

Pernyataan try mungkin memiliki lebih dari satu klausa except, untuk menentukan penangan dari berbagai exception. Paling banyak satu penangan akan dieksekusi. Penangan hanya menangani exception yang terjadi pada klausa try yang sesuai, bukan pada penangan lain yang sama pernyataan try. Klausa except dapat menyebutkan beberapa exception sebagai tanda kurung tuple, misalnya:

```python
except (RuntimeError, TypeError, NameError):
  pass
```

Kelas dalam klausa `except` kompatibel dengan exception jika itu adalah kelas yang sama atau kelas basisnya (tapi bukan sebaliknya --- sebuah klausa `except` dari daftar kelas turunan tidak kompatibel dengan kelas). Misalnya, kode berikut akan mencetak B, C, D dalam urutan itu:

```python
class B(Exception):
    pass

class C(B):
    pass

class D(C):
    pass

for cls in [B, C, D]:
    try:
        raise cls()
    except D:
        print("D")
    except C:
        print("C")
    except B:
        print("B")
```

Perhatikan bahwa jika klausa `except` dibalik (dengan `except` B dahulu), itu akan dicetak B, B, B --- pencocokan pertama klausa `except` dipicu.

> Klausa `except` terakhir dapat menghilangkan nama-(nama) exception, untuk berfungsi sebagai **wildcard**.

## 4. Raising Exceptions

- Pernyataan raise memungkinkan programmer untuk memaksa exception yang ditentukan terjadi.
- Satu-satunya argumen untuk raise menunjukkan exception yang dimunculkan.
- Ini harus berupa instance exception atau kelas exception (kelas yang berasal dari Exception).
- Jika kelas exception dikirimkan, itu akan secara implisit diinstansiasi dengan memanggil pembangunnya constructor tanpa argumen:

## 5. User-defined Exceptions

- Program dapat memberi nama exception mereka sendiri dengan membuat kelas exception baru (lihat tut-class untuk informasi lebih lanjut tentang kelas Python).
- Exception biasanya berasal dari kelas Exception, baik secara langsung atau tidak langsung.
- Kelas exception dapat didefinisikan yang melakukan apa saja yang dapat dilakukan oleh kelas lain, tetapi biasanya tetap sederhana, seringkali hanya menawarkan sejumlah atribut yang memungkinkan informasi tentang kesalahan diekstraksi oleh penangan sebagai exception.
- Saat membuat modul yang dapat menimbulkan beberapa kesalahan berbeda, praktik yang umum adalah membuat kelas dasar untuk exception yang ditentukan oleh modul itu, dan mensubkelaskan kelas itu untuk membuat kelas exception khusus untuk kondisi kesalahan yang berbeda

## 6. Defining Clean-up Actions

- Pernyataan `try` memiliki klausa opsional lain yang dimaksudkan untuk menentukan tindakan pembersihan yang harus dijalankan dalam semua keadaan.
- Klausa `finally` dieksekusi dalam peristiwa apa pun.
- `TypeError` yang ditimbulkan dengan membagi dua string tidak ditangani oleh klausa except dan karenanya kembali muncul setelah klausa finally telah dieksekusi.
- Dalam aplikasi dunia nyata, klausa finally berguna untuk melepaskan sumber daya eksternal (seperti berkas atau koneksi jaringan), terlepas dari apakah penggunaan sumber daya tersebut berhasil.

## 7. Predefined Clean-up Actions

Beberapa objek mendefinisikan tindakan pembersihan standar yang harus dilakukan ketika objek tidak lagi diperlukan, terlepas dari apakah operasi menggunakan objek berhasil atau gagal. Lihatlah contoh berikut, yang mencoba membuka berkas dan mencetak isinya ke layar.

```python
for line in open("myfile.txt"):
    print(line, end="")
```

Masalah dengan kode ini adalah bahwa ia membiarkan berkas terbuka untuk jumlah waktu yang tidak ditentukan setelah bagian kode ini selesai dieksekusi. Ini bukan masalah dalam skrip sederhana, tetapi bisa menjadi masalah untuk aplikasi yang lebih besar. Pernyataan with memungkinkan objek seperti berkas digunakan dengan cara yang memastikan mereka selalu dibersihkan secepatnya dan dengan benar.

```python
with open("myfile.txt") as f:
    for line in f:
        print(line, end="")
```

Setelah pernyataan dieksekusi, file f selalu ditutup, bahkan jika ada masalah saat pemrosesan baris-baris. Objek yang, seperti berkas-berkas, memberikan tindakan pembersihan yang telah ditentukan, akan menunjukkan ini dalam dokumentasinya.
