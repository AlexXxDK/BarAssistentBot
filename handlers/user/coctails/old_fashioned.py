from aiogram.types import CallbackQuery
from aiogram.utils.markdown import hbold

from utils.connect import dp
from keyboards.back_list_main_keyboard import back_list_main_keyboard


@dp.callback_query(lambda callback: callback.data == 'old_fashioned')
async def old_fashioned_callback(callback: CallbackQuery):
    await callback.message.edit_text(
        text=f'''<u>{hbold('РЕЦЕПТ Old Fashioned')}</u>
       Сахар 5гр
        Бурбон (Four rous) - 50мл
        Газированная вода - 5мл\n
        {hbold('Метод приготовления:')}
        Стир. Сахар 5гр кидаем в смесительный бокал - добавляем  воду 5мл и тщательно вымешиваем Сахар до полного растворения -  добавляем лед в смесительный бокал и вымешиваем еще раз (сек. 5) - добавляем Бурбон 50мл и снова вымешиваем 5сек - переливаем содержимое в охлажденный бокал Олд фэшн со льдом
        {hbold('Бокал подачи:')} Олд Фэшны\n
        (Потом тут будет видео рецепт пошагово)
        ''',
        reply_markup=back_list_main_keyboard,
        parse_mode='HTML'
    )