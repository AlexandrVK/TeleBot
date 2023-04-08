import requests
from mymodule import *



def enumerate_photos(photos):
    for index, photo_url in enumerate(photos):
        image_downloader(f"spacex_{index}{get_file_extension(photo_url)}","images", photo_url)  
    

def fetch_spacex_launch(id):
    response = requests.get(f"https://api.spacexdata.com/v5/launches/{id}")
    response.raise_for_status()
    launch=response.json()
    photos = launch.get("links").get("flickr").get("original")
    
    enumerate_photos(photos)
    



def fetch_spacex_last_launch():
    
    response = requests.get("https://api.spacexdata.com/v5/launches/")
    response.raise_for_status()
    launches=response.json()
    
    for launch in reversed(launches):
        if launch.get("links").get("flickr").get("original"):
            photos = launch.get("links").get("flickr").get("original")
            break

    enumerate_photos(photos)
    


if __name__ == "__main__":    
    
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument ('id', nargs='?', default='')
    args = parser.parse_args() 
    if args.id:
        fetch_spacex_launch(args.id)
    else:
        fetch_spacex_last_launch()         