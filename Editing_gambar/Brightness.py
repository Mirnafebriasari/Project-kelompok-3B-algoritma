from PIL import Image, ImageEnhance
import os

def adjust_brightness(image_path, output_path, level):
    """Mengubah kecerahan gambar berdasarkan level yang ditentukan.
    args:
        image_path (str): Jalur gambar dari folder.
        output_path (str): Jalur gambar yang akan disimpan.
        level (float): Tingkat kecerahan yang diinginkan (0.0 hingga 2.0)."""
    
    # Cek apakah level berada dalam rentang yang valid
    if level < 0.0 or level > 2.0:
        print("Level kecerahan harus antara 0.0 (sangat gelap) dan 2.0 (sangat cerah). Menggunakan kecerahan 'normal' (1.0).")
        level = 1.0  # Default ke 'normal' jika level tidak valid

    # Cek apakah file gambar ada
    if not os.path.isfile(image_path):
        print(f"File gambar tidak ditemukan: {image_path}")
        return

    image = Image.open(image_path)  # Membuka file gambar
    enhancer = ImageEnhance.Brightness(image)  # Menggunakan fungsi pencerahan dari Pillow
    brightened_image = enhancer.enhance(level)  # Menentukan skala kecerahan gambar
    brightened_image.save(output_path)  # Menyimpan hasil di jalur output
    brightened_image.show()  # Menunjukkan hasil pencerahan gambar


#help(adjust_brightness)

#adjust_brightness(
 #   "C:\\Users\\Asus\\Documents\\y.jpg", # Buat backslash (\) menjadi double backslash (\\) agar path gambar dapat terbaca
  #  "C:\\Users\\Asus\\Documents\\dkk.jpg", # Buat backslash (\) menjadi double backslash (\\) agar path gambar dapat terbaca
   # "sangattt gelap" # Pilihan level yang tersedia: sangat gelap, gelap, normal, cerah, sangat cerah)
