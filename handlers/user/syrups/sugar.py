from aiogram.types import CallbackQuery
from aiogram.utils.markdown import hbold

from utils.connect import dp
from keyboards.back_list_syrups_keyboard import back_list_syrups_keyboard


@dp.callback_query(lambda callback: callback.data == 'sugar')
async def sugar_callback(callback: CallbackQuery):
    await callback.message.edit_text(
        text=f'''<u>{hbold('РЕЦЕПТ Сироп Сахарный')}</u>
        Сахар - 600гр
        Кипяток - 400гр
        Кожура 1 апельсина\n
        {hbold('Метод приготовления:')}
        Чистим апельсин, измельчаем кожуру 
        Все ингредиенты закидываем в блендер
        После даем настоятся и процеживаем\n
        (Потом тут будет видео рецепт пошагово)
        ''',
        reply_markup=back_list_syrups_keyboard,
        parse_mode='HTML'
    )