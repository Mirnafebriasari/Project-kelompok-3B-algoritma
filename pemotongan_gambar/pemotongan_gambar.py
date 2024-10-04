from PIL import Image     

def ukuran_gambar(Input_path,Output_path,left,top,right,bottom):
    """
    Memotong gambar sesuai koordinat yang diberikan dan menyimpan hasilnya.
    
    Args:
        input_path (str): jalur gambar dari folder
        out_path (str): jalur gambar yang akan disimpan
        left,top: koordinat parameter pemotongan gambar bagian kiri atas
        right,bottom: koordinat parameter pemotongan gambar bagian kanan bawah"""
    try:
        image = Image.open(Input_path) # Membuka file gambar
        cropped_image = image.crop((left, top, right, bottom)) # Memotong gambar sesuai koordinat kiri atas dan kanan bawah sehingga terbentuk segii empat
        cropped_image.save(Output_path) # Menyimpan hasil di jalur output
        cropped_image.show() # Menunjukkan hasil gambar yang telah dipotong
        return f"Gambar berhasil dipotong dan disimpan di {Output_path}" # Akhir dari program
    except Exception as e:
        return f"Terjadi kesalahan: {e}"

help(ukuran_gambar)

ukuran_gambar(
              "C:\\Users\jpael\OneDrive\Pictures\Ignition Teaser.png", # Buat backslash (\) menjadi double backslash (\\) agar path gambar dapat terbaca
              "C:\\Users\jpael\OneDrive\Pictures\Ignition Teaser14.png", # Buat backslash (\) menjadi double backslash (\\) agar path gambar dapat terbaca
              0,0,100,100
)


