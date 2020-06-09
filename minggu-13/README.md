# Workshop Python Pertemuan 13 → 10 minutes to pandas

> NAMA: Yanuar Galih Waskito
> NIM: 155410211

## Object creation
**Series** adalah array berlabel satu dimensi yang mampu menampung semua tipe data (bilangan bulat, string, angka floating point, objek Python, dll.). Label sumbu secara kolektif disebut sebagai *index*. Metode dasar untuk membuat Series adalah memanggil **pd.Series(data, index=index)**.
## Viewing data
Untuk melihat sampel kecil objek Series atau DataFrame, gunakan metode head () dan tail (). Jumlah elemen default untuk ditampilkan adalah lima, tetapi dapat dirubah dengan meng kutom jumlahnya.
## Selection
Pada bagian ini memperlihatkan bagaimana dilakukan selection data Seperti memilih salah satu kolom dengan nama tertentu. Memilih dengan mengiris baris dari baris yang dimaksud hingga baris yang ditentukan.
## Missing data
NaN adalah penanda nilai hilang standar karena alasan kecepatan dan kenyamanan komputasi, kita harus dapat dengan mudah mendeteksi nilai ini dengan data dari berbagai jenis: floating point, integer, boolean, dan objek umum. Dalam pembahasan ini membahas mengenai missing data seperti menampilkan, menghapus dan mengisi data.
## Operations
Operasi secara umum mengecualikan data yang hilang. Operasi yang dimaksud operasi statistik, apply, histogramming, string method.
## Merge
Pandas menyediakan berbagai fasilitas untuk dengan mudah menggabungkan objek Series dan DataFrame dengan berbagai jenis logika yang ditetapkan untuk indeks dan fungsionalitas aljabar relasional dalam kasus operasi join / merge-type.
## Grouping
Dengan "Group by", mengacu pada proses yang melibatkan satu atau lebih langkah-langkah berikut :
- **Splitting** data ke dalam kelompok berdasarkan beberapa kritesia
- **Applying** fungsi untuk masing-masing kelompok secara mandiri
- **Combining** hasilnya menjadi struktur data
## Reshaping
Metode ini dirancang untuk bekerja bersama dengan objek MultiIndex. Berikut ini pada dasarnya apa yang dilakukan metode ini:
- stack: "pivot" tingkat label kolom (mungkin hierarkis), mengembalikan DataFrame dengan indeks dengan label baris paling baru paling dalam.
- unstack: (operasi invers tumpukan) "pivot" tingkat indeks baris (mungkin hierarkis) ke sumbu kolom, menghasilkan DataFrame yang dibentuk kembali dengan tingkat baru paling dalam label kolom.
Fungsi pivot_table () dapat digunakan untuk membuat tabel pivot gaya spreadsheet.
## Time series
Pandas berisi kemampuan dan fitur yang luas untuk bekerja dengan data deret waktu untuk semua domain. Menggunakan datum64 NumPy dan timedelta64 dtypes, panda telah mengkonsolidasikan sejumlah besar fitur dari pustaka Python lain seperti scikits.timeseries serta menciptakan sejumlah besar fungsi baru untuk memanipulasi data deret waktu.
## Catgoricals
Categoricals adalah tipe data panda yang sesuai dengan variabel kategorikal dalam statistik. Variabel kategorikal mengambil sejumlah nilai yang mungkin terbatas (dan biasanya tetap, dalam kategori R).
## Plotting
## Getting data in/out
## Gotchas
Source : https://pandas.pydata.org/pandas-docs/stable/getting_started/10min.html