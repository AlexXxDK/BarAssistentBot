from aiogram.types import CallbackQuery
from aiogram.utils.markdown import hbold

from utils.connect import dp
from keyboards.back_list_main_keyboard import back_list_main_keyboard


@dp.callback_query(lambda callback: callback.data == 'twinkle_Bitch')
async def twinkle_callback(callback: CallbackQuery):
    await callback.message.edit_text(
        text=f'''<u>{hbold('РЕЦЕПТ Twinkle Bitch')}</u>
        Водка РБ - 25мл
        Персиковый сок - 50мл
        Апельсиновый сок - 50мл
        Сливочный ликер Фруко Шультц - 25мл\n
        {hbold('Метод приготовления:')}
        Все ингредиенты влить в шейкер
        {hbold('Бокал подачи:')} Шале\n
        (Потом тут будет видео рецепт пошагово)
        ''',
        reply_markup=back_list_main_keyboard,
        parse_mode='HTML'
    )


