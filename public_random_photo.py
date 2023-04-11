import os
import random
import argparse
from dotenv import load_dotenv
import telegram
from mymodule import get_all_images,get_image_size,compress_image

load_dotenv()

# Устанавливаем токен бота
TOKEN = os.environ['token']
CHAT_ID = os.environ['chat_id']

bot = telegram.Bot(token = TOKEN)

# Путь к каталогу с изображениями
images_directory = "images"
# Максимальный размер изображения в байтах (20 MB)
max_image_size_bytes = 20 * 1024 * 1024


# Получаем список всех изображений в каталоге
image_files = get_all_images(images_directory)

# Перемешиваем список изображений
random.shuffle(image_files)

# Создание парсера аргументов командной строки
parser = argparse.ArgumentParser(description="Публикация случайного или выбраного изображеня из каталога")
parser.add_argument("filename", nargs='?', default=os.path.basename(image_files[0]), help="Имя публикуемого файла ")
args = parser.parse_args()



if args.filename in image_files:
    image_file = os.path.join(images_directory, args.filename)
    # Проверяем размер изображения
    if get_image_size(image_file) > max_image_size_bytes:
        # Если размер изображения больше максимального, сжимаем его
        compress_image(image_file, max_image_size_bytes)

    # Публикуем изображение
    bot.send_photo(chat_id=CHAT_ID, photo=open(image_file, 'rb'))
else:
    print("Невозможно опубликовать -  нет такого файла")


