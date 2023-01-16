from aiogram.dispatcher.filters.state import State, StatesGroup


class GameBasketState(StatesGroup):
    bot_turn = State()
    user_turn = State()
