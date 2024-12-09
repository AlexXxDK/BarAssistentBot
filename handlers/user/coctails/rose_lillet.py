from aiogram.types import CallbackQuery
from aiogram.utils.markdown import hbold

from utils.connect import dp
from keyboards.back_list_main_keyboard import back_list_main_keyboard


@dp.callback_query(lambda callback: callback.data == 'rose_lillet')
async def rose_callback(callback: CallbackQuery):
    await callback.message.edit_text(
        text=f'''<u>{hbold('РЕЦЕПТ Rose Lillet')}</u>
        Лилет Розе - 50мл
        Ламбруско Розе - 100мл
        Тоник - 70мл\n
        {hbold('Метод приготовления:')}
        Билд
        {hbold('Бокал подачи:')} Винный бокал\n
        (Потом тут будет видео рецепт пошагово)
        ''',
        reply_markup=back_list_main_keyboard,
        parse_mode='HTML'
    )