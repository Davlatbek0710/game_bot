from aiogram import types
from aiogram.dispatcher import FSMContext
from loader import dp
from keyboards.defualt.request_game import basket
import time
from state.basketgame import GameBasketState


@dp.callback_query_handler(text='basketball')
async def game(call: types.CallbackQuery, state: FSMContext):
    await GameBasketState.bot_turn.set()
    await call.message.answer("Мы начинаем игру в Баскетбол!\nЯ(бот) Начинаю первым!")
    time.sleep(1)
    bot_data = await call.message.answer_dice('🏀')
    time.sleep(4.56)
    bot_data = bot_data['dice']['value']
    async with state.proxy() as data:
        data['bot_data'] = bot_data
    await call.message.answer("Видишь Как я умею!\nТвой черед, бросай ты!", reply_markup=basket)
    await GameBasketState.next()


@dp.message_handler(state=GameBasketState.user_turn, content_types=types.ContentType.DICE)
async def user(message: types.Message, state: FSMContext):
    user_data = message['dice']['value']
    async with state.proxy() as data:
        data['user_data'] = user_data
    time.sleep(4.59)
    if data['bot_data'] == data['user_data']:
        await message.answer("Поздравляю с ничьей!😎")
    elif data['bot_data'] > data['user_data']:
        await message.answer("Я Победил тебя хаха!🥳")
    elif data['bot_data'] < data['user_data']:
        await message.answer("Чтож... Тебе повезло!😏, Поздраляю с победой!🥳")
    await state.finish()


