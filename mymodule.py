import requests
import pathlib
import os
from PIL import Image
from urllib.parse import urlparse
from dotenv import load_dotenv
load_dotenv()

# Функция для получения расширения файла
def get_file_extension(file_path):
    path, extension = os.path.splitext(urlparse(file_path).path)
    return extension

# Функция для скачивания файлов 
def image_downloader(filename,path,url,params=""):
    pathlib.Path(path).mkdir(parents=True, exist_ok=True) 
    response = requests.get(url,params=params)
    response.raise_for_status()
    with open(f"{path}/{filename}", 'wb') as file:
        file.write(response.content)


# Функция для получения списка всех изображений в каталоге
def get_all_images(directory):
    image_files = []
    for filename in os.listdir(directory):
        if filename.endswith(".jpg") or filename.endswith(".jpeg") or filename.endswith(".png") or filename.endswith(".gif"):
            # image_files.append(os.path.join(directory, filename))
            image_files.append(filename)
    return image_files

# Функция для определения размера изображения в байтах
def get_image_size(image_path):
    with open(image_path, "rb") as f:
        return len(f.read())

# Функция для сжатия изображения с использованием Pillow
def compress_image(image_path, max_size_bytes):
    img = Image.open(image_path)
    # Сжатие изображения до указанного максимального размера
    img.save(image_path, optimize=True, quality=85)
    while get_image_size(image_path) > max_size_bytes:
        # Если изображение все еще больше максимального размера, уменьшаем качество
        img = Image.open(image_path)
        img.save(image_path, optimize=True, quality=img.info["quality"] - 5)

