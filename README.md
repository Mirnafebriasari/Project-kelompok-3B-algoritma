"# Project-kelompok-3B-algoritma" 
pip install .

#cara penggunaan
from motipy import adjust_brightness
from PIL import Image

# Memuat gambar
image = Image.open('path/to/image.jpg')

# Menyesuaikan kecerahan
bright_image = adjust_brightness(image, factor=1.5)

# Menyimpan gambar hasil
bright_image.save('path/to/bright_image.jpg')



### Penjelasan Singkat:
- **Judul**: Nama proyek.
- **Deskripsi**: Apa itu Motipy.
- **Fitur**: Fitur utama dari paket.
- **Instalasi**: Cara menginstal paket.
- **Penggunaan**: Contoh kode untuk menggunakan paket.
- **Dependensi**: Daftar dependensi yang diperlukan.
- **Kontribusi**: Mengundang orang lain untuk berkontribusi.
- **Lisensi**: Informasi tentang lisensi.
- **Kontak**: Cara menghubungi jika ada pertanyaan.
