from aiogram.dispatcher.filters.state import StatesGroup, State


class CurrencyStates(StatesGroup):
    choose_currency = State()