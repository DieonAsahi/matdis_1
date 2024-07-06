# Deskripsi:
# Sebuah perusahaan ingin memprediksi apakah seorang calon karyawan akan diterima berdasarkan beberapa atribut seperti pendidikan, pengalaman kerja, dan keterampilan.

# Pertanyaan:

# Kumpulkan data mengenai calon karyawan yang telah diterima dan ditolak.
# Buat pohon keputusan untuk memprediksi penerimaan calon karyawan berdasarkan data yang dikumpulkan.

# Data contoh
data = [
    {'Pendidikan': 'S1', 'Pengalaman': '2 tahun', 'Keterampilan': 'Python', 'Penerimaan': 'Diterima'},
    {'Pendidikan': 'S2', 'Pengalaman': '3 tahun', 'Keterampilan': 'Java', 'Penerimaan': 'Diterima'},
    {'Pendidikan': 'D3', 'Pengalaman': '1 tahun', 'Keterampilan': 'HTML', 'Penerimaan': 'Ditolak'},
    {'Pendidikan': 'S1', 'Pengalaman': '5 tahun', 'Keterampilan': 'Python', 'Penerimaan': 'Diterima'},
    {'Pendidikan': 'SMA', 'Pengalaman': '0 tahun', 'Keterampilan': 'CSS', 'Penerimaan': 'Ditolak'},
    {'Pendidikan': 'S2', 'Pengalaman': '2 tahun', 'Keterampilan': 'Java', 'Penerimaan': 'Diterima'},
    {'Pendidikan': 'S1', 'Pengalaman': '3 tahun', 'Keterampilan': 'C++', 'Penerimaan': 'Diterima'},
    {'Pendidikan': 'D3', 'Pengalaman': '4 tahun', 'Keterampilan': 'JavaScript', 'Penerimaan': 'Ditolak'}
]

# Mengonversi data kategorikal menjadi numerik
mapping = {
    'Pendidikan': {'SMA': 0, 'D3': 1, 'S1': 2, 'S2': 3},
    'Keterampilan': {'HTML': 0, 'CSS': 1, 'JavaScript': 2, 'Python': 3, 'Java': 4, 'C++': 5},
    'Penerimaan': {'Ditolak': 0, 'Diterima': 1}
}

# Fungsi untuk mengubah pengalaman menjadi angka
def pengalaman_to_num(pengalaman):
    if pengalaman.endswith(" tahun"):
        return int(pengalaman.split(" ")[0])
    return -1

# Fungsi untuk prediksi penerimaan karyawan (ini hanya contoh dummy)
def prediksi(input_data):
    # Implementasikan model prediksi di sini. Ini hanya contoh dummy.
    # Sebagai contoh, kita mengembalikan 1 (Diterima) jika pendidikan >= 2 dan pengalaman >= 2 dan keterampilan >= 3
    if input_data[0][0] >= 2 and input_data[0][1] >= 2 and input_data[0][2] >= 3:
        return [1]
    return [0]

# Fungsi untuk memprediksi penerimaan calon karyawan berdasarkan input pengguna
def prediksi_karyawan(pendidikan, pengalaman, keterampilan):
    pendidikan_num = mapping['Pendidikan'].get(pendidikan, -1)
    pengalaman_num = pengalaman_to_num(pengalaman)
    keterampilan_num = mapping['Keterampilan'].get(keterampilan, -1)
    
    if pendidikan_num == -1 or pengalaman_num == -1 or keterampilan_num == -1:
        return "Data input tidak valid."
    
    return 'Diterima' if prediksi([[pendidikan_num, pengalaman_num, keterampilan_num]])[0] == 1 else 'Ditolak'

# Mengambil input dari pengguna
pendidikan = input("Masukkan pendidikan (SMA, D3, S1, S2): ")
pengalaman = input("Masukkan pengalaman (misal: 2 tahun): ")
keterampilan = input("Masukkan keterampilan (HTML, CSS, JavaScript, Python, Java, C++): ")

# Prediksi penerimaan karyawan
penerimaan_karyawan = prediksi_karyawan(pendidikan, pengalaman, keterampilan)
print("Penerimaan Karyawan:", penerimaan_karyawan)

