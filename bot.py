import telegram
import os
from dotenv import load_dotenv
load_dotenv()
import telegram
# Устанавливаем токен вашего бота
TOKEN = os.environ['token']
chat_id="@Photos4space"

bot = telegram.Bot(token = TOKEN)

# {'is_bot': True, 'supports_inline_queries': False, 'can_join_groups': True, 'username': 'Photos4spaceBot','id': 6035860865, 'first_name': 'Photos4space', 'can_read_all_group_messages': False}

# bot.send_message(text='Hi John!', chat_id=chat_id)

# media_1 = telegram.InputMediaPhoto(media=open('images\spacex_1.jpg', 'rb'))
# bot.send_media_group(chat_id=chat_id, media=[media_1, ])

bot.send_photo(chat_id=chat_id, photo=open('images\spacex_1.jpg', 'rb'))