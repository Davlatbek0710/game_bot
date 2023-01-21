from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

all_games = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton('🎲Dice', callback_data='dice'),
            InlineKeyboardButton('Soccer⚽️', callback_data='soccer')
        ],
        [
            InlineKeyboardButton('🎳Bowling', callback_data='bowling'),
            InlineKeyboardButton('Basketball🏀', callback_data='basketball')
        ],
        [
            InlineKeyboardButton('🎰Slot Machine', callback_data='slot_machine'),
            InlineKeyboardButton('Dart🎯', callback_data='dart')
        ]
    ]
)
