from aiogram.types import CallbackQuery
from aiogram.utils.markdown import hbold

from utils.connect import dp
from keyboards.back_list_tincture_keyboard import back_list_tincture_keyboard


@dp.callback_query(lambda callback: callback.data == 'sagan_dal')
async def sagan_callback(callback: CallbackQuery):
    await callback.message.edit_text(
        text=f'''<u>{hbold('РЕЦЕПТ Настойка Саган Дайля')}</u>
        0.5 джин меверик + чай Саган дайля 2 веточки 
        Су вид 40 градусов 2-3 часа\n
        ВАЖНО! После сувида дать остыть настойке и только потом открывать банку\n
        (Потом тут будет видео рецепт пошагово)
        ''',
        reply_markup=back_list_tincture_keyboard,
        parse_mode='HTML'
    )