from aiogram.types import CallbackQuery
from aiogram.utils.markdown import hbold

from utils.connect import dp
from keyboards.back_list_limonade_keyboard import back_list_limonade_keyboard


@dp.callback_query(lambda callback: callback.data == 'sea_buckthorn_mint')
async def sea_mint_callback(callback: CallbackQuery):
    await callback.message.edit_text(
        text=f'''<u>{hbold('РЕЦЕПТ Лимонад Облепиха-Мята')}</u>
        Сироп облепиха - 50
        Мята 5 листиков
        Лимон - 25мл
        Сахар -25мл
        Бонаква сл.газ- до конца\n
        (Потом тут будет видео рецепт пошагово)
        ''',
        reply_markup=back_list_limonade_keyboard,
        parse_mode='HTML'
    )