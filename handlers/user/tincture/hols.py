from aiogram.types import CallbackQuery
from aiogram.utils.markdown import hbold

from utils.connect import dp
from keyboards.back_list_tincture_keyboard import back_list_tincture_keyboard


@dp.callback_query(lambda callback: callback.data == 'hols')
async def hols_callback(callback: CallbackQuery):
    await callback.message.edit_text(
        text=f'''<u>{hbold('РЕЦЕПТ Настойка Холс')}</u>
        0.5 водки Рб переливаем в банку
        Добавляем 1 пачку холса черного + 15 листиков мяты 
        В сувид на 50 градусов 4часа\n
        ВАЖНО! После сувида дать остыть настойке и только потом открывать банку\n
        (Потом тут будет видео рецепт пошагово)
        ''',
        reply_markup=back_list_tincture_keyboard,
        parse_mode='HTML'
    )