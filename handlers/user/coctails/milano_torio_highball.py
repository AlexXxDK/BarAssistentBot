from aiogram.types import CallbackQuery
from aiogram.utils.markdown import hbold

from utils.connect import dp
from keyboards.back_list_main_keyboard import back_list_main_keyboard


@dp.callback_query(lambda callback: callback.data == 'milano_torio_highball')
async def milano_callback(callback: CallbackQuery):
    await callback.message.edit_text(
        text=f'''<u>{hbold('РЕЦЕПТ Milano Torio Highball')}</u>
        Ольмека Бьянко - 25мл
        Чинзано Россо - 25мл
        Швепс - до конца\n
        {hbold('Метод приготовления:')}
        Билд
        {hbold('Бокал подачи:')} Хайбол\n
        (Потом тут будет видео рецепт пошагово)
        ''',
        reply_markup=back_list_main_keyboard,
        parse_mode='HTML'
    )