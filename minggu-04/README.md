## Workshop Python Pertemuan 4 Tutorial 6 
 
> NAMA: Yanuar Galih Waskito
> NIM: 155410211
> Source :https://docs.python.org/3.7/tutorial/modules.html

# 6. Modules
Python memiliki cara untuk meletakkan definisi dalam file dan menggunakannya dalam skrip atau dalam contoh interaktif dari interpreter. File seperti itu disebut modul; definisi dari suatu modul dapat diimpor ke modul lain atau ke modul utama (kumpulan variabel yang memiliki akses ke dalam skrip dieksekusi di tingkat atas dan dalam mode kalkulator).

Modul adalah file yang berisi definisi dan pernyataan Python. Nama file adalah nama modul dengan akhiran .py. Dalam sebuah modul, nama modul (sebagai string) tersedia sebagai nilai variabel global __name__.

## 6.1. More on Modules
Modul dapat berisi pernyataan yang dapat dieksekusi serta definisi fungsi. Pernyataan-pernyataan ini dimaksudkan untuk menginisialisasi modul. Mereka dieksekusi hanya pertama kali nama modul ditemui dalam pernyataan impor. 1 (Mereka juga dijalankan jika file dieksekusi sebagai skrip.)

Setiap modul memiliki tabel simbol pribadi sendiri, yang digunakan sebagai tabel simbol global oleh semua fungsi yang didefinisikan dalam modul. Dengan demikian, penulis modul dapat menggunakan variabel global dalam modul tanpa khawatir tentang bentrokan tidak disengaja dengan variabel global pengguna. Di sisi lain, jika tahu apa yang dilakukan, dapat menyentuh variabel global modul dengan notasi yang sama yang digunakan untuk merujuk ke fungsinya, modname.itemname.

Pada praktikum ini sesuai dengan yang terdapat dalam tutorial modul yang digunakan adalah fibo.py

Note : Untuk alasan efisiensi, setiap modul hanya diimpor satu kali per sesi Interpreter. Oleh karena itu, jika Anda mengubah modul, Anda harus memulai ulang Interpreter - atau, jika hanya satu modul yang ingin Anda uji secara interaktif, gunakan memuat reload (), mis. reload (modulename).

### 6.1.1. Executing modules as scripts
Jika menjalankan modul Python dengan *python fibo.py <arguments>* kode dalam modul akan dieksekusi, sama seperti jika Anda mengimpornya, tetapi dengan __name__ diatur ke "__main__".

Ini sering digunakan baik untuk menyediakan antarmuka pengguna yang nyaman ke modul, atau untuk tujuan pengujian (menjalankan modul sebagai skrip menjalankan suite pengujian).

### 6.1.2. The Module Search Path
Ketika modul bernama spam diimpor, penerjemah pertama-tama mencari modul bawaan dengan nama itu. Jika tidak ditemukan, ia kemudian mencari file bernama spam.py di daftar direktori yang diberikan oleh variabel sys.path. sys.path diinisialisasi dari lokasi ini:
- direktori yang berisi skrip input (atau direktori saat ini).
- PYTHONPATH (daftar nama direktori, dengan sintaksis yang sama dengan PATH variabel shell).
- standar yang bergantung pada instalasi.

Setelah inisialisasi, program Python dapat memodifikasi sys.path. Direktori yang berisi skrip yang dijalankan ditempatkan di awal jalur pencarian, di depan jalur perpustakaan standar. Ini berarti bahwa skrip dalam direktori tersebut akan dimuat alih-alih modul dengan nama yang sama di direktori perpustakaan. Ini adalah kesalahan kecuali penggantian dimaksudkan. Lihat bagian Modul Standar untuk informasi lebih lanjut.

### 6.1.3. “Compiled” Python files
Sebagai percepatan penting waktu start-up untuk program pendek yang menggunakan banyak modul standar, jika file bernama spam.pyc ada di direktori tempat spam.py ditemukan, ini diasumsikan mengandung sudah- “ versi byte-dikompilasi ”dari modul spam. Waktu modifikasi versi spam.py yang digunakan untuk membuat spam.pyc direkam dalam spam.pyc, dan file .pyc diabaikan jika ini tidak cocok.

