from aiogram.types import ReplyKeyboardMarkup


def start_markup():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = [['USD', 'EUR'], ['RUB']]
    for button in buttons:
        markup.add(*button)
    return markup
