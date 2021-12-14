from aiogram import Dispatcher

from filters.general import IsAdmin


def setup(dp: Dispatcher):
    dp.filters_factory.bind(IsAdmin)
