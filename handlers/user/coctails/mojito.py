from aiogram.types import CallbackQuery
from aiogram.utils.markdown import hbold

from utils.connect import dp
from keyboards.back_list_main_keyboard import back_list_main_keyboard


@dp.callback_query(lambda callback: callback.data == 'mojito')
async def mojito_callback(callback: CallbackQuery):
    await callback.message.edit_text(
        text=f'''<u>{hbold('РЕЦЕПТ Мохито')}</u>
        Ром(если мохито алк.) - 40мл
        Мята - 10листиков
        Лайм - 2 дольки
        Спрайт
        Лимон сироп - 20мл
        Сахар сироп- 20мл\n
        {hbold('Метод приготовления:')}
        В бокал закидываем мяту и лайм, с помощью мадлера разминаем всё, закидываем лёд, наливаем лимонный и сахарный сиропы, (если алк. мохито, добавляем ром), заливаем спрайтом, перемешать, украшаем долькой лайма
        (Потом тут будет видео рецепт пошагово)
        ''',
        reply_markup=back_list_main_keyboard,
        parse_mode='HTML'
    )