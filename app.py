from loader import dp
from aiogram import executor
from utils.notify_admins import on_startup_notify
from utils.set_defualt_commands import set_default_commands
from handlers import cmd_start


async def on_startup(dispatcher):
    await on_startup_notify(dispatcher)

    await set_default_commands(dispatcher)


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)
