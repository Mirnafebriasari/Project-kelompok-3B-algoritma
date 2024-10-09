from PIL import Image, ImageDraw, ImageFont

def tambahkan_teks(input_path,output_path,teks,left,top,nama_font,font_size,warna_font):
    """
    Menambahkan teks pada gambar sesuai koordinat yang diberikan pengguna
     
    Args:
        input_path (str): Jalur gambar dari folder
        output_path (str): jalur gambar yang akan disimpan
        teks (str): Teks yang akan ditambahkan
        left: Koordinat penempatan teks dari kiri
        top: Koordinat penampatan teks dari atas
        nama_font (str): Nama font yang akan digunakan
        font_size: Ukuran font yang akan digunakan
        warna_font: Warna font yang akan digunakan"""
    # Membuka file gambar
    input_path = Image.open(input_path)
    # Menentukan posisi teks
    posisi = (left, top)
    # Mengolah gambar
    gambar = ImageDraw.Draw(input_path)
    # Mengolah nama font dan ukuran teks
    font = ImageFont.truetype(nama_font, font_size)
    # Menempatkan posisi dan warna teks
    gambar.text(posisi, teks, fill=warna_font, font=font)
    input_path.save(output_path) # Menyimpan hasil di output
    input_path.show(output_path) # Menunjukkan hasil gambar yang telah ditambahkan teks

#help(tambahkan_teks)

#tambahkan_teks(
  #  "C:\\Users\\aisyah salsabila\Downloads\jay.jpg", # Buat backslash (\) menjadi double backslash (\\) agar path gambar dapat terbaca
  #  "C:\\Users\\aisyah salsabila\Downloads\jaii.jpg", # Buat backslash (\) menjadi double backslash (\\) agar path gambar dapat terbaca
#"apaa", #Tambahkan teks string
#200,300, # Masukkan koordinat teks
# "times.ttf", # font yang tersedia: "arial.ttf", "ALGER.TTF", "calibri.ttf", "cambriab.ttf", "times.ttf"
 #   100, # Masukkan ukuran font
 #   "red" # Masukkan warna font dalam bahasa inggris)
