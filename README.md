# Program Perkalian Matriks 5x5 dengan Python

Program ini dibuat menggunakan bahasa pemrograman Python.

## Fitur
- Melakukan perkalian dua matriks 5x5
- Menampilkan hasil perkalian dalam bentuk matriks
- Menggunakan struktur perulangan `for` dan metode `append`
- Cocok untuk pembelajaran dasar operasi matriks

## Cara Kerja

Program menggunakan rumus dasar perkalian matriks:

hasil[i][j] = A[i][0]×B[0][j] + A[i][1]×B[1][j] + ... + A[i][4]×B[4][j]

Dengan tiga lapis perulangan:
- Baris matriks A
- Kolom matriks B
- Perkalian dan penjumlahan elemen-elemen

## Output Matriks 1 dan Matriks 2

```sh
matrix_1 = [
    [1,1,3,6,2],
    [9,5,2,4,6],
    [3,4,2,5,1],
    [6,2,4,6,2],
    [8,3,5,3,5]
]

matrix_2 = [
    [2,2,5,3,2],
    [4,6,2,1,6],
    [0,2,2,5,7],
    [5,6,7,4,2],
    [7,3,5,2,8]
]
```

## Output Hasil
```sh
Hasil perkalian matriks 5 x 5:
[50, 56, 65, 47, 57]
[100, 94, 117, 70, 118]
[54, 67, 67, 45, 62]
[64, 74, 94, 68, 80]
[78, 77, 102, 74, 115]
```


