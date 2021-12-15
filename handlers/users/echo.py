import datetime
import random

import requests
from aiogram import types, bot
from aiogram.dispatcher.filters import Text
from utils.db.db_functions import add_image_info

from keyboards.currency_keyboard import start_markup
from keyboards.admin_keyboard import main_admin_markup
from loader import dp, bot
from filters.general import IsAdmin
from aiogram.types import ReplyKeyboardRemove


@dp.message_handler(content_types=types.ContentTypes.PHOTO)
async def get_pic_info(message: types.Message):
    await message.photo[-1].download(destination_dir='D:\\lilfuckup_bot\\photos')
    # add_image_info(message.photo[-1])
    await message.answer('Pic')


@dp.message_handler(IsAdmin(), commands='admin')
async def start_admin_menu(message: types.Message):
    await message.answer('Добро пожаловать в админ меню', reply_markup=main_admin_markup())


@dp.message_handler(Text(equals=['Обновить контактную информацию', 'Отправить сообщение всем пользователям',
                                 'Получить лог-файл']))
async def admin_menu_actions(message: types.Message):
    await message.answer('Wow such admin much though guy', reply_markup=ReplyKeyboardRemove())


@dp.message_handler(Text(equals=['USD', 'EUR']))
async def choose_currency(message: types.Message):
    datetime.date.today().strftime('%d.%m.%Y')
    headers = {'Accept': '*/*', 'X-Requested-With': 'XMLHttpRequest', 'Accept-Encoding': 'gzip, deflate, br',
               'Accept-Language': 'ru-RU,ru;q=0.9'}
    response = requests.get(f"https://bank.gov.ua/ua/tables/exchangerates?date="
                            f"{datetime.date.today().strftime('%d.%m.%Y')}&period=daily", headers=headers)
    currencies = response.json().get('data')
    requested_currency = ''
    for item in currencies:
        if message.text in item.get('cc'):
            requested_currency = item.get('rate')

    await message.answer(f'Current course for {message.text} is {requested_currency} UAH',
                         reply_markup=ReplyKeyboardRemove())


@dp.message_handler(text='RUB')
async def check_currencies(message: types.Message):
    await bot.send_photo(message.chat.id, 'https://pbs.twimg.com/media/DgIayZ5X4AA7CQV.jpg',
                         reply_markup=ReplyKeyboardRemove())


@dp.message_handler(text='/currency')
async def check_currencies(message: types.Message):
    await message.answer(text='Choose your currency', reply_markup=start_markup())


@dp.message_handler(text='/meme')
async def memes_sender(message: types.ContentTypes.PHOTO):
    chat_id = message.chat.id
    response = requests.post('https://api.memes.com/api/trending/feed?page=1')
    meme_to_send = random.choice(response.json().get('posts'))
    photo = 'https://cdn.memes.com/' + meme_to_send.get('path')
    caption = meme_to_send.get('postText')
    await bot.send_photo(chat_id, photo, caption)


@dp.message_handler(state=None)
async def dick_handler(message: types.Message):
    text = message.text.split(' ')
    reply_message = 'хуе' + ' хуе'.join(text)
    await message.answer(reply_message)

# # Эхо хендлер, куда летят текстовые сообщения без указанного состояния
#
# @dp.message_handler(state=None)
# async def bot_echo(message: types.Message):
#     await message.answer(f"Эхо без состояния."
#                          f"Сообщение:\n"
#                          f"{message.text}")
#
#
# # Эхо хендлер, куда летят ВСЕ сообщения с указанным состоянием
# @dp.message_handler(state="*", content_types=types.ContentTypes.ANY)
# async def bot_echo_all(message: types.Message, state: FSMContext):
#     state = await state.get_state()
#     await message.answer(f"Эхо в состоянии <code>{state}</code>.\n"
#                          f"\nСодержание сообщения:\n"
#                          f"<code>{message}</code>")
