from aiogram.types import Message
from aiogram.filters import Command, CommandStart
from aiogram import Router, F

from lexicon.lexicon import LEXICON_RU
from keyboards.keyboards import start_keyboard, playing_keyboard
from servises.servises import bot_choise

router = Router()


@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text=LEXICON_RU['/start'].format(message.chat.first_name),
                         reply_markup=start_keyboard)


@router.message(Command(commands='help'))
async def process_help_command(message: Message):
    await message.answer(text=LEXICON_RU['/help'])


@router.message(F.text == 'Давай!')
async def procees_start_playing(message: Message):
    await message.answer(text=LEXICON_RU['start_playing'].format(message.chat.first_name),
                         reply_markup=playing_keyboard)


@router.message(F.text == 'Не хочу!')
async def procees_stop_playing(message: Message):
    await message.answer(text=LEXICON_RU['stop_playing'],
                         reply_markup=start_keyboard)


@router.message(F.text.in_({'🪨', '✂️', '📄'}))
async def procees_player_selected(message: Message):
    result = bot_choise(message.text)
    await message.answer(text=result[0])
    await message.answer(text=LEXICON_RU[result[1]].format(message.text, result[0]),
                         reply_markup=start_keyboard)