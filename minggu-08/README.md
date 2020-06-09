# 10. Brief Tour of the Standard Library

> NAMA: Yanuar Galih Waskito
> NIM: 155410211


## 10.1. Operating System Interface
Modul ***os*** menyediakan puluhan fungsi untuk berinteraksi dengan sistem operasi.
Fungsi dir () dan help () bawaan berguna sebagai alat bantu interaktif untuk bekerja dengan modul besar seperti os.
Untuk tugas manajemen file dan direktori harian, modul shutil menyediakan antarmuka level yang lebih tinggi yang lebih mudah digunakan.
## 10.2. File Wildcards
Modul glob menyediakan fungsi untuk membuat daftar file dari pencarian wildcard direktori.
## 10.3. Command Line Arguments
Skrip utilitas umum seringkali perlu memproses argumen baris perintah. Argumen-argumen ini disimpan dalam atribut argv modul sys sebagai daftar.
Modul argparse menyediakan mekanisme yang lebih canggih untuk memproses argumen baris perintah.
## 10.4. Error Output Redirection and Program Termination
Modul ***sys*** juga memiliki atribut untuk stdin, stdout, dan stderr. Yang terakhir berguna untuk memancarkan peringatan dan pesan kesalahan untuk membuatnya terlihat bahkan ketika stdout telah diarahkan.
## 10.5. String Pattern Matching
Modul ***re*** menyediakan alat ekspresi reguler untuk pemrosesan string lanjutan. Untuk pencocokan dan manipulasi yang kompleks, ekspresi reguler menawarkan solusi yang ringkas dan dioptimalkan.
Ketika hanya kemampuan sederhana yang diperlukan, metode string lebih disukai karena lebih mudah dibaca dan di-debug.
## 10.6. Mathematics
Modul ***math*** memberikan akses ke fungsi C library yang mendasari untuk matematika titik mengambang.
Modul ***random*** menyediakan alat untuk membuat pilihan acak.
Modul ***statistics*** menghitung sifat statistik dasar (rata-rata, median, varian, dll.) Dari data numerik.
Proyek SciPy <https://scipy.org> memiliki banyak modul lain untuk perhitungan numerik.
## 10.7. Internet Access
Ada sejumlah modul untuk mengakses internet dan memproses protokol internet. Dua yang paling sederhana adalah urllib.request untuk mengambil data dari URL dan smtplib untuk mengirim email.
## 10.8. Dates and Times
Modul ***datetime*** menyediakan kelas untuk memanipulasi tanggal dan waktu dengan cara yang sederhana dan kompleks. Sementara aritmatika tanggal dan waktu didukung, fokus implementasi adalah pada ekstraksi anggota yang efisien untuk pemformatan dan manipulasi output. Modul ini juga mendukung objek yang sadar zona waktu.
## 10.9. Data Compression
Format pengarsipan dan kompresi data umum didukung langsung oleh modul termasuk: zlib, gzip, bz2, lzma, zipfile dan tarfile.
## 10.10. Performance Measurement
Beberapa pengguna Python mengembangkan minat mendalam untuk mengetahui kinerja relatif dari berbagai pendekatan untuk masalah yang sama. Python menyediakan alat pengukuran yang segera menjawab pertanyaan-pertanyaan itu.
Sebagai contoh, mungkin tergoda untuk menggunakan fitur tuple packing dan unpacking daripada pendekatan tradisional untuk bertukar argumen. Modul ***timeit*** dengan cepat menunjukkan keunggulan kinerja sederhana.
Berbeda dengan granularitas tingkat halus ***timeit***, modul ***profile*** dan ***pstats*** menyediakan alat untuk mengidentifikasi bagian-bagian penting waktu dalam blok kode yang lebih besar.
## 10.11 Quality Control
Salah satu pendekatan untuk mengembangkan perangkat lunak berkualitas tinggi adalah dengan menulis tes untuk setiap fungsi saat dikembangkan dan untuk menjalankan tes tersebut sering selama proses pengembangan.
Modul ***doctest*** menyediakan alat untuk memindai modul dan memvalidasi tes yang tertanam dalam dokumen program. Konstruksi pengujian sesederhana memotong dan menempel panggilan khas beserta hasilnya ke dalam docstring. Ini meningkatkan dokumentasi dengan memberikan contoh kepada pengguna dan memungkinkan modul doctest untuk memastikan kode tetap benar untuk dokumentasi.
Modul ***unittest*** tidak semudah modul doctest, tetapi memungkinkan serangkaian tes yang lebih komprehensif untuk dipertahankan dalam file terpisah.
## 10.12. Batteries Included
Python memiliki filosofi "batteries included". Ini paling baik dilihat melalui kemampuan yang canggih dan kuat dari paket-paket yang lebih besar.
- Modul ***xmlrpc***.*client* dan ***xmlrpc***.***server*** menjadikan penerapan panggilan prosedur jarak jauh menjadi tugas yang hampir sepele. Terlepas dari nama-nama modul, tidak diperlukan pengetahuan atau penanganan XML secara langsung.
- Paket ***email*** adalah perpustakaan untuk mengelola pesan email, termasuk MIME dan dokumen pesan berbasis **RFC** **2822** lainnya. Tidak seperti **smtplib** dan ***poplib*** yang benar-benar mengirim dan menerima pesan, paket email memiliki perangkat lengkap untuk membangun atau mendekodekan struktur pesan yang kompleks (termasuk lampiran) dan untuk mengimplementasikan pengkodean internet dan protokol header.
- Paket ***json*** menyediakan dukungan kuat untuk mem-parsing format pertukaran data populer ini. Modul ***csv*** mendukung pembacaan dan penulisan file secara langsung dalam format Nilai Terpisah Koma, yang umumnya didukung oleh database dan spreadsheet. Pemrosesan XML didukung oleh paket ***xml.etree.ElementTree***, ***xml.dom*** dan ***xml.sax***. Bersama-sama, modul dan paket ini sangat menyederhanakan pertukaran data antara aplikasi Python dan alat lainnya.
- Modul ***sqlite3*** adalah pembungkus untuk pustaka database SQLite, menyediakan database persisten yang dapat diperbarui dan diakses menggunakan sintaks SQL yang sedikit tidak standar.
- Internasionalisasi didukung oleh sejumlah modul termasuk ***gettext***, ***locale***, dan paket ***codec***.

