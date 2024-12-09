from aiogram.types import CallbackQuery
from aiogram.utils.markdown import hbold

from utils.connect import dp
from keyboards.back_list_main_keyboard import back_list_main_keyboard


@dp.callback_query(lambda callback: callback.data == 'luxury_paloma')
async def luxury_callback(callback: CallbackQuery):
    await callback.message.edit_text(
        text=f'''<u>{hbold('РЕЦЕПТ Luxury Paloma')}</u>
        Текила Ольмека Бьянко - 20мл
        Грейпфруктовый сок - 50мл
        Сироп бузины - 15мл
        Барон Ди Араньяк - до конца\n
        {hbold('Метод приготовления:')}
        Билд
        {hbold('Бокал подачи:')} Белая Винка\n
        (Потом тут будет видео рецепт пошагово)
        ''',
        reply_markup=back_list_main_keyboard,
        parse_mode='HTML'
    )


