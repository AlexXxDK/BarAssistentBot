from aiogram.types import CallbackQuery
from aiogram.utils.markdown import hbold

from utils.connect import dp
from keyboards.back_list_main_keyboard import back_list_main_keyboard


@dp.callback_query(lambda callback: callback.data == 'sacura')
async def sacura_callback(callback: CallbackQuery):
    await callback.message.edit_text(
        text=f'''<u>{hbold('РЕЦЕПТ Sacura')}</u>
        Арарат Априкот - 50мл
        Сироп Макадамия - 25мл
        Лимон - 25мл
        Белок\n
        {hbold('Метод приготовления:')}
        Дабл шейк
        {hbold('Бокал подачи:')} Олдфешен\n
        (Потом тут будет видео рецепт пошагово)
        ''',
        reply_markup=back_list_main_keyboard,
        parse_mode='HTML'
    )


