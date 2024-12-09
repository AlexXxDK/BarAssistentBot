from aiogram.types import CallbackQuery
from aiogram.utils.markdown import hbold

from utils.connect import dp
from keyboards.back_list_main_keyboard import back_list_main_keyboard


@dp.callback_query(lambda callback: callback.data == 'cherry_sour')
async def cherry_callback(callback: CallbackQuery):
    await callback.message.edit_text(
        text=f'''<u>{hbold('РЕЦЕПТ Cherry_sour')}</u>
        Настойка холс - 50мл
        Пюре Monin Вишня - 25мл
        Лимонный сок - 20мл
        Белок яйца - 1шт\n
        {hbold('Метод приготовления:')}
        Сначала шейкуем без льда, затем добавляем лед и шейкуем еще раз
        {hbold('Бокал подачи:')} Олд фешен\n
        (Потом тут будет видео рецепт пошагово)
        ''',
        reply_markup=back_list_main_keyboard,
        parse_mode='HTML'
    )