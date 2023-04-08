import requests
import pathlib
import os
from urllib.parse import urlparse
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



