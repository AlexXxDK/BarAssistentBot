from aiogram.types import CallbackQuery
from aiogram.utils.markdown import hbold

from utils.connect import dp
from keyboards.back_list_syrups_keyboard import back_list_syrups_keyboard


@dp.callback_query(lambda callback: callback.data == 'apple')
async def apple_callback(callback: CallbackQuery):
    await callback.message.edit_text(
        text=f'''<u>{hbold('РЕЦЕПТ Сироп Пряное Яблоко')}</u>
        Яблоки
        Лимон
        Специи
        {hbold('Метод приготовления:')}
        500гр яблок (очищенных от кожуры, семечек и всего не нужного – не выкидываем это все)
        250мл сок с лимона (очистить от кожуры и отложить)
        Все это закидываем в блендер. Блендируем и откладываем в холодильник на 4 часа 
        500гр сахара белого
        250мл воды
        Шкурки от яблок и лимонов 
        15 гвоздик, 2 палочки корицы, 10 кардамона, имбирь 50 гр (потертый на терку), 2 звездочки аниса, 5 зерен душистого перца 
        Смешиваем с отставленным в холодильник и готовим пол часа на медленном огне и оставляем чтоб остыл 
        Цедим через сито и все готово.\n
        (Потом тут будет видео рецепт пошагово)
        ''',
        reply_markup=back_list_syrups_keyboard,
        parse_mode='HTML'
    )