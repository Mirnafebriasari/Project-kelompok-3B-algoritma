from PIL import Image, ImageEnhance
import os

def adjust_brightness(image_path, output_path, level):
    """Mengubah kecerahan gambar berdasarkan level yang ditentukan.
    args:
        image_path (str): Jalur gambar dari folder.
        output_path (str): Jalur gambar yang akan disimpan.
        level (float or str): Tingkat kecerahan yang diinginkan (angka atau string)."""
    
    # Faktor kecerahan berdasarkan level yang ditentukan
    brightness_factors = {
        'sangat gelap': 0.2,
        'gelap': 0.5,
        'normal': 1.0,
        'cerah': 1.5,
        'sangat cerah': 2.0
    }
    
    # Cek apakah level adalah angka (float)
    if isinstance(level, (int, float)):
        factor = float(level)
    else:
        # Mendapatkan faktor kecerahan dari level yang diberikan
        factor = brightness_factors.get(level.lower(), None)

    # Menambahkan peringatan jika level tidak valid
    if factor is None or factor < 0.0 or factor > 2.0:
        print("Level kecerahan tidak dikenali atau tidak valid. Menggunakan kecerahan 'normal' (1.0).")
        factor = 1.0  # Default ke 'normal' jika level tidak valid

    # Cek apakah file gambar ada
    if not os.path.isfile(image_path):
        print(f"File gambar tidak ditemukan: {image_path}")
        return

    image = Image.open(image_path)  # Membuka file gambar
    enhancer = ImageEnhance.Brightness(image)  # Menggunakan fungsi pencerahan dari Pillow
    brightened_image = enhancer.enhance(factor)  # Menentukan skala kecerahan gambar
    brightened_image.save(output_path)  # Menyimpan hasil di jalur output
    brightened_image.show()  # Menunjukkan hasil pencerahan gambar

#help(adjust_brightness)

#adjust_brightness(
 #   "C:\\Users\\Asus\\Documents\\y.jpg", # Buat backslash (\) menjadi double backslash (\\) agar path gambar dapat terbaca
  #  "C:\\Users\\Asus\\Documents\\dkk.jpg", # Buat backslash (\) menjadi double backslash (\\) agar path gambar dapat terbaca
   # "sangattt gelap" # Pilihan level yang tersedia: sangat gelap, gelap, normal, cerah, sangat cerah)
