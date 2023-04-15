from dotenv import load_dotenv
import fetch_spacex_images
import fetch_nasa_apod_images
import fetch_nasa_epic_images
import os    




def main():

    load_dotenv()
    api_key =  os.environ["NASA_API_KEY"]
    print("Качаем фото из spacex_last_launch")
    fetch_spacex_images.fetch_spacex_last_launch()
    print("Качаем фото из NASA APOD")
    fetch_nasa_apod_images.fetch_nasa(api_key,20)
    print("Качаем фото из NASA EPIC")
    fetch_nasa_epic_images.fetch_nasa_epic(api_key)

   

    print("Всё сделано")

if __name__ == "__main__":
    main()
