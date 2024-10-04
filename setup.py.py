from setuptools import setup, find_packages

setup(
    name='Editing_gambar',
    version='0.1.0',
    author='Mirna',
    author_email='email@mirnhafebriasari.com',
    description='Paket Python untuk pengolahan gambar',
    long_description=open('README.md').read(),  # Membaca isi README.md untuk deskripsi yang lebih panjang
    long_description_content_type='text/markdown',  # Tipe konten README
    url='https://github.com/Mirnafebriasari/Project-kelompok-3B-algoritma',
    license='MIT',
    packages=find_packages(),  # Menemukan semua paket yang ada
    install_requires=[
        'numpy>=1.21',  # Versi minimal numpy
        'Pillow>=8.0',   # Versi minimal Pillow
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7',  # Versi Python yang dibutuhkan
)
