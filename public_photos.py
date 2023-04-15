import os
import random
import argparse
import time
from dotenv import load_dotenv
import telegram
from modules import get_all_images, compress_image

def main():
    
    load_dotenv()

    chat_id = os.environ["CHAT_ID"]

    bot = telegram.Bot(token = os.environ["TOKEN"])

  
    images_directory = "images"
   
    max_image_size_bytes = 20 * 1024 * 1024
    
    parser = argparse.ArgumentParser(description="Публикация изображений из каталога в произвольном порядке с заданным интервалом")
    parser.add_argument("interval", type=int, nargs="?", default=14400, help="Интервал между публикациями в секундах")
    args = parser.parse_args()
    
    filenames = get_all_images(images_directory)
    
    random.shuffle(filenames)

    while True:
        for filename in filenames:
            filepath = os.path.join(images_directory, filename)
            
            if os.path.getsize(filepath) > max_image_size_bytes:
                # Если размер изображения больше максимального, сжимаем его
                compress_image(filepath, max_image_size_bytes)
        
            

            
            with open(filepath, "rb") as file:
                bot.send_photo(chat_id=chat_id, photo=file)
                
            time.sleep(args.interval)
       
        random.shuffle(filenames)

if __name__ == "__main__":
    main()
