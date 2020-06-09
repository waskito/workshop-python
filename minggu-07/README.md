# Classes

> NAMA: Yanuar Galih Waskito
> NIM: 155410211

Kelas menyediakan cara menggabungkan data dan fungsionalitas bersama. Membuat kelas baru menciptakan tipe objek baru, memungkinkan instance baru dari tipe itu dibuat. Setiap instance kelas dapat memiliki atribut yang melekat. Instance kelas juga dapat memiliki metode (ditentukan oleh kelasnya) untuk memodifikasi kondisinya.

Kelas Python menyediakan semua fitur standar Pemrograman Berorientasi Objek: mekanisme pewarisan kelas memungkinkan beberapa kelas dasar, kelas turunan dapat menimpa metode apa pun dari kelas dasar atau kelasnya, dan metode dapat memanggil metode kelas dasar dengan nama yang sama . Objek dapat berisi jumlah dan jenis data yang berubah-ubah. Seperti halnya untuk modul, kelas mengambil bagian dari sifat dinamis Python: mereka dibuat pada saat runtime, dan dapat dimodifikasi lebih lanjut setelah pembuatan.
## 9.1. A Word About Names and Objects
Objek memiliki individualitas, dan banyak nama (dalam berbagai lingkup) dapat terikat ke objek yang sama. Ini dikenal sebagai aliasing dalam bahasa lain. Ini biasanya tidak dihargai pada pandangan pertama pada Python, dan dapat diabaikan dengan aman ketika berhadapan dengan tipe dasar yang tidak berubah (angka, string, tupel). Namun, aliasing memiliki efek yang mungkin mengejutkan pada semantik kode Python yang melibatkan objek yang bisa berubah seperti lists, dictionaries, dan sebagian besar tipe lainnya. Ini biasanya digunakan untuk kepentingan program, karena alias berperilaku seperti petunjuk dalam beberapa hal.
## 9.2. Python Scopes and Namespaces
**Namespace** adalah pemetaan dari nama ke objek. Contoh namespaces adalah: himpunan nama bawaan (berisi fungsi seperti abs (), dan nama pengecualian bawaan); nama global dalam sebuah modul; dan nama-nama lokal dalam fungsi. Dalam arti himpunan atribut suatu objek juga membentuk namespace. Hal penting yang perlu diketahui tentang namespaces adalah sama sekali tidak ada hubungan antara nama dalam namespaces yang berbeda; misalnya, dua modul yang berbeda dapat menentukan fungsi *maximize* tanpa confusion - users modul harus awalan dengan nama modul.

**Scope** adalah wilayah tekstual dari program Python di mana namespace dapat diakses secara langsung. "Dapat diakses secara langsung" di sini berarti bahwa referensi yang tidak memenuhi syarat untuk suatu nama berusaha menemukan nama tersebut di namespace.
### 9.2.1. Scopes and Namespaces Example
## 9.3. A First Look at Classes
Kelas memperkenalkan sedikit sintaks baru, tiga tipe objek baru, dan beberapa semantik baru.
### 9.3.1. Class Definition Syntax
Definisi kelas, seperti definisi fungsi (pernyataan def) harus dieksekusi sebelum mereka memiliki efek. (Anda bisa menempatkan definisi kelas di cabang pernyataan if, atau di dalam fungsi.)

### 9.3.2. Class Objects
Objek kelas mendukung dua jenis operasi: referensi atribut dan instantiasi.
**Referensi atribut** menggunakan sintaksis standar yang digunakan untuk semua referensi atribut dengan Python: obj.name. Nama atribut yang valid adalah semua nama yang ada di namespace kelas ketika objek kelas dibuat.

