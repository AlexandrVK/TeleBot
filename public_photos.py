import os
import random
import argparse
import time
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

# Создание парсера аргументов командной строки
parser = argparse.ArgumentParser(description="Публикация изображений из каталога в произвольном порядке с заданным интервалом")
parser.add_argument("interval", type=int, nargs='?', default=14400, help="Интервал между публикациями в секундах")
args = parser.parse_args()



# Получаем список всех изображений в каталоге
image_files = get_all_images(images_directory)

# Перемешиваем список изображений
random.shuffle(image_files)

while True:
    for filename in image_files:
        image_file = os.path.join(images_directory, filename)
        # Проверяем размер изображения
        if get_image_size(image_file) > max_image_size_bytes:
            # Если размер изображения больше максимального, сжимаем его
            compress_image(image_file, max_image_size_bytes)
     
        # Публикуем изображение
        bot.send_photo(chat_id=CHAT_ID, photo=open(image_file, 'rb'))
        
        # Ожидаем указанный интервал времени
        time.sleep(args.interval)

    # Если изображения закончились, перемешиваем список изображений
    random.shuffle(image_files)
