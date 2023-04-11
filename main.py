import os
from dotenv import load_dotenv
load_dotenv()




if __name__ == "__main__":        
    import fetch_spacex_images
    import fetch_nasa_apod_images
    import fetch_nasa_epic_images

    print("Качаем фото из spacex_last_launch")
    fetch_spacex_images.fetch_spacex_last_launch()
    print("Качаем фото из NASA APOD")
    fetch_nasa_apod_images.fetch_nasa(20)
    print("Качаем фото из NASA EPIC")
    fetch_nasa_epic_images.fetch_nasa_epic()

    #formatprint = pprint.PrettyPrinter()
    #formatprint.pprint(photos)
    print("Всё сделано")