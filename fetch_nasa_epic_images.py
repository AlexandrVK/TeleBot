import requests
import os
import datetime
from dotenv import load_dotenv
import mymodule

 
def fetch_nasa_epic():
    load_dotenv()
    payload = {"api_key": os.environ['nasa_api_key']
              }
    response = requests.get("https://api.nasa.gov/EPIC/api/natural",params=payload)
    response.raise_for_status()
    photos=response.json()

    
    for photo_number, photo_url in enumerate(photos):
      
        datetime_obj = datetime.datetime.fromisoformat(photo_url.get('date'))

        # Форматирование даты в строку "гггг/мм/дд"
        formatted_date = datetime_obj.strftime('%Y/%m/%d')
       
       
        mymodule.image_downloader(f"nasa_epic_{photo_number}.png","images",f"https://api.nasa.gov/EPIC/archive/natural/{formatted_date}/png/{ photo_url.get('image')}.png",payload)
        
if __name__ == "__main__":    
    
    fetch_nasa_epic()        