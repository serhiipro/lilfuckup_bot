from aiogram import executor, types
from loader import dp
import middlewares, filters, handlers
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands, clear_all_commands


@dp.message_handler()
async def get_message(message: types.Message):
    chat_id = message.chat.id

    await dp.bot.get_updates()


async def on_startup(dispatcher):
    import filters
    filters.setup(dp)

    await on_startup_notify(dp)
    await clear_all_commands(dp)
    await set_default_commands(dp)


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)

