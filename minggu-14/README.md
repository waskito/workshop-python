# An introduction to machine learning with scikit-learn

> NAMA: Yanuar Galih Waskito
> NIM: 155410211

## Machine learning: the problem setting
Pembelajaran terbagi dalam beberapa kategori :
- Supervised learning, data dilengkapi atribut tambahan yang ingin diprediksi. Masalah dapat berupa :
  - Classification
  - Regression
- Unsupervised learning, di mana data pelatihan terdiri dari sekumpulan vektor input x tanpa nilai target yang sesuai. Tujuan dalam masalah tersebut mungkin untuk menemukan kelompok contoh serupa dalam data, di mana disebut clustering, atau untuk menentukan distribusi data dalam ruang input, yang dikenal sebagai estimasi kepadatan, atau untuk memproyeksikan data dari dimensi tinggi.

## Loading and example dataset
scikit-learn dilengkapi dengan beberapa dataset standar, misalnya dataset iris dan digit untuk klasifikasi dan dataset diabetes untuk regresi.

## Learning and predicting
Dalam scikit-belajar, estimator untuk klasifikasi adalah objek Python yang mengimplementasikan metode fit (X, y) dan memprediksi (T).

## Model persistence
Dimungkinkan untuk menyimpan model di scikit-learn dengan menggunakan model persistensi built-in Python.

## Conventions
scikit-learn estimators mengikuti aturan tertentu untuk membuat perilakunya lebih prediktif.
Sumber : https://scikit-learn.org/stable/tutorial/basic/tutorial.html