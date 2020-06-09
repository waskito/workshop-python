## Workshop Python Pertemuan 5 Tutorial 7 

> NAMA: Yanuar Galih Waskito
> NIM: 155410211
> Source : https://docs.python.org/3.7/tutorial/inputoutput.html

# 7. Input and Output
Ada beberapa cara untuk mempresentasikan output suatu program; data dapat dicetak dalam bentuk yang dapat dibaca manusia, atau ditulis ke file untuk digunakan di masa mendatang.

## 7.1. Fancier Output Formatting
Sejauh ini kami telah menemukan dua cara untuk menulis nilai: pernyataan ekspresi dan fungsi print (). (Cara ketiga menggunakan metode write () dari objek file; file output standar dapat dirujuk sebagai sys.stdout. Lihat Referensi Perpustakaan untuk informasi lebih lanjut tentang ini.)

Ada beberapa cara untuk memformat output.
- Untuk menggunakan string literal yang diformat, mulailah string dengan f atau F sebelum tanda kutip pembuka atau tanda kutip tiga. Di dalam string ini, Anda bisa menulis ekspresi Python antara karakter {dan} yang bisa merujuk ke variabel atau nilai literal.
- Metode str.format () dari string membutuhkan lebih banyak upaya manual. Anda masih akan menggunakan {dan} untuk menandai di mana variabel akan diganti dan dapat memberikan arahan pemformatan terperinci, tetapi Anda juga harus memberikan informasi yang akan diformat.
- Akhirnya, Anda dapat melakukan semua string yang menangani diri Anda sendiri dengan menggunakan operasi slicing dan concatenation untuk membuat tata letak yang dapat Anda bayangkan. Tipe string memiliki beberapa metode yang melakukan operasi yang berguna untuk string padding ke lebar kolom yang diberikan.

Fungsi str () dimaksudkan untuk mengembalikan representasi nilai-nilai yang terbaca oleh manusia, sedangkan repr () dimaksudkan untuk menghasilkan representasi yang dapat dibaca oleh penerjemah (atau akan memaksa SyntaxError jika tidak ada sintaks yang setara). Untuk objek yang tidak memiliki representasi khusus untuk konsumsi manusia, str () akan mengembalikan nilai yang sama dengan repr (). Banyak nilai, seperti angka atau struktur seperti daftar dan kamus, memiliki representasi yang sama menggunakan kedua fungsi tersebut. String, khususnya, memiliki dua representasi berbeda.

### 7.1.1. Formatted String Literal
Literal string terformat (juga singkatnya f-string) memungkinkan untuk memasukkan nilai ekspresi Python di dalam string dengan mengawali string dengan f atau F dan menulis ekspresi sebagai {ekspresi}.

### 7.1.2. The String format() Method
Jika memiliki string format yang sangat panjang yang tidak ingin Anda pisahkan, alangkah baiknya jika dapat merujuk variabel yang akan diformat berdasarkan nama alih-alih berdasarkan posisi. Ini dapat dilakukan hanya dengan melewati dict dan menggunakan tanda kurung siku '[]' untuk mengakses kunci.

### 7.1.3. Manual String Formatting
Perhatikan bahwa satu spasi di antara setiap kolom ditambahkan dengan cara print () berfungsi: ia selalu menambahkan spasi di antara argumennya.)
Metode str.rjust () dari objek string membenarkan string dalam bidang dengan lebar tertentu dengan menambahkannya dengan spasi di sebelah kiri. Ada metode serupa str.ljust () dan str.center (). Metode ini tidak menulis apa pun, mereka hanya mengembalikan string baru. Jika string input terlalu panjang, mereka tidak memotongnya, tetapi mengembalikannya tidak berubah; ini akan mengacaukan tata letak kolom Anda tetapi itu biasanya lebih baik daripada alternatifnya, yang akan berbohong tentang suatu nilai. (Jika Anda benar-benar menginginkan pemotongan, Anda selalu dapat menambahkan operasi slice, seperti pada x.ljust (n) [: n].) Ada metode lain, str.zfill (), yang melapisi string numerik di sebelah kiri dengan nol.

### 7.1.4. Old string formatting
Operator% juga dapat digunakan untuk pemformatan string. Ini mengartikan argumen kiri seperti string format gaya sprintf () untuk diterapkan pada argumen yang benar, dan mengembalikan string yang dihasilkan dari operasi pemformatan ini.

## 7.2. Reading and Writing Files
open () mengembalikan objek file, dan paling umum digunakan dengan dua argumen: open (nama file, mode).

Argumen pertama adalah string yang berisi nama file. Argumen kedua adalah string lain yang berisi beberapa karakter yang menggambarkan cara file akan digunakan. mode dapat 'r' ketika file hanya akan dibaca, 'w' hanya untuk menulis (file yang ada dengan nama yang sama akan dihapus), dan 'a' membuka file untuk ditambahkan; setiap data yang ditulis ke file secara otomatis ditambahkan ke bagian akhir. 'r +' membuka file untuk membaca dan menulis. Argumen mode adalah opsional; 'r' akan diasumsikan jika dihilangkan.

