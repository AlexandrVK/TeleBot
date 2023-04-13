import requests
import os
from dotenv import load_dotenv
from my_modules import download_image, get_file_extension
import argparse


def fetch_nasa(api_key,count='1'):
   
    payload = {"count": count,
               "api_key": api_key
              }
    response = requests.get("https://api.nasa.gov/planetary/apod",params=payload)
    response.raise_for_status()
    photos=response.json()
    

    for photo_number, photo_url in enumerate(photos):
        if photo_url:
            filename = f"nasa_apod_{photo_number}{get_file_extension(photo_url.get('url'))}"
            download_image(filename,"images", photo_url.get("url"))
        
def main():  
    load_dotenv()
    api_key =  os.environ['NASA_API_KEY']
    parser = argparse.ArgumentParser(description="Скачивание фотографий с сайта Nasa APOD ")
    parser.add_argument ('count', nargs='?', default=1, help="Количество фотографий (по умолчанию 1) ")
    args = parser.parse_args() 
    fetch_nasa(api_key, args.count)

if __name__ == '__main__':
    main()