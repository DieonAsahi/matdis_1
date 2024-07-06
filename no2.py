# Kasus: Sistem Deteksi Penyakit Berdasarkan Gejala
# Misalkan kita ingin membuat sistem sederhana yang mendeteksi kemungkinan penyakit berdasarkan gejala yang diberikan. Kita menggunakan aljabar boolean untuk menentukan apakah seseorang mungkin menderita penyakit tertentu berdasarkan gejala yang dialami.


def deteksi_penyakit(B, P, D, NS, BM, M, NO, K):
    flu = B and P and D
    demam_berdarah = D and NS and BM
    malaria = D and M and NO
    tifus = D and NS and K
    
    hasil = []
    if flu:
        hasil.append("Flu")
    if demam_berdarah:
        hasil.append("Demam Berdarah")
    if malaria:
        hasil.append("Malaria")
    if tifus:
        hasil.append("Tifus")
    
    return hasil if hasil else ["Tidak ada penyakit yang terdeteksi"]

def input_gejala():
    print("Masukkan gejala yang Anda alami dengan mengetik 1 untuk 'Ya' dan 0 untuk 'Tidak':")
    B = int(input("Apakah Anda mengalami batuk? (1/0): "))
    P = int(input("Apakah Anda mengalami pilek? (1/0): "))
    D = int(input("Apakah Anda mengalami demam? (1/0): "))
    NS = int(input("Apakah Anda mengalami nyeri sendi? (1/0): "))
    BM = int(input("Apakah Anda mengalami bintik merah? (1/0): "))
    M = int(input("Apakah Anda mengalami menggigil? (1/0): "))
    NO = int(input("Apakah Anda mengalami nyeri otot? (1/0): "))
    K = int(input("Apakah Anda mengalami kelelahan? (1/0): "))
    
    return B, P, D, NS, BM, M, NO, K

# Input gejala dari pengguna
B, P, D, NS, BM, M, NO, K = input_gejala()

# Deteksi penyakit berdasarkan gejala yang diinput
penyakit = deteksi_penyakit(B, P, D, NS, BM, M, NO, K)
print("Penyakit yang terdeteksi:", penyakit)
