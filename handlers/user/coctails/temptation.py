from aiogram.types import CallbackQuery
from aiogram.utils.markdown import hbold

from utils.connect import dp
from keyboards.back_list_main_keyboard import back_list_main_keyboard


@dp.callback_query(lambda callback: callback.data == 'temptation')
async def temptation_callback(callback: CallbackQuery):
    await callback.message.edit_text(
        text=f'''<u>{hbold('РЕЦЕПТ temptation')}</u>
        Водка(шмидт/сябры) - 25мл
        Мерриес(сливочный ликер) - 25мл
        Ананасовый сок - 100мл
        Арбузный сироп - 20мл\n
        {hbold('Метод приготовления:')}
        Шейк
        {hbold('Бокал подачи:')} Шале\n
        (Потом тут будет видео рецепт пошагово)
        ''',
        reply_markup=back_list_main_keyboard,
        parse_mode='HTML'
    )


