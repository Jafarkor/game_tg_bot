from aiogram.types import KeyboardButton, Message, ReplyKeyboardMarkup, ReplyKeyboardRemove

button_1 = KeyboardButton(text='Давай!')
button_2 = KeyboardButton(text='Не хочу!')
start_keyboard = ReplyKeyboardMarkup(keyboard=[[button_1, button_2]],
                                     resize_keyboard=True,
                                     one_time_keyboard=True)

stone_button = KeyboardButton(text='🪨')
scissors_button = KeyboardButton(text='✂️')
paper_button = KeyboardButton(text='📄')
playing_keyboard = ReplyKeyboardMarkup(keyboard=[[stone_button, scissors_button, paper_button]],
                                       resize_keyboard=True)
