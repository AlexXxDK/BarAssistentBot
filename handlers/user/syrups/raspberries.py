from aiogram.types import CallbackQuery
from aiogram.utils.markdown import hbold

from utils.connect import dp
from keyboards.back_list_syrups_keyboard import back_list_syrups_keyboard


@dp.callback_query(lambda callback: callback.data == 'raspberries')
async def raspberries_callback(callback: CallbackQuery):
    await callback.message.edit_text(
        text=f'''<u>{hbold('РЕЦЕПТ Сироп Малины')}</u>
        Малина замороженная 600гр
        Кипяток 400гр
        Сахар 200гр\n
        {hbold('Метод приготовления:')}
        Малину Сахар и кипяток смешать в болендере и процедить
        (Потом тут будет видео рецепт пошагово)
        ''',
        reply_markup=back_list_syrups_keyboard,
        parse_mode='HTML'
    )