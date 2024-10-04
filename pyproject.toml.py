[build-system]
requires = ["setuptools>=42", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "Editing_gambar"  # Nama proyek sebaiknya tidak mengandung spasi
version = "0.1.0"
description = "Paket Python untuk pengolahan gambar"
authors = ["Mirna <email@mirnhafebriasari.com>"]
license = "MIT"
readme = "README.md"
homepage = "https://github.com/Mirnafebriasari/Project-kelompok-3B-algoritma"
repository = "https://github.com/Mirnafebriasari/Project-kelompok-3B-algoritma"
keywords = ["gambar", "pengolahan", "python"]

[project.dependencies]
numpy = "^1.21"
Pillow = "^8.0"

[tool.setuptools.packages.find]
where = ["Editing_gambar"]  # Pastikan direktori ini ada di struktur paket Anda
