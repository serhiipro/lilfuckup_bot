from aiogram.types import ReplyKeyboardMarkup


def main_admin_markup():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ['Обновить контактную информацию', 'Отправить сообщение всем пользователям', 'Получить лог-файл']
    for button in buttons:
        markup.insert(button)

    return markup