Biasanya, Anda tidak perlu melakukan apa pun untuk membuat file spam.pyc. Setiap kali spam.py berhasil dikompilasi, upaya dilakukan untuk menulis versi yang dikompilasi ke spam.pyc. Ini bukan kesalahan jika upaya ini gagal; jika karena alasan apa pun file tidak ditulis sepenuhnya, file spam.pyc yang dihasilkan akan dikenali tidak valid dan karenanya diabaikan kemudian. Isi file spam.pyc bersifat independen terhadap platform, sehingga direktori modul Python dapat dibagikan oleh mesin dari arsitektur yang berbeda.
Beberapa tips untuk para ahli:
- Ketika interpreter Python dipanggil dengan flag -O, kode yang dioptimalkan dihasilkan dan disimpan dalam file .pyo. Pengoptimal saat ini tidak banyak membantu; itu hanya menghilangkan pernyataan tegas. Ketika -O digunakan, semua bytecode dioptimalkan; File .pyc diabaikan dan file .py dikompilasi untuk bytecode yang dioptimalkan.
- Melewati dua -O flag ke interpreter Python (-OO) akan menyebabkan kompiler bytecode untuk melakukan optimasi yang dalam beberapa kasus jarang mengakibatkan program yang tidak berfungsi. Saat ini hanya string __doc__ yang dihapus dari bytecode, menghasilkan file .pyo yang lebih ringkas. Karena beberapa program mungkin mengandalkan ini tersedia, Anda hanya boleh menggunakan opsi ini jika Anda tahu apa yang Anda lakukan.
- Suatu program tidak berjalan lebih cepat ketika itu dibaca dari file .pyc atau .pyo daripada ketika itu dibaca dari file .py; satu-satunya hal yang lebih cepat tentang file .pyc atau .pyo adalah kecepatannya.
- Ketika skrip dijalankan dengan memberikan namanya pada baris perintah, bytecode untuk skrip tidak pernah ditulis ke file .pyc atau .pyo. Dengan demikian, waktu mulai skrip dapat dikurangi dengan memindahkan sebagian besar kodenya ke modul dan memiliki skrip bootstrap kecil yang mengimpor modul itu. Dimungkinkan juga untuk menamai file .pyc atau .pyo secara langsung pada baris perintah.
- Dimungkinkan untuk memiliki file yang disebut spam.pyc (atau spam.pyo ketika -O digunakan) tanpa file spam.py untuk modul yang sama. Ini dapat digunakan untuk mendistribusikan pustaka kode Python dalam bentuk yang cukup sulit untuk dibalikkan.
- Modul compileall dapat membuat file .pyc (atau .pyo file ketika -O digunakan) untuk semua modul dalam direktori.

## 6.2. Standard Modules
Python dilengkapi dengan pustaka modul standar, yang dijelaskan dalam dokumen terpisah, Referensi Pustaka Python (“Pustaka Referensi” selanjutnya). Beberapa modul dibangun ke interpreter; ini menyediakan akses ke operasi yang bukan bagian dari inti bahasa tetapi tetap dibangun, baik untuk efisiensi atau untuk menyediakan akses ke sistem operasi primitif seperti panggilan sistem. Set modul tersebut adalah opsi konfigurasi yang juga tergantung pada platform yang mendasarinya. Misalnya, modul winreg hanya disediakan pada sistem Windows. Satu modul tertentu patut mendapat perhatian: sys, yang dibangun ke dalam setiap interpreter Python.

Variabel sys.path adalah daftar string yang menentukan jalur pencarian penerjemah untuk modul. Ini diinisialisasi ke jalur default yang diambil dari variabel lingkungan PYTHONPATH, atau dari bawaan bawaan jika PYTHONPATH tidak diatur.

## 6.3. The dir() Function
Fungsi dir bawaan () digunakan untuk mencari tahu nama mana yang didefinisikan oleh modul.

## 6.4. Packages
Paket adalah cara penataan namespace modul Python dengan menggunakan "dotted module names". Sebagai contoh, nama modul AB menunjuk sebuah submodule bernama B dalam paket bernama A. Sama seperti penggunaan modul menyelamatkan penulis modul yang berbeda dari harus khawatir tentang nama variabel global masing-masing, penggunaan nama modul bertitik menyimpan penulis paket multi-modul seperti NumPy atau Pillow karena harus khawatir tentang nama modul masing-masing.

### 6.4.1. Importing * From a Package
### 6.4.2. Intra-package References
erhatikan bahwa impor relatif eksplisit dan implisit didasarkan pada nama modul saat ini. Karena nama modul utama selalu "__main__", modul yang dimaksudkan untuk digunakan sebagai modul utama aplikasi Python harus selalu menggunakan impor absolut.

### 6.4.3. Packages in Multiple Directories
Paket mendukung satu atribut khusus lagi, __path__. Ini diinisialisasi menjadi daftar yang berisi nama direktori yang menyimpan paket __init__.py sebelum kode dalam file tersebut dieksekusi. Variabel ini dapat dimodifikasi; hal itu memengaruhi pencarian modul dan subpackage di masa depan yang terkandung dalam paket.

Meskipun fitur ini tidak sering dibutuhkan, ia dapat digunakan untuk memperluas set modul yang ditemukan dalam sebuah paket.
