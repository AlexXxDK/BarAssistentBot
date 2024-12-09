from aiogram.types import CallbackQuery
from aiogram.utils.markdown import hbold

from utils.connect import dp
from keyboards.back_list_main_keyboard import back_list_main_keyboard


@dp.callback_query(lambda callback: callback.data == 'hotei_verry_perry')
async def very_callback(callback: CallbackQuery):
    await callback.message.edit_text(
        text=f'''<u>{hbold('РЕЦЕПТ Hotei verry perry')}</u>
        Ром ангастура - 50мл
        Ананасовый сок - 50мл
        Кокосовый сироп - 25мл
        Лимонный сок - 20мл
        Кордиал анчан - 50мл\n
        {hbold('Метод приготовления:')}
        Шейк
        {hbold('Бокал подачи:')} Флюте\n
        (Потом тут будет видео рецепт пошагово)
        ''',
        reply_markup=back_list_main_keyboard,
        parse_mode='HTML'
    )

