from aiogram.dispatcher.filters.state import State, StatesGroup


class UserInfo(StatesGroup):
    f_name = State()
    l_name = State()
    phone_number = State()
    passport_id = State()
