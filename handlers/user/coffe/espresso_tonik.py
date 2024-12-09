from aiogram.types import CallbackQuery
from aiogram.utils.markdown import hbold

from utils.connect import dp
from keyboards.back_list_coffe import back_list_keyboard


@dp.callback_query(lambda callback: callback.data == 'tonik')
async def elder_callback(callback: CallbackQuery):
    await callback.message.edit_text(
        text=f'''<u>{hbold('РЕЦЕПТ Эспрессо Тоник')}</u>
        Эспрессо
        Тоник
        {hbold('Метод приготовления:')}
        В бокал засыпать лед и тоник - добавить порцию эспрессо с верху
        (Потом тут будет видео рецепт пошагово)
        ''',
        reply_markup=back_list_keyboard,
        parse_mode='HTML'
    )