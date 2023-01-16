from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart, ChatTypeFilter
from loader import dp
from aiogram import bot
from keyboards.inline.game_menu import all_games


@dp.message_handler(CommandStart(), ChatTypeFilter(chat_type=types.ChatType.PRIVATE))
async def cmd_start_private(message: types.Message):
    await message.answer('Hello! Press the command - /game to start a game with bot!')


@dp.message_handler(CommandStart(), ChatTypeFilter(chat_type=types.ChatType.GROUP or types.ChatType.SUPERGROUP))
async def cmd_start_groups(message: types.Message):
    await message.reply(f'Hello {message.from_user.full_name} Press the command - /game to start a game with bot!')


@dp.message_handler(commands='game')
async def game(message: types.Message):
    await message.answer('-------Game Dice!-------\nChoose one to start!', reply_markup=all_games)

