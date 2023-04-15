import os
import pathlib
from urllib.parse import urlparse
import requests
from PIL import Image


def get_file_extension(url):
    """ Возвращает расширения файла, которыс качается по указанному URL.
    Args:
        url (str): url файла
    Returns:
        str: расширение переданного файла
    """
    return  os.path.splitext(urlparse(url).path)[1]


def download_image(filename,filepath,url,params=""):
    """Скачивает изображения по указанному URL.
    Args:
        filename (str): имя файла, которое присвоится скачанному файлу
        filepath (str): каталог в который будет записан файл
        url (str): URL для скачивания файла
        params: массив параметров Ключ : Значение, которые передадутся указанному URL
            например {"key1": key1, "key2": key2 } 
    """
    pathlib.Path(filepath).mkdir(parents=True, exist_ok=True) 
    response = requests.get(url,params=params)
    response.raise_for_status()
    with open(os.path.join(filepath,filename), "wb") as file:
        file.write(response.content)


def get_all_images(directory):
    """ Возвращает список изображений в указанном каталоге.
    Args:
        directory (str): каталог с изображениями
    Returns:
        список изображений
    """   
    image_files = []
    for filename in os.listdir(directory):
        if filename.endswith(".jpg") or filename.endswith(".jpeg") or filename.endswith(".png") or filename.endswith(".gif"):
            image_files.append(filename)
    return image_files


def compress_image(filepath, max_size_bytes):
    """Сжимает переданный файл изображения с использованием Pillow до указанного размера и записывает на место исходного.
    Args:
        filepath (str): Путь к файлу
        max_size_bytes (int): Максимальный размер файла
    """
    img = Image.open(filepath)
    img.save(filepath, optimize=True, quality=85)
    while os.path.getsize(filepath) > max_size_bytes:
        img = Image.open(filepath)
        img.save(filepath, optimize=True, quality=img.info["quality"] - 5)

