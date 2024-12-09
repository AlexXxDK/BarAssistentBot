from aiogram.types import CallbackQuery
from aiogram.utils.markdown import hbold

from utils.connect import dp
from keyboards.back_list_main_keyboard import back_list_main_keyboard


@dp.callback_query(lambda callback: callback.data == 'origami')
async def kintsugi_callback(callback: CallbackQuery):
    await callback.message.edit_text(
        text=f'''<u>{hbold('РЕЦЕПТ Origami')}</u>
        Бифитер - 50мл
        Ананасовый сок - 50мл
        Сок лимона - 25мл
        Роза сироп - 25мл\n
        {hbold('Метод приготовления:')}
        Шейк
        {hbold('Бокал подачи:')} Флюте\n
        (Потом тут будет видео рецепт пошагово)
        ''',
        reply_markup=back_list_main_keyboard,
        parse_mode='HTML'
    )