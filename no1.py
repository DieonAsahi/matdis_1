# Soal 7
# Soal:
# Sebuah perusahaan memiliki lima lokasi yang dihubungkan oleh jalan dengan jarak yang berbeda. Jalan-jalan tersebut adalah sebagai berikut:

# mathematica
# Salin kode
# 1. Lokasi A ke Lokasi B = 4 km
# 2. Lokasi A ke Lokasi C = 3 km
# 3. Lokasi B ke Lokasi D = 2 km
# 4. Lokasi C ke Lokasi D = 4 km
# 5. Lokasi C ke Lokasi E = 1 km
# 6. Lokasi D ke Lokasi E = 2 km
# Gunakan algoritma Kruskal untuk menemukan pohon rentang minimum.





# Fungsi untuk menemukan set dari simpul menggunakan path compression
def cari(induk, i):
    if induk[i] == i:
        return i
    return cari(induk, induk[i])

# Fungsi untuk menggabungkan dua set menggunakan union by rank
def gabungkan(induk, peringkat, x, y):
    akar_x = cari(induk, x)
    akar_y = cari(induk, y)

    if peringkat[akar_x] < peringkat[akar_y]:
        induk[akar_x] = akar_y
    elif peringkat[akar_x] > peringkat[akar_y]:
        induk[akar_y] = akar_x
    else:
        induk[akar_y] = akar_x
        peringkat[akar_x] += 1

# Fungsi untuk menemukan MST menggunakan algoritma Kruskal
def kruskal_mst(jumlah_simpul, tepi):
    # Urutkan tepi berdasarkan bobotnya
    tepi.sort()
    induk = []
    peringkat = []

    for simpul in range(jumlah_simpul):
        induk.append(simpul)
        peringkat.append(0)

    mst = []
    indeks = 0

    while len(mst) < jumlah_simpul - 1:
        bobot, u, v = tepi[indeks]
        indeks += 1
        x = cari(induk, u)
        y = cari(induk, v)

        if x != y:
            mst.append((u, v, bobot))
            gabungkan(induk, peringkat, x, y)

    return mst

# Definisi graf dengan jumlah simpul dan tepi-tepi
jumlah_simpul = 5
tepi = [
    (4, 0, 1),  # A ke B dengan bobot 4
    (3, 0, 2),  # A ke C dengan bobot 3
    (2, 1, 3),  # B ke D dengan bobot 2
    (4, 2, 3),  # C ke D dengan bobot 4
    (1, 2, 4),  # C ke E dengan bobot 1
    (2, 3, 4)   # D ke E dengan bobot 2
]

# Temukan dan cetak MST menggunakan algoritma Kruskal
mst = kruskal_mst(jumlah_simpul, tepi)
print("Tepi dalam MST:")
for u, v, bobot in mst:
    print(f"{u} -- {v} == {bobot}")
