import requests
import os
from dotenv import load_dotenv
from mymodule import image_downloader, get_file_extension


def fetch_nasa(count='1'):
    load_dotenv()
    payload = {"count": count,
               "api_key": os.environ['nasa_api_key']
              }
    response = requests.get("https://api.nasa.gov/planetary/apod",params=payload)
    response.raise_for_status()
    photos=response.json()
    

    for photo_number, photo_url in enumerate(photos):
        if photo_url:
            image_downloader(f"nasa_apod_{photo_number}{get_file_extension(photo_url.get('url'))}","images", photo_url.get("url"))
        
if __name__ == "__main__":    
    
    import argparse
    parser = argparse.ArgumentParser(description="Скачивание фотографий с сайта Nasa APOD ")
    parser.add_argument ('count', nargs='?', default=1, help="Количество фотографий (по умолчанию 1) ")
    args = parser.parse_args() 
    fetch_nasa(args.count)
