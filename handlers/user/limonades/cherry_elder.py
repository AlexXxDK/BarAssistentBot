from aiogram.types import CallbackQuery
from aiogram.utils.markdown import hbold

from utils.connect import dp
from keyboards.back_list_limonade_keyboard import back_list_limonade_keyboard


@dp.callback_query(lambda callback: callback.data == 'cherry_elder')
async def elder_callback(callback: CallbackQuery):
    await callback.message.edit_text(
        text=f'''<u>{hbold('РЕЦЕПТ Лимонад Вишня-Бузина')}</u>
        Сок рич вишня - 100мл
        Сироп бузина - 20мл
        Сок лимона - 20мл
        Вода сл.газ до конца\n
        (Потом тут будет видео рецепт пошагово)
        ''',
        reply_markup=back_list_limonade_keyboard,
        parse_mode='HTML'
    )