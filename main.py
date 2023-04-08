import requests
import pathlib
import pprint
import os
from urllib.parse import urlparse
import datetime
from dotenv import load_dotenv
load_dotenv()


def get_file_extension(file_path):
    path, extension = os.path.splitext(urlparse(file_path).path)
    return extension


def image_downloader(filename,path,url,params=""):
    pathlib.Path(path).mkdir(parents=True, exist_ok=True) 
    response = requests.get(url,params=params)
    response.raise_for_status()
    with open(f"{path}/{filename}", 'wb') as file:
        file.write(response.content)

def fetch_spacex_last_launch():
    response = requests.get("https://api.spacexdata.com/v5/launches/")
    response.raise_for_status()
    launches=response.json()
    
    for launch in reversed(launches):
        if launch.get("links").get("flickr").get("original"):
            photos = launch.get("links").get("flickr").get("original")
            break
    
    for index, photo_url in enumerate(photos):
        image_downloader(f"spacex_{index}{get_file_extension(photo_url)}","images", photo_url)  



def fetch_nasa(count):
    payload = {"count": count,
               "api_key": os.environ['nasa_api_key']
              }
    response = requests.get("https://api.nasa.gov/planetary/apod",params=payload)
    response.raise_for_status()
    photos=response.json()
    

    for photo_number, photo_url in enumerate(photos):
        image_downloader(f"nasa_apod_{photo_number}{get_file_extension(photo_url.get('url'))}","images", photo_url.get("url"))
        



def fetch_nasa_epic():
    payload = {"api_key": os.environ['nasa_api_key']
              }
    response = requests.get("https://api.nasa.gov/EPIC/api/natural",params=payload)
    response.raise_for_status()
    photos=response.json()
    
    # formatprint = pprint.PrettyPrinter()
    # formatprint.pprint(photos)
    
    
    for photo_number, photo_url in enumerate(photos):
      
        datetime_obj = datetime.datetime.fromisoformat(photo_url.get('date'))

        # Форматирование даты в строку "гггг/мм/дд"
        formatted_date = datetime_obj.strftime('%Y/%m/%d')
        
       
        image_downloader(f"nasa_epic_{photo_number}.png","images",f"https://api.nasa.gov/EPIC/archive/natural/{formatted_date}/png/{ photo_url.get('image')}.png",payload)
        

fetch_spacex_last_launch()
fetch_nasa(10)
fetch_nasa_epic()


#formatprint = pprint.PrettyPrinter()
#formatprint.pprint(photos)



  

