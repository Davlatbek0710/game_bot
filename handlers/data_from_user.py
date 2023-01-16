from loader import dp
from aiogram import types
from aiogram.dispatcher import FSMContext
from state.user_data import UserInfo
import time
from loader import bot


@dp.message_handler(text='Данные Гражданина P.Узбекистана', state=None
                    )
async def data(message: types.Message):
    await bot.send_message(chat_id=f'{message.from_user.id}', text='Для проверки вашего гражданства в Республике Узбекистан требуются ввести нижеприведенные данные✍🏻\nИмя:\nФамилия:\nНомер тел📱:\nПаспорт №:')
    time.sleep(5)
    await UserInfo.f_name.set()
    await bot.send_message(chat_id=f'{message.from_user.id}', text='Сейчас введите ваше имя')
    await UserInfo.next()


@dp.message_handler(state=UserInfo.l_name)
async def data(message: types.Message, state: FSMContext):
    f_name = message.text
    async with state.proxy() as data_citizen:
        data_citizen['f_name'] = f_name.capitalize()
    time.sleep(1)
    await bot.send_message(chat_id=f'{message.from_user.id}', text='Введите вашу фамилию!')
    await UserInfo.next()


@dp.message_handler(state=UserInfo.phone_number)
async def data(message: types.Message, state: FSMContext):
    l_name = message.text
    async with state.proxy() as data_citizen:
        data_citizen['l_name'] = l_name.capitalize()
    time.sleep(1)
    await bot.send_message(chat_id=f'{message.from_user.id}', text='Введите ваш телефоный номер!')
    await UserInfo.next()


@dp.message_handler(state=UserInfo.passport_id)
async def data(message: types.Message, state: FSMContext):
    phone = message.text
    async with state.proxy() as data_citizen:
        data_citizen['phone_number'] = phone
    time.sleep(1)
    await UserInfo.next()
    await bot.send_message(chat_id=f'{message.from_user.id}', text='Введите номер паспорта!')


@dp.message_handler()
async def data(message: types.Message, state: FSMContext):
    p_num = message.text
    async with state.proxy() as data_citizen:
        data_citizen['passport_id'] = p_num
    time.sleep(2)
    await state.finish()
    await message.answer(f'Вы Прошли тест на гражданство Р.Узбекистан\n'
                         f'Ваши данные были удачно сохранены!\n'
                         f'Имя: {data_citizen["f_name"]}\nФамилия: {data_citizen["l_name"]}\n'
                         f'Номер тел📱: {data_citizen["phone_number"]}\nПаспорт №: {data_citizen["passport_id"]}')


