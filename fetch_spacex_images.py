import requests
from modules import download_image, get_file_extension
import argparse


def fetch_spacex_launch(id):
    response = requests.get(f"https://api.spacexdata.com/v5/launches/{id}")
    response.raise_for_status()
    launch=response.json()
    photos = launch.get("links").get("flickr").get("original")
    
    for index, photo_url in enumerate(photos):
        download_image(f"spacex_{index}{get_file_extension(photo_url)}","images", photo_url)  

def fetch_spacex_last_launch():
    
    response = requests.get("https://api.spacexdata.com/v5/launches/")
    response.raise_for_status()
    launches=response.json()
    
    for launch in reversed(launches):
        if launch.get("links").get("flickr").get("original"):
            photos = launch.get("links").get("flickr").get("original")
            break

    for index, photo_url in enumerate(photos):
        download_image(f"spacex_{index}{get_file_extension(photo_url)}","images", photo_url)  
 
    


def main():   
    parser = argparse.ArgumentParser(description="Сохранение фотографий с сайта SpaceX с последнего или выбраного запуска")
    parser.add_argument ("id", nargs="?", default="",help="ID запуска")
    args = parser.parse_args() 
    if args.id:
        fetch_spacex_launch(args.id)
    else:
        fetch_spacex_last_launch()         

if __name__ == "__main__":
    main()        