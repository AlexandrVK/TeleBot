import telegram
import os
from dotenv import load_dotenv
load_dotenv()
import telegram
# Устанавливаем токен вашего бота
TOKEN = os.environ['token']
# bot = telegram.Bot(token='TOKEN')
bot = telegram.Bot(token="6035860865:AAEih7uwKMkyzINQ_75OdTpum9Go3rXk9Kw")

# {'is_bot': True, 'supports_inline_queries': False, 'can_join_groups': True, 'username': 'Photos4spaceBot','id': 6035860865, 'first_name': 'Photos4space', 'can_read_all_group_messages': False}

bot.send_message(text='Hi John!', chat_id="@Photos4space")