from PIL import Image, ImageOps

def flip_image(image_path, output_path, direction):
    """
    Membalik gambar berdasarkan arah yang ditentukan dan menyimpannya ke lokasi output

    Parameter:
    image_path(str):
        Lokasi file gambar yang akan dibalik. Pastikan menggunakan double backslashes (\\)
        
    output_path(str):
        Lokasi file tempat gambar yang akan disimpan. Pastikan menggunakan double backslashes (\\)

    direction(str):
         Arah pemantulan gambar dapat berupa:
            -'horizontal': untuk membalik gambar secara horizontal
            -'vertikal': untuk membalik gambar secara vertikal.

            Raises:
            ValueError:
                Jika arah yang dimasukkan bukan 'horizontal' atau 'vertikal'

            Exception:
                Menangkap kesalahan lain yang mungkin terjadi selama proses membuka, membalik, atau menyimpan gambar.
    """
    try:
        # Open the image
        image = Image.open(image_path)

        # Flip the image based on the direction
        if direction.lower() == 'horizontal': 
            flipped_image = ImageOps.mirror(image)
        elif direction.lower() == 'vertikal':
            flipped_image = ImageOps.flip(image)
        else: 
            raise ValueError("Arah yang dimasukkan harus 'horizontal' atau 'vertikal'.")

        # Save the flipped image
        flipped_image.save(output_path)
        print(f"Gambar berhasil dipantulkan dan disimpan di: {output_path}")
        flipped_image.show()
    except Exception as e:
        return(f"Terjadi kesalahan: {e}")
    
help(flip_image)

flip_image(
    "C:\Users\LENOVO\Downloads\keindaahan alam semesta.jpg",
    "C:\Users\LENOVO\Downloads\Ignition Teaser14.jpg",  
    "vertikal"  
)