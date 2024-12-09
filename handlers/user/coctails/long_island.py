from aiogram.types import CallbackQuery
from aiogram.utils.markdown import hbold

from utils.connect import dp
from keyboards.back_list_main_keyboard import back_list_main_keyboard


@dp.callback_query(lambda callback: callback.data == 'long_island')
async def long_island_callback(callback: CallbackQuery):
    await callback.message.edit_text(
        text=f'''<u>{hbold('РЕЦЕПТ Long Island')}</u>
        Водка - 20мл
        Джин - 20мл
        Текила - 20мл
        Ром - 20мл
        Лимонный фреш -20мл
        Кола - 100мл\n
        {hbold('Метод приготовления:')}
        Шейк. Все ингредиенты(кроме коллы) залить в шейкер - шейковать на протяжении 7сек - в охлажденный хайбол (наполненный льдом) налить коллу 100мл - затем перелить содержимое шейкера
        {hbold('Бокал подачи:')} Охлажденный Хайбол\n
        (Потом тут будет видео рецепт пошагово)
        ''',
        reply_markup=back_list_main_keyboard,
        parse_mode='HTML'
    )