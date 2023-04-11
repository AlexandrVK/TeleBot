# Space Telegram

A set of scripts is designed to automatically collect photos of space and publish them in Telegram

### How to install

Python3 should already be installed. 
Then use `pip` (or `pip3`, there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```
For the scripts to work, you need to fill in the following environment variables:
1. Register on site `https://api.nasa.gov`, get the API Key and assign the variable `nasa_api_key`
2. Register a Telegram bot and assign the received token to the `token` variable
3. Register the Telegram channel, make the bot its administrator and assign the chat id to the `chat_id` variable

### Usage

The set of scripts includes the following modules:
- `fetch_spacex_images.py ` Saving photos from the SpaceX website from the last or selected launch. Optional parameter: Startup ID.  
```python
py fetch_spacex_images.py 5eb87d47ffd86e000604b38a
```    
- `fetch_nasa_epic_images.py ` Downloads an EPIC photo from NASA.
```python
py fetch_nasa_epic_images.py
``` 
- `fetch_nasa_apod_images.py ` Downloads APOD photos from NASA (1 pc by default). Optional parameter: Number of photos. 
```python
py fetch_nasa_apod_images.py 10
``` 
- `public_photos.py ` Publishes all photos from the directory in an infinite loop in any order with a specified interval in seconds. (by default, 4 hours is 14,400 seconds). The interval can be specified as a script startup parameter.
```python 
py public_photos.py 1000
``` 
- `public_random_photo.py ` Publishes the specified photo to the channel. If “which” is not specified, publishes a random photo. The name of the photo file can be specified as a script startup parameter.
```python
py public_random_photo.py spacex_0.jpg 
``` 
- `main.py ` A template that allows you to download photos from all sources at once with default parameters.
```python
py main.py
```
### Project Goals

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).