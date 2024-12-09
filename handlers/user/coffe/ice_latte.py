from aiogram.types import CallbackQuery
from aiogram.utils.markdown import hbold

from utils.connect import dp
from keyboards.back_list_coffe import back_list_keyboard


@dp.callback_query(lambda callback: callback.data == 'latte')
async def elder_callback(callback: CallbackQuery):
    await callback.message.edit_text(
        text=f'''<u>{hbold('РЕЦЕПТ Айс Латте')}</u>
        Эспрессо
        Сироп(по желанию клиента)
        Молоко
        {hbold('Метод приготовления:')}
        В бокал со льдом добавляем 15гр сиропа, заливаем молоком и размешиваем, наверх залить эспрессо\n
        (Потом тут будет видео рецепт пошагово)
        ''',
        reply_markup=back_list_keyboard,
        parse_mode='HTML'
    )