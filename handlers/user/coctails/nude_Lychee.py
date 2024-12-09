from aiogram.types import CallbackQuery
from aiogram.utils.markdown import hbold

from utils.connect import dp
from keyboards.back_list_main_keyboard import back_list_main_keyboard

print("Loading nude_Lychee handler...")


@dp.callback_query(lambda callback: callback.data == 'nude_Lychee')
async def nude_callback(callback: CallbackQuery):
    await callback.message.edit_text(
        text=f'''<u>{hbold('РЕЦЕПТ Nude Lychee')}</u>        
        Водка РБ - 50мл
        Пюре Личи - 25гр
        Сироп Земляника - 25гр
        Лимонный сок - 30гр
        Швепс - 100мл
        Мята - 5-6 листиков \n
        {hbold('Метод приготовления:')}
        Закинуть мяту в шейкер, добавить все ингридиенты(кроме швепса) и шейкуем, перелить в Флюте - долить швепс
        {hbold('Бокал подачи:')} Флюте\n
        (Потом тут будет видео рецепт пошагово)
        ''',
        reply_markup=back_list_main_keyboard,
        parse_mode='HTML'
    )


print("nude_Lychee handler loaded.")
