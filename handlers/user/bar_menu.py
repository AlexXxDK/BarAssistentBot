from aiogram.types import CallbackQuery
from utils.connect import dp
from keyboards.bar_menu_keyboard import bar_menu_keyboard
from aiogram.utils.markdown import hbold


@dp.callback_query(lambda callback: callback.data == 'bar_menu')
async def menu_new_callback(callback: CallbackQuery):
    await callback.message.edit_text(
        text=f'''<u>{hbold('ХОЛОДНЫЕ НАПИТКИ')}</u>
    {hbold('ЛИМОНАД')}
        Маракуйя-жасмин
        Вишня-бузина
        Облепиха-мята
        Малина-бабл-гам
        молочный коктейль\n
    {hbold('ОСВЕЖАЮЩИЕ НАПИТКИ')}
        Coca-cola no sugar
        Coca-cola
        Fanta
        Sprite
        Schweppes
        Bonaqua негаз./среднегаз./сильногаз.
        Rich в ассортименте\n
<u>{hbold('ГОРЯЧИЕ НАПИТКИ')}</u>
    {hbold('ЧАЙ')}
        <i>{hbold('Чёрный чай')}</i>
        Эрл грей с бергамотом
        Чай с чебрецом\n
        <i>{hbold('Зеленый чай')}</i>
        Китайская сенча
        Японская липа\n
        <i>{hbold('Фруктовый чай')}</i>
        Нахальный фрукт\n
    {hbold('ФИРМЕННЫЙ ЧАЙ')}
        Облепиха
        Пряное яблоко
        Смородина-имбирь\n
    {hbold('КОФЕ')}
        Эспрессо
        Американо
        Капучино
        Латте Макиато
        Флэт Уайт
        Горячий шоколад
        Земляничный айс-латте\n
<u>{hbold('КОКТЕЙЛИ')}</u>
        Hotei Verry perry
        Cherry sour
        White wing highball
        Cookie Martini
        Twinkle Bitch
        Nude Lychee
        Глинтвейн\n
<u>{hbold('ВИНО')}</u>
        <i>{hbold('Игристое вино')}</i>
        Tosso Prosecco Millesimato (Италия)
        Lambrusco dell`Emillia (Италия)
        Lambrusco dell`Emillia Rossato (Италия)\n
        <i>{hbold('Белое вино')}</i>
        Pinot Grigio Villa San Giorgio (Италия сух.)
        Gaivota (Португалия п/сух.)
        Вино Riesling Trocken (Германия сух.)
        J.Meyler Gewurztraminer (Германия п/сух.)\n
        <i>{hbold('Красное вино')}</i>
        Jardin de la Taur Grenache-Syrah (Франция п/сух.)
        Jardin de la Taur Marsanne-Sauvignon Blanc (Франция сух.)
        Gatto Matto Nero D`avola sicilia DOC (Италия сух.)\n
        <i>{hbold('Розовое вино')}</i>
        Southlands Sauvignon Blanc Rose (ЮАР)\n
<u>{hbold('КРЕПКИЙ АЛКОГОЛЬ')}</u>
        <i>{hbold('Водка')}</i>
        Absolute (Швеция)
        Белорусская\n
        <i>{hbold('Джин')}</i>
        Beefeater (Великобритания)\n
        <i>{hbold('Ром')}</i>
        Angostura Reserva (Тринидат)\n
        <i>{hbold('Текила')}</i>
        Olmeka Altos Reposado (Мексика)
        Olmeka Blanco (Мексика)\n
        <i>{hbold('Коньяк')}</i>
        Ararat Ahtamar (Армения)
        Ararat Apricot (Армения)\n
        <i>{hbold('Виски')}</i>
        Chivas Regal (Шотландия)
        Ballantine`s Finest (Шотландия)
        Jameson (Ирландия)
        Four Roses (США)\n
        <i>{hbold('Вермут')}</i>
        Cinzano Rosso (Италия)
        Сinzano Bianco (Италия)
        Lillet Rose (Франция)\n
        <i>{hbold('Ликёр')}</i>
        Campari (Италия)
        Becherovka (Чехия)\n
<u>{hbold('ПИВО')}</u>
        Аливария 1894 Премиум (разливное)
        Аливария Белое Золото (бут.)
        Аливария Портер (бут.)
        Аливария 0 пшеничное (безалк.)
        1664 Blanc (бут.)
        Grinbergen Blanche
        Grinbergen Ambree
                    ''',
                    reply_markup=bar_menu_keyboard,
                    parse_mode='HTML'
                )
