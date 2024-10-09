from PIL import Image, ImageEnhance
import os

def adjust_brightness(image_path, output_path, level):
    """Mengubah kecerahan gambar berdasarkan level yang ditentukan.
    
    Args:
        image_path (str): Jalur gambar dari folder.
        output_path (str): Jalur gambar yang akan disimpan.
        level (float): Tingkat kecerahan yang diinginkan (angka antara 0.0 dan 2.0).
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

   

