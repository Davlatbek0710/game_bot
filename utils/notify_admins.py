from data.config import ADMINS
from loader import bot
from aiogram import Dispatcher

# To add some user Admin IDs
# ADMINS.append('179125200')


async def on_startup_notify(dp: Dispatcher):
    for admin in ADMINS:
        await bot.send_message(admin, text='BOT WAS LAUNCHED')
