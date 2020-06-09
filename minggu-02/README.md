# Workshop Python Pertemuan 2 Tutorial 4

>NAMA: Yanuar Galih Waskito
>NIM: 155410211

## More Control Flow Tools

Selain statement while yang diperkenalkan, Python menggunakan flow control statement yang dikenal di bahasa lain.

### 4.1. if-statement
Type pernyataan yang paling terkenal, fungsi pernyataan bersyarat. Dimana suatu statement akan dijalankan ketika pernyataan if bernilai benar.

### 4.2. for Statement
Pernyataan for dalam Python sedikit berbeda dari apa yang mungkin Anda gunakan di C atau Pascal. Alih-alih selalu mengulangi perkembangan aritmatika angka (seperti dalam Pascal), atau memberi pengguna kemampuan untuk menentukan langkah iterasi dan kondisi penghentian (sebagai C), pernyataan Python untuk pernyataan beralih pada item dari urutan apa pun (daftar atau string), dalam urutan yang ditampilkan dalam urutan.

### 4.3. The range() Function
Untuk mengulangi uruta angka

### 4.4. break and continue statements, and else clauses on Loops
Pernyataan break sama seperti dalam bahasa C, keluar dari bagian terdalam for|or|while|loop.

### 4.5. pass Statements
Pernyataan pass tidak melakukan apappun. Dapat digunakan ketika pernyataan diperlukan secara sintaksis tetapi program tidak memerlukan tindakan.

### 4.6. Defining Functions
Fungsi merupakan blok kode yang terorganisir dan dapat digunakan kembali untuk melakukan sebuah tindakan.

### 4.7. More on Defining FUntions
Python memungkinkan untuk mendifinisikan fungsi dengan sejumlah variabel arugumen. Terdapat 3 bentuk yang dapat digabungkan :
- Default Arguments Values
Menentukan nilai default untuk satu atau lebih argumen. Menciptakan fungsi yang bisa dipanggil dengan argumen yang lebih sedikit dari yang diijinkan untuk diijinkan.
- Keywoard Arguments
Fungsi juga dapat dipanggil menggunakan argumen kata kunci dari bentuk kwarg = nilai.
- Special parametes
Secara default, argumen dapat diteruskan ke fungsi Python baik dengan posisi atau secara eksplisit oleh kata kunci. Untuk keterbacaan dan kinerja, masuk akal untuk membatasi cara argumen dapat dilewati sehingga pengembang hanya perlu melihat definisi fungsi untuk menentukan apakah item dilewati oleh posisi, posisi atau kata kunci, atau kata kunci.
- Arbiratry Argument Lists
Opsi yang paling jarang digunakan adalah menentukan bahwa suatu fungsi dapat dipanggil dengan sejumlah argumen arbitrer. Argumen-argumen ini akan dibungkus dalam sebuah tuple (lihat Tuples and Sequences).
- Unpacking Argument Lists
Ketika argumen sudah ada dalam daftar atau tupel tetapi perlu dibongkar untuk panggilan fungsi yang membutuhkan argumen posisi terpisah. Misalnya, fungsi built-in|range()| mengharapkan argumen mulai dan berhenti terpisah.
- Lambda Expressions
Small anonymous function dibuat dengan kata kunci lambda. Fungsi ini mengembalikan jumlah dari dua argumennya: lambda a, b: a + b. Fungsi Lambda dapat digunakan di mana pun objek fungsi diperlukan. Mereka secara sintaksis terbatas pada satu ekspresi. Semantik, mereka hanya gula sintaksis untuk definisi fungsi normal.
- Documentation Strings
Baris pertama harus selalu berupa ringkasan singkat dan ringkas dari tujuan objek. Untuk singkatnya, itu tidak boleh secara eksplisit menyatakan nama atau jenis objek, karena ini tersedia dengan cara lain (kecuali jika nama tersebut merupakan kata kerja yang menggambarkan operasi fungsi). Baris ini harus dimulai dengan huruf kapital dan diakhiri dengan titik.

Jika ada lebih banyak baris dalam string dokumentasi, baris kedua harus kosong, secara visual memisahkan ringkasan dari sisa deskripsi. Baris berikut harus berupa satu atau lebih paragraf yang menggambarkan konvensi pemanggilan objek, efek sampingnya, dll.

Pengurai Python tidak menghapus lekukan dari string multi-line literal di Python, jadi alat yang memproses dokumentasi harus menghapus lekukan jika diinginkan. Ini dilakukan dengan menggunakan konvensi berikut. Baris non-kosong pertama setelah baris pertama string menentukan jumlah indentasi untuk seluruh string dokumentasi. (Kami tidak dapat menggunakan baris pertama karena umumnya berbatasan dengan tanda kutip pembukaan string sehingga lekukannya tidak jelas dalam string literal.) Spasi “ekuivalen” untuk lekukan ini kemudian dilucuti dari awal semua baris string . Garis yang indentasi lebih sedikit seharusnya tidak terjadi, tetapi jika terjadi semua spasi putih utama mereka harus dilucuti. Kesetaraan spasi harus diuji setelah ekspansi tab (hingga 8 spasi, biasanya).
- Function Annotations
Anotasi fungsi adalah informasi metadata yang sepenuhnya opsional tentang jenis yang digunakan oleh fungsi yang ditentukan pengguna.
