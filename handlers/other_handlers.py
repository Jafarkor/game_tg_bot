from aiogram.types import Message
from lexicon.lexicon import LEXICON_RU
from aiogram import Router

router = Router()


@router.message()
async def send_echo(message: Message):
    await message.answer(LEXICON_RU['misunderstanding'])