# 11. Brief Tour of the Standard Library — Part II
## 11.1. Output Formatting
Modul ***reprlib*** menyediakan versi ***repr ()*** yang disesuaikan untuk tampilan yang disingkat dari wadah yang besar atau sangat bersarang.
Modul ***pprint*** menawarkan kontrol yang lebih canggih atas pencetakan baik objek bawaan maupun yang ditentukan pengguna dengan cara yang dapat dibaca oleh penerjemah. Ketika hasilnya lebih dari satu baris, "pretty printer" menambahkan jeda baris dan lekukan untuk lebih jelas mengungkapkan struktur data.
Modul ***textwrap*** memformat paragraf teks agar sesuai dengan lebar layar yang diberikan.
Modul ***locale*** mengakses basis data format data spesifik budaya. Atribut pengelompokan fungsi format lokal menyediakan cara langsung memformat angka dengan pemisah grup.
## 11.2. Templating
Modul ***string*** menyertakan kelas Templat yang fleksibel dengan sintaks yang disederhanakan yang cocok untuk diedit oleh pengguna akhir. Ini memungkinkan pengguna untuk menyesuaikan aplikasi mereka tanpa harus mengubah aplikasi.
Format ini menggunakan nama placeholder yang dibentuk oleh $ dengan pengidentifikasi Python yang valid (karakter alfanumerik dan garis bawah). Mengitari placeholder dengan kawat gigi memungkinkannya diikuti oleh lebih banyak huruf alfanumerik tanpa spasi. Menulis $$ membuat satu lolos $.
Metode ***subtitusi*** () memunculkan KeyError ketika placeholder tidak disediakan dalam kamus atau argumen kata kunci. Untuk aplikasi gaya gabungan surat, data yang diberikan pengguna mungkin tidak lengkap dan metode safe_substitute () mungkin lebih tepat - itu akan membuat penampung tidak berubah jika data hilang.
Subkelas templat dapat menentukan pembatas khusus. Misalnya, utilitas penggantian nama batch untuk browser foto dapat memilih untuk menggunakan tanda persen untuk penampung seperti tanggal saat ini, nomor urut gambar, atau format file.
Aplikasi lain untuk templating adalah memisahkan logika program dari detail berbagai format output. Ini memungkinkan untuk mengganti template khusus untuk file XML, laporan teks biasa, dan laporan web HTML.
## 11.3. Working with Binary Data Record Layouts
Modul ***struct*** menyediakan fungsi pack () dan unpack () untuk bekerja dengan format rekaman biner panjang variabel.
## 11.4. Multi-threading
Threading adalah teknik untuk memisahkan tugas-tugas yang tidak tergantung secara berurutan. Utas dapat digunakan untuk meningkatkan responsif aplikasi yang menerima input pengguna saat tugas lain berjalan di latar belakang. Kasus penggunaan terkait menjalankan I / O secara paralel dengan perhitungan di utas lainnya.
Tantangan utama aplikasi multi-threaded adalah mengoordinasikan utas yang berbagi data atau sumber daya lainnya. Untuk itu, modul threading menyediakan sejumlah primitif sinkronisasi termasuk kunci, peristiwa, variabel kondisi, dan semaphore.
## 11.5. Logging
Modul ***logging*** menawarkan sistem logging yang berfitur lengkap dan fleksibel. Paling sederhana, pesan log dikirim ke file atau ke *sys.stderr*.
istem logging dapat dikonfigurasikan secara langsung dari Python atau dapat diambil dari file konfigurasi yang dapat diedit pengguna untuk logging yang dikustomisasi tanpa mengubah aplikasi.
## 11.6. Weak References
Python melakukan manajemen memori otomatis (penghitungan referensi untuk sebagian besar objek dan pengumpulan sampah untuk menghilangkan siklus). Memori dibebaskan tidak lama setelah referensi terakhir untuk itu telah dihilangkan.
## 11.7. Tools for Working with Lists
Banyak kebutuhan struktur data dapat dipenuhi dengan tipe built-in list. Namun, kadang-kadang ada kebutuhan untuk implementasi alternatif dengan trade-off kinerja yang berbeda.
Modul ***array*** menyediakan objek *array ()* yang seperti daftar yang hanya menyimpan data homogen dan menyimpannya dengan lebih kompak.
Modul ***collecions*** menyediakan objek *deque ()* yang seperti daftar dengan menambahkan lebih cepat dan muncul dari sisi kiri tetapi pencarian lebih lambat di tengah. Objek-objek ini sangat cocok untuk mengimplementasikan antrian dan pencarian pohon pertama yang luas.
Selain implementasi daftar alternatif, library juga menawarkan alat lain seperti modul ***bisect*** dengan fungsi untuk memanipulasi daftar yang diurutkan.
Modul ***heapq*** menyediakan fungsi untuk mengimplementasikan tumpukan berdasarkan daftar reguler. Entri bernilai terendah selalu disimpan di posisi nol. Ini berguna untuk aplikasi yang berulang kali mengakses elemen terkecil tetapi tidak ingin menjalankan semacam daftar lengkap.
## 11.8. Decimal Floating Point Arithmetic
Modul desimal menawarkan tipe data Desimal untuk aritmatika floating point desimal. Dibandingkan dengan implementasi float bawaan dari floating point biner, kelas ini sangat membantu untuk
- aplikasi keuangan dan penggunaan lainnya yang membutuhkan representasi desimal yang tepat,
- kontrol atas presisi,
- kontrol atas pembulatan untuk memenuhi persyaratan hukum atau peraturan,
- pelacakan tempat desimal yang signifikan, atau
- aplikasi tempat pengguna mengharapkan hasil agar sesuai dengan perhitungan yang dilakukan dengan tangan.
Modul desimal memberikan aritmatika dengan presisi sebanyak yang dibutuhkan
