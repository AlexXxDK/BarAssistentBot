from aiogram.types import CallbackQuery
from aiogram.utils.markdown import hbold

from utils.connect import dp
from keyboards.back_list_syrups_keyboard import back_list_syrups_keyboard


@dp.callback_query(lambda callback: callback.data == 'сurrant')
async def currant_callback(callback: CallbackQuery):
    await callback.message.edit_text(
        text=f'''<u>{hbold('РЕЦЕПТ Сироп Смородина')}</u>
        Смородина - 600гр
        Cахар - 200гр
        Кипяток - 400гр\n
        {hbold('Метод приготовления:')}
        Все ингредиенты смешиваем в блендере и процеживаем\n
        (Потом тут будет видео рецепт пошагово)
        ''',
        reply_markup=back_list_syrups_keyboard,
        parse_mode='HTML'
    )