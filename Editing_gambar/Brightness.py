from PIL import Image, ImageEnhance
from IPython.display import display
import os

def adjust_brightness(image_path, output_path, level, show_image=True):
    """Mengubah kecerahan gambar berdasarkan level yang ditentukan.
    
    Args:
        image_path (str): Jalur gambar dari folder.
        output_path (str): Jalur gambar yang akan disimpan.
        level (float): Tingkat kecerahan yang diinginkan (angka antara 0.0 dan 2.0).
        show_image (bool): Menentukan apakah gambar hasil akan ditampilkan. Default adalah True.
    """
    
    # Cek apakah level adalah angka (float)
    if not isinstance(level, (int, float)):
        print("Level kecerahan harus berupa angka.")
        return

    factor = float(level)

    if factor < 0.0 or factor > 2.0:
        print("Level kecerahan tidak valid. Menggunakan kecerahan 'normal' (1.0).")
        factor = 1.0

    if not os.path.isfile(image_path):
        print(f"File gambar tidak ditemukan: {image_path}")
        return

    image = Image.open(image_path)
    enhancer = ImageEnhance.Brightness(image)
    brightened_image = enhancer.enhance(factor)

    brightened_image.save(output_path)
    print(f"File disimpan di: {output_path}")

    # Tampilkan gambar jika show_image adalah True
    if show_image:
        display(brightened_image)

# Contoh penggunaan
#adjust_brightness("/content/y.jpg", "/content/Brg.jpg", 0.4, show_image=True)

# Cek file yang ada
#!ls /content/
