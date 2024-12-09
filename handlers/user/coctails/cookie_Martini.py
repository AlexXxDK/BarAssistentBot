from aiogram.client import bot
from aiogram.methods import SendAnimation
from aiogram.types import CallbackQuery
from aiogram.utils.markdown import hbold

from utils.connect import dp
from keyboards.back_list_main_keyboard import back_list_main_keyboard
from aiogram.utils.markdown import hide_link


@dp.callback_query(lambda callback: callback.data == 'cookie_Martini')
async def cookie_callback(callback: CallbackQuery):
    photo = open('handlers/user/flower-5201_256.gif')
    await callback.message.edit_text(
        text=f'''<u>{hbold('РЕЦЕПТ Cookie Martini')}</u>
        Водка - 50мл
        Кофе эспрессо - 10гр
        Сироп Шоколадное Печенье - 25мл\n
        {hbold('Метод приготовления:')}
        Все ингредиенты влить в шейкер, шейкуем и переливаем в охлажденную шале
        {hbold('Бокал подачи:')} Шале\n
        (Потом тут будет видео рецепт пошагово)
        ''',
        reply_markup=back_list_main_keyboard,
        parse_mode='HTML'
    )