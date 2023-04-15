import os
import random
import argparse
from dotenv import load_dotenv
import telegram
from modules import get_all_images,compress_image

def main():

    load_dotenv()

    chat_id = os.environ["CHAT_ID"]

    bot = telegram.Bot(token = os.environ["TOKEN"])

    
    images_directory = "images"
    
    max_image_size_bytes = 20 * 1024 * 1024


    image_files = get_all_images(images_directory)

    random.shuffle(image_files)

    parser = argparse.ArgumentParser(description="Публикация случайного или выбраного изображеня из каталога")
    parser.add_argument("filename", nargs="?", default=os.path.basename(image_files[0]), help="Имя публикуемого файла ")
    args = parser.parse_args()



    if args.filename in image_files:
        filepath = os.path.join(images_directory, args.filename)
        if os.path.getsize(filepath) > max_image_size_bytes:
            compress_image(filepath, max_image_size_bytes)

        with open(filepath, "rb") as file:
            bot.send_photo(chat_id=chat_id, photo=file)

if __name__ == "__main__":
    main()


