from aiogram.types import CallbackQuery
from aiogram.utils.markdown import hbold

from utils.connect import dp
from keyboards.back_list_syrups_keyboard import back_list_syrups_keyboard


@dp.callback_query(lambda callback: callback.data == 'mandarin')
async def mandarin_callback(callback: CallbackQuery):
    await callback.message.edit_text(
        text=f'''<u>{hbold('РЕЦЕПТ Сироп Мандарин')}</u>
        Мандарин 9шт
        Сахарный сироп
        Винный уксус\n
        {hbold('Метод приготовления:')}
        Мандарин выжимаем сок (и откладываем его)
        Половинки мандарина разрезаем и закидываем в блендер
        На каждую половинку  добавляем 30гр сахарного сиропа  ( должно выйти 540гр сахарного сиропа)
        Процеживаем  
        Добавляем сок мандарина 
        Добавляем От полученного обьема 10% винного уксуса
        Блендером еще раз и переливаем в бутылку\n
        (Потом тут будет видео рецепт пошагово)
        ''',
        reply_markup=back_list_syrups_keyboard,
        parse_mode='HTML'
    )