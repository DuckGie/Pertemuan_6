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

hasil = []

for i in range(5):
    baris = []
    for j in range(5):
        total = 0
        for k in range(5):
            total += matrix_1[i][k] * matrix_2[k][j]
        baris.append(total)
    hasil.append(baris)

print("\nHasil perkalian matriks 5 x 5:")
for baris in hasil:
    print(baris)