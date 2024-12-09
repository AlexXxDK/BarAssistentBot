from aiogram.types import CallbackQuery
from aiogram.utils.markdown import hbold

from utils.connect import dp
from keyboards.back_list_coffe import back_list_keyboard


@dp.callback_query(lambda callback: callback.data == 'shmel')
async def elder_callback(callback: CallbackQuery):
    await callback.message.edit_text(
        text=f'''<u>{hbold('РЕЦЕПТ Шмель')}</u>
        Эспрессо
        Апельсиновый сок
        {hbold('Метод приготовления:')}
        В бокал со льдом добавляем апельсиновый сок(почти до конца), наверх льём эспрессо
        (Потом тут будет видео рецепт пошагово)
        ''',
        reply_markup=back_list_keyboard,
        parse_mode='HTML'
    )