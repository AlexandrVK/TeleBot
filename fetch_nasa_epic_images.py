import requests
import os
import datetime
from dotenv import load_dotenv
from my_modules import download_image


 
def fetch_nasa_epic(api_key):

    payload = {"api_key": api_key}
    response = requests.get("https://api.nasa.gov/EPIC/api/natural",params=payload)
    response.raise_for_status()
    photos=response.json()

    
    for photo_number, photo_url in enumerate(photos):
      
        datetime_obj = datetime.datetime.fromisoformat(photo_url.get('date'))
        formatted_date = datetime_obj.strftime('%Y/%m/%d')
     
        url = f"https://api.nasa.gov/EPIC/archive/natural/{formatted_date}/png/{ photo_url.get('image')}.png"
        download_image(f"nasa_epic_{photo_number}.png","images",url,payload)
        
def main(): 
    load_dotenv()
    api_key =  os.environ['NASA_API_KEY']
    fetch_nasa_epic(api_key)        


if __name__ == '__main__':
    main()     