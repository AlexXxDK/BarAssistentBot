from aiogram.types import CallbackQuery
from aiogram.utils.markdown import hbold

from utils.connect import dp
from keyboards.back_list_main_keyboard import back_list_main_keyboard


@dp.callback_query(lambda callback: callback.data == 'campari_spritz')
async def campari_callback(callback: CallbackQuery):
    await callback.message.edit_text(
        text=f'''<u>{hbold('РЕЦЕПТ Campari Spritz')}</u>
        Кампари - 25мл
        Чинзано Россо - 25мл
        Барон Ди Араньяк - 100мл
        Тоник - 50мл\n
        {hbold('Метод приготовления:')}
        Билд
        {hbold('Бокал подачи:')} Винка\n
        (Потом тут будет видео рецепт пошагово)
        ''',
        reply_markup=back_list_main_keyboard,
        parse_mode='HTML'
    )