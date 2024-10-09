from PIL import Image
import os

def convert_to_grayscale(input_image_path, output_image_path):
    """
    Mengonversi gambar menjadi grayscale dan menyimpannya ke lokasi output.

    input_image_path (str): Jalur gambar dari folder.
    output_image_path (str): Jalur gambar yang akan disimpan.
    """
    # Memeriksa apakah path input gambar valid
    if not os.path.exists(input_image_path):
        print(f"Error: File '{input_image_path}' tidak ditemukan.")
        return

    try:
        # Membuka gambar dari path input
        image = Image.open(input_image_path)
        
        # Mengonversi gambar ke grayscale
        grayscale_image = image.convert('L')
        
        # Menyimpan gambar grayscale ke path output
        grayscale_image.save(output_image_path)
        print(f"Gambar grayscale berhasil disimpan di: {output_image_path}")

    except Exception as e:
        # Menampilkan pesan kesalahan jika terjadi masalah
        print(f"Terjadi kesalahan: {e}")

help(convert_to_grayscale)

#convert_to_grayscale(
#   "C:\Users\ASUS\Documents\GrayscaleConverter\gambar_input.jpg",
#  "C:\Users\ASUS\Documents\GrayscaleConverter\gambar_output.jpg",
#)
