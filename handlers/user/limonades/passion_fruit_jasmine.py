from aiogram.types import CallbackQuery
from aiogram.utils.markdown import hbold

from utils.connect import dp
from keyboards.back_list_limonade_keyboard import back_list_limonade_keyboard


@dp.callback_query(lambda callback: callback.data == 'passion_fruit_jasmine')
async def jasmine_callback(callback: CallbackQuery):
    await callback.message.edit_text(
        text=f'''<u>{hbold('РЕЦЕПТ Лимонад Маракуйя-Жасмин')}</u>
        Маракуйя - 30мл 
        Жасмин - 30мл 
        Лимон - 20мл 
        Бонаква сл.газ - до конца\n
        (Потом тут будет видео рецепт пошагово)
        ''',
        reply_markup=back_list_limonade_keyboard,
        parse_mode='HTML'
    )