Biasanya, file dibuka dalam mode teks, yang berarti, Anda membaca dan menulis string dari dan ke file, yang dikodekan dalam pengkodean tertentu. Jika pengkodean tidak ditentukan, standarnya adalah tergantung platform (lihat buka ()). 'b' ditambahkan ke mode membuka file dalam mode biner: sekarang data dibaca dan ditulis dalam bentuk objek byte. Mode ini harus digunakan untuk semua file yang tidak mengandung teks.

Dalam mode teks, standar saat membaca adalah mengonversi ujung baris khusus platform (\ n pada Unix, \ r \ n di Windows) menjadi hanya \ n. Saat menulis dalam mode teks, defaultnya adalah untuk mengonversi kemunculan \ n kembali ke akhir baris khusus platform. Modifikasi belakang layar ini untuk mengarsipkan data baik untuk file teks, tetapi akan merusak data biner seperti itu dalam file JPEG atau EXE. Berhati-hatilah untuk menggunakan mode biner saat membaca dan menulis file seperti itu.

Penggunaan kata kunci with saat berurusan with objek file. Keuntungannya adalah bahwa file ditutup with benar setelah suite-nya selesai, bahkan jika suatu pengecualian muncul di beberapa titik. Menggunakan with juga jauh lebih pendek daripada menulis blok try-finally yang setara.

Jika tidak menggunakan kata kunci with, maka harus memanggil f.close () untuk menutup file dan segera membebaskan semua sumber daya sistem yang digunakan olehnya. Jika tidak secara eksplisit menutup file, pengumpul sampah Python pada akhirnya akan menghancurkan objek dan menutup file yang terbuka untuk Anda, tetapi file tersebut mungkin tetap terbuka untuk sementara waktu. Risiko lain adalah implementasi Python yang berbeda akan melakukan pembersihan ini pada waktu yang berbeda.

Setelah objek file ditutup, baik dengan pernyataan with atau dengan memanggil f.close (), upaya untuk menggunakan objek file akan gagal secara otomatis.

### 7.2.1. Methods of File Objects
Untuk membaca konten file, panggil f.read (size), yang membaca sejumlah data dan mengembalikannya sebagai string (dalam mode teks) atau objek byte (dalam mode biner). ukuran adalah argumen numerik opsional. Ketika ukuran dihilangkan atau negatif, seluruh isi file akan dibaca dan dikembalikan; itu masalah Anda jika file tersebut dua kali lebih besar dari memori mesin Anda. Jika tidak, sebagian besar karakter ukuran (dalam mode teks) atau byte ukuran (dalam mode biner) dibaca dan dikembalikan. Jika akhir file telah tercapai, f.read () akan mengembalikan string kosong ('').

f.readline () membaca satu baris dari file; karakter baris baru (\ n) dibiarkan di akhir string, dan hanya dihapus pada baris terakhir file jika file tidak berakhir di baris baru. Ini membuat nilai pengembalian tidak ambigu; jika f.readline () mengembalikan string kosong, akhir file telah tercapai, sementara baris kosong diwakili oleh '\ n', string yang hanya berisi satu baris baru.

f.tell () mengembalikan integer yang memberikan posisi objek file saat ini dalam file yang direpresentasikan sebagai jumlah byte dari awal file ketika dalam mode biner dan angka buram ketika dalam mode teks.
Untuk mengubah posisi objek file, gunakan f.seek (offset, dari mana). Posisi dihitung dari menambahkan offset ke titik referensi; titik referensi dipilih oleh argumen mana. Nilai 0 yang diukur dari awal file, 1 menggunakan posisi file saat ini, dan 2 menggunakan akhir file sebagai titik referensi. di mana dapat dihilangkan dan default ke 0, menggunakan awal file sebagai titik referensi.

### 7.2.2. Saving structured data with json
String dapat dengan mudah ditulis dan dibaca dari file. Angka membutuhkan sedikit usaha, karena metode read () hanya mengembalikan string, yang harus diteruskan ke fungsi seperti int (), yang mengambil string seperti '123' dan mengembalikan nilai numeriknya 123. Saat Anda ingin menyimpan tipe data yang lebih kompleks seperti daftar dan kamus bersarang, penguraian dan serialisasi dengan tangan menjadi rumit.

Alih-alih membuat pengguna terus-menerus menulis dan men-debug kode untuk menyimpan tipe data yang rumit ke file, Python memungkinkan Anda untuk menggunakan format pertukaran data populer yang disebut JSON (JavaScript Object Notation). Modul standar yang disebut json dapat mengambil hierarki data Python, dan mengubahnya menjadi representasi string; proses ini disebut serialisasi. Merekonstruksi data dari representasi string disebut deserializing. Antara serialisasi dan deserializing, string yang mewakili objek mungkin telah disimpan dalam file atau data, atau dikirim melalui koneksi jaringan ke beberapa mesin yang jauh.