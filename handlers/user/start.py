from aiogram import types
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram.utils.markdown import hbold

from keyboards.start_keyboard import start_keyboard
from utils.connect import dp


@dp.message(Command(commands=['start']))
async def command_start_handler(message: Message) -> None:
    await message.answer(
        text=f'Привет, {hbold(message.from_user.full_name)}!\n'
             f'С помощью этого бота ты сможешь найти нужный тебе рецептик или просмотреть меню бара!',
        reply_markup=start_keyboard
        )

