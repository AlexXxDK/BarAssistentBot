from aiogram.types import CallbackQuery
from aiogram.utils.markdown import hbold

from utils.connect import dp
from keyboards.back_list_main_keyboard import back_list_main_keyboard


@dp.callback_query(lambda callback: callback.data == 'yakuza')
async def yakuza_callback(callback: CallbackQuery):
    await callback.message.edit_text(
        text=f'''<u>{hbold('РЕЦЕПТ Yakuza')}</u>
        Бурбон Фоур Роуз - 40мл
        Франгелико - 20мл
        Украсить цедрой апельсина
        2дэша апельсиновый битер\n
        {hbold('Метод приготовления:')}
        Стир
        {hbold('Бокал подачи:')} Олдфешен\n
        (Потом тут будет видео рецепт пошагово)
        ''',
        reply_markup=back_list_main_keyboard,
        parse_mode='HTML'
    )


