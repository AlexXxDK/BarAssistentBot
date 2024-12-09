from aiogram.types import CallbackQuery
from aiogram.utils.markdown import hbold

from utils.connect import dp
from keyboards.back_list_main_keyboard import back_list_main_keyboard


@dp.callback_query(lambda callback: callback.data == 'kintsugi')
async def kintsugi_callback(callback: CallbackQuery):
    await callback.message.edit_text(
        text=f'''<u>{hbold('РЕЦЕПТ Kintsugi')}</u>
        Пюре Monin Вишня - 25мл
        Кокосовое молоко - 100мл
        Ром Ангастура - 50мл\n
        {hbold('Метод приготовления:')}
        Шейк
        {hbold('Бокал подачи:')} Белая винка\n
        (Потом тут будет видео рецепт пошагово)
        ''',
        reply_markup=back_list_main_keyboard,
        parse_mode='HTML'
    )