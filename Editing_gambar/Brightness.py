from PIL import Image, ImageEnhance
import os

def adjust_brightness(image_path, output_path, level):
    """Mengubah kecerahan gambar berdasarkan level yang ditentukan.
    Args:
        image_path (str): Jalur gambar dari folder.
        output_path (str): Jalur gambar yang akan disimpan.
        level (float): Tingkat kecerahan yang diinginkan (angka antara 0.0 dan 2.0)."""

    # Cek apakah level adalah angka (float)
    if not isinstance(level, (int, float)):
        print("Level kecerahan harus berupa angka.")
        return

    # Mengkonversi level menjadi float
    factor = float(level)

    # Menambahkan peringatan jika level tidak valid
    if factor < 0.0 or factor > 2.0:
        print("Level kecerahan tidak valid. Harus antara 0.0 dan 2.0. Menggunakan kecerahan 'normal' (1.0).")
        factor = 1.0  # Default ke 'normal' jika level tidak valid

    # Cek apakah file gambar ada
    if not os.path.isfile(image_path):
        print(f"File gambar tidak ditemukan: {image_path}")
        return

    image = Image.open(image_path)  # Membuka file gambar
    enhancer = ImageEnhance.Brightness(image)  # Menggunakan fungsi pencerahan dari Pillow
    brightened_image = enhancer.enhance(factor)  # Menentukan skala kecerahan gambar

    # Memeriksa apakah jalur output sudah ada
    if os.path.isfile(output_path):
        overwrite = input(f"File sudah ada di {output_path}. Apakah Anda ingin menimpa? (y/n): ")
        if overwrite.lower() != 'y':
            print("Proses dibatalkan.")
            return

#help(adjust_brightness)

#adjust_brightness(
 #   "C:\\Users\\Asus\\Documents\\y.jpg", # Buat backslash (\) menjadi double backslash (\\) agar path gambar dapat terbaca
  #  "C:\\Users\\Asus\\Documents\\dkk.jpg", # Buat backslash (\) menjadi double backslash (\\) agar path gambar dapat terbaca
   # "sangattt gelap" # Pilihan level yang tersedia: sangat gelap, gelap, normal, cerah, sangat cerah)
