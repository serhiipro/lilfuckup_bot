from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Запустить бота"),
            types.BotCommand("meme", "Random meme"),
            types.BotCommand("currency", "Get currency"),
            types.BotCommand("help", "Вывести справку"),
        ]
    )


async def clear_all_commands(dp):
    await dp.bot.set_my_commands([])
