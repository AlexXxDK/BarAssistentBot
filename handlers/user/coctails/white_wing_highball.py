from aiogram.types import CallbackQuery
from aiogram.utils.markdown import hbold

from utils.connect import dp
from keyboards.back_list_main_keyboard import back_list_main_keyboard

print("Loading white_wing_highball handler...")


@dp.callback_query(lambda callback: callback.data == 'white_wing_highball')
async def white_callback(callback: CallbackQuery):
    await callback.message.edit_text(
        text=f'''<u>{hbold('РЕЦЕПТ White wing highball')}</u>
        Настойка Саган Дайля - 25мл
        Чинзано россо - 25мл
        Пюре Monin Черника - 25мл
        Тоник - 100мл
        Лимон - 25мл\n
        {hbold('Метод приготовления:')}
        Все ингредиенты влить в хайбол и перемешать 
        {hbold('Бокал подачи:')} Хайбол\n
        (Потом тут будет видео рецепт пошагово)
        ''',
        reply_markup=back_list_main_keyboard,
        parse_mode='HTML'
    )


print("white_wing_highball handler loaded.")
