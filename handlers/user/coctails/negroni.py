from aiogram.types import CallbackQuery
from aiogram.utils.markdown import hbold

from utils.connect import dp
from keyboards.back_list_main_keyboard import back_list_main_keyboard


@dp.callback_query(lambda callback: callback.data == 'negroni')
async def negroni_callback(callback: CallbackQuery):
    await callback.message.edit_text(
        text=f'''<u>{hbold('РЕЦЕПТ Негрони')}</u>
        Кампари - 25мл
        Джин - 25мл
        Красный вермут - 25мл\n
        {hbold('Метод приготовления:')}
        Стир. Все ингредиенты залить в смесительный бокал - перемешать
        {hbold('Бокал подачи:')} Охлажденный Олд Фэшн\n
        (Потом тут будет видео рецепт пошагово)
        ''',
        reply_markup=back_list_main_keyboard,
        parse_mode='HTML'
    )