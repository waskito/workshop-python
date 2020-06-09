# 12. Virtual Environments and Packages

> NAMA: Yanuar Galih Waskito
> NIM: 155410211

## 12.1. Introduction
Virtual environment dapat menjadi solusi ketika kita membutuhkan library python dengan versi yang berbeda untuk aplikasi yang akan kita buat. Dengan membuat virtual environment kita dapat menggunakannya tanpa mengubah apapun yang sudah terpasang di komputer/aplikasi kita sebelumnya.
## 12.2. Creating Virtual Environments
Modul yang digunakan untuk membuat dan mengelola virtual environments disebut venv. venv biasanya akan menginstal versi Python terbaru yang di miliki. Jika memiliki beberapa versi Python di sistem, dapat memilih versi Python tertentu dengan menjalankan python3 atau versi mana pun yang di inginkan.
Untuk membuat virtual environment, tentukan direktori tempat untuk meletakkannya, dan jalankan modul venv sebagai skrip dengan jalur direktori.
Lokasi direktori umum untuk virtual environment adalah .venv. Nama ini menyimpan direktori yang biasanya tersembunyi di dalam shell dan dengan demikian menyingkir sambil memberikannya nama yang menjelaskan mengapa direktori itu ada. Ini juga mencegah bentrok dengan file definisi variabel .env environment yang didukung oleh beberapa tooling.
Mengaktifkan virtual environment akan mengubah prompt shell Anda untuk menunjukkan virtual environment apa yang Anda gunakan, dan memodifikasi environment sehingga menjalankan python akan membuat Anda mendapatkan versi tertentu dan pemasangan Python.
## 12.3. Managing Packages with pip
Untuk menginstal, upgrade dan menghapus paket dapat menggunakan pip. Secara default pip akan menginstal paket dari indek paket python <https://pypi.org>. Untuk menelusuri paket python dapat menggunakan browser atau pip search secara terbatas.

Source : https://docs.python.org/3/tutorial/venv.html

---
# Getting started with conda
Conda adalah manajer paket yang powerful dan manajer environment yang di gunakan dengan perintah baris perintah di Anaconda Prompt untuk Windows, atau di jendela terminal untuk macOS atau Linux.
## Starting conda
## Managing conda
## Managing Environment
Conda memungkinkan Anda untuk membuat environment terpisah yang berisi file, paket, dan dependensinya yang tidak akan berinteraksi dengan environment lain.
Ketika mulai menggunakan conda, sudah memiliki environment default bernama base. Jika tidak ingin memasukkan program ke environment basis. Buat environment terpisah untuk menjaga program terisolasi satu sama lain.
## Managing Python
Saat Anda membuat lingkungan baru, Anda dapat menginstal versi Python yang sama dengan yang Anda gunakan saat mengunduh dan menginstal Anaconda. Jika Anda ingin menggunakan versi Python yang berbeda, misalnya Python 3.5, cukup buat lingkungan baru dan tentukan versi Python yang Anda inginkan.
## Managing packages
Sorce : https://docs.conda.io/projects/conda/en/latest/user-guide/getting-started.html