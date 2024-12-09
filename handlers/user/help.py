from aiogram.filters import Command
from aiogram.types import Message
from utils.connect import dp


@dp.message(Command(commands=["hl", "help"]))
async def command_start_handler(message: Message) -> None:
    await message.answer(
        text='Нужна помощь?\n'
             'Вот список команд которые я исполняю:\n'
             '/start\n'
             '/help'
    )