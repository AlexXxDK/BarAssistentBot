from aiogram.types import CallbackQuery
from aiogram.utils.markdown import hbold

from utils.connect import dp
from keyboards.back_list_coffe import back_list_keyboard


@dp.callback_query(lambda callback: callback.data == 'cherry_gad')
async def elder_callback(callback: CallbackQuery):
    await callback.message.edit_text(
        text=f'''<u>{hbold('РЕЦЕПТ Вишневый Сад')}</u>
        Вишневый сок - 200мл
        Эспрессо
        {hbold('Метод приготовления:')}
        В бокал засыпать лед и налить вишневый сок - добавить порцию эспрессо с верху
        {hbold('Бокал подачи:')} Рокс со льдом\n
        (Потом тут будет видео рецепт пошагово)
        ''',
        reply_markup=back_list_keyboard,
        parse_mode='HTML'
    )