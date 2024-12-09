from aiogram.types import CallbackQuery
from aiogram.utils.markdown import hbold

from utils.connect import dp
from keyboards.back_list_main_keyboard import back_list_main_keyboard


@dp.callback_query(lambda callback: callback.data == 'fierro_spritz')
async def fierro_callback(callback: CallbackQuery):
    await callback.message.edit_text(
        text=f'''<u>{hbold('РЕЦЕПТ Fierro Spritz')}</u>
        Martini Fiero - 75мл
        Швепс - 250мл\n
        {hbold('Метод приготовления:')}
        Билд
        {hbold('Бокал подачи:')} Белая Винка\n
        (Потом тут будет видео рецепт пошагово)
        ''',
        reply_markup=back_list_main_keyboard,
        parse_mode='HTML'
    )