**Instansiasi** kelas menggunakan notasi fungsi. Hanya berpura-pura bahwa objek kelas adalah fungsi tanpa parameter yang mengembalikan instance baru dari kelas.
### 9.3.3. Instance Objects
Satu-satunya operasi yang dipahami oleh objek instan adalah referensi atribut. Ada dua jenis nama atribut yang valid: atribut data dan metode.
**atribut data** sesuai dengan "variabel instan" di Smalltalk, dan "anggota data" di C ++. Atribut data tidak perlu dinyatakan; seperti variabel lokal, mereka muncul ketika mereka pertama kali ditugaskan.
Jenis lain dari referensi atribut instance adalah **metode**. Metode adalah fungsi yang "milik" suatu objek. Nama metode yang valid dari objek instan bergantung pada kelasnya. Menurut definisi, semua atribut kelas yang merupakan objek fungsi menentukan metode yang sesuai dari instansnya.
### 9.3.4. Method Objects
### 9.3.5. Class and Instance Variables
Secara umum, variabel instance adalah untuk data unik untuk setiap instance dan variabel kelas adalah untuk atribut dan metode yang dibagikan oleh semua instance kelas.
## 9.4. Random Remarks
Jika nama atribut yang sama muncul di kedua instance dan di kelas, maka pencarian atribut memprioritaskan instance.
## 9.5. Inheritance
Kelas turunan dapat menimpa metode kelas dasar mereka. Karena metode tidak memiliki hak khusus ketika memanggil metode lain dari objek yang sama, metode kelas dasar yang memanggil metode lain yang didefinisikan dalam kelas dasar yang sama mungkin akhirnya memanggil metode kelas turunan yang menimpanya.
Python memiliki dua fungsi built-in yang bekerja dengan inheritance:
- Gunakan isinstance () untuk memeriksa tipe instance: isinstance (obj, int) akan Benar hanya jika obj .__ class__ adalah int atau beberapa kelas berasal dari int.
- Gunakan issubclass () untuk memeriksa warisan kelas: issubclass (bool, int) Benar karena bool adalah subclass dari int. Namun, issubclass (float, int) adalah False karena float bukan subclass dari int.
### 9.5.1. Multiple Inheritance
Python mendukung bentuk pewarisan berganda juga.
## 9.6. Private Variables
Variabel instance "Privat" yang tidak dapat diakses kecuali dari dalam objek yang tidak ada di Python. Namun, ada konvensi yang diikuti oleh sebagian besar kode Python: nama diawali dengan garis bawah (misalnya _spam) harus diperlakukan sebagai bagian non-publik dari API (apakah itu fungsi, metode atau anggota data) . Ini harus dianggap sebagai detail implementasi dan dapat berubah tanpa pemberitahuan.
Name mangling sangat membantu untuk membiarkan subclass menimpa metode tanpa memutus panggilan metode intraclass.
## 9.7. Odds and Ends
## 9.8. Iterators
## 9.9. Generators
Generator adalah alat sederhana dan kuat untuk membuat iterator. Ditulis seperti fungsi biasa tetapi menggunakan pernyataan hasil setiap kali  ingin mengembalikan data. Setiap kali next () dipanggil, generator melanjutkan di tempat yang ditinggalkannya (mengingat semua nilai data dan pernyataan mana yang terakhir dieksekusi).
Apa pun yang dapat dilakukan dengan generator juga dapat dilakukan dengan iterator berbasis kelas seperti yang dijelaskan pada bagian sebelumnya. Apa yang membuat generator sangat kompak adalah bahwa metode __iter __ () dan __next __ () dibuat secara otomatis.
Fitur utama lainnya adalah variabel lokal dan status eksekusi secara otomatis disimpan di antara panggilan. Ini membuat fungsi lebih mudah untuk ditulis dan jauh lebih jelas daripada pendekatan menggunakan variabel instan seperti self.index dan self.data.
Selain pembuatan metode otomatis dan status program penyimpanan, ketika generator berhenti, mereka secara otomatis meningkatkan StopIteration. Secara kombinasi, fitur-fitur ini membuatnya mudah untuk membuat iterator tanpa lebih dari sekadar menulis fungsi biasa.
## 9.10. Generator Expressions
Beberapa generator sederhana dapat dikodekan secara ringkas sebagai ekspresi menggunakan sintaksis yang mirip dengan pemahaman daftar tetapi dengan tanda kurung alih-alih tanda kurung siku. Ungkapan-ungkapan ini dirancang untuk situasi di mana generator digunakan segera oleh fungsi penutup. Ekspresi generator lebih kompak tetapi kurang fleksibel daripada definisi generator penuh dan cenderung lebih ramah memori daripada pemahaman daftar setara.