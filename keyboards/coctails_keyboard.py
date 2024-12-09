from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


builder = InlineKeyboardBuilder()

back = InlineKeyboardButton(text='👈Назад', callback_data='back_list')

hotei_verry_perry = InlineKeyboardButton(text='🥥Hotei verry perry', callback_data='hotei_verry_perry')
cherry_sour = InlineKeyboardButton(text='🍒Cherry sour', callback_data='cherry_sour')
white_wing_highball = InlineKeyboardButton(text='White wing highball', callback_data='white_wing_highball')
cookie_Martini = InlineKeyboardButton(text='🍪Cookie Martini', callback_data='cookie_Martini')
twinkle_Bitch = InlineKeyboardButton(text='🍑Twinkle Bitch', callback_data='twinkle_Bitch')
nude_Lychee = InlineKeyboardButton(text='Nude Lychee', callback_data='nude_Lychee')

temptation = InlineKeyboardButton(text='🍍Temptation', callback_data='temptation')
luxury_paloma = InlineKeyboardButton(text='Laxury Paloma', callback_data='luxury_paloma')
fierro_spritz = InlineKeyboardButton(text='Fierro Spritz', callback_data='fierro_spritz')
sangria = InlineKeyboardButton(text='🍷Сангрия', callback_data='sangria')
sacura = InlineKeyboardButton(text='🥜Sacura', callback_data='sacura')
yakuza = InlineKeyboardButton(text='Yakuza', callback_data='yakuza')

origami = InlineKeyboardButton(text='🍍Origami', callback_data='origami')
kintsugi = InlineKeyboardButton(text='🥥Kintsugi', callback_data='kintsugi')
watermalon_daiquiri = InlineKeyboardButton(text='🍉Watermalon Daiquiri', callback_data='watermalon_daiquiri')
milano_torio_highball = InlineKeyboardButton(text='Milano Torio Highball', callback_data='milano_torio_highball')
aperol_spritz = InlineKeyboardButton(text='Aperol Spritz', callback_data='aperol_spritz')
campari_spritz = InlineKeyboardButton(text='Campari Spritz', callback_data='campari_spritz')
rose_lillet = InlineKeyboardButton(text='🌹Rose Lillet', callback_data='rose_lillet')
negroni = InlineKeyboardButton(text='Негрони', callback_data='negroni')
long_island  = InlineKeyboardButton(text='Long Island', callback_data='long_island')
old_fashioned = InlineKeyboardButton(text='Old Fashioned', callback_data='old_fashioned')
mojito = InlineKeyboardButton(text='🌿Мохито', callback_data='mojito')

builder.row(hotei_verry_perry)
builder.row(cherry_sour)
builder.row(white_wing_highball)
builder.row(cookie_Martini)
builder.row(twinkle_Bitch)
builder.row(nude_Lychee)

builder.row(temptation)
builder.row(luxury_paloma)
builder.row(fierro_spritz)
builder.row(sangria)
builder.row(sacura)
builder.row(yakuza)

builder.row(origami)
builder.row(kintsugi)
builder.row(watermalon_daiquiri)
builder.row(milano_torio_highball)
builder.row(aperol_spritz)
builder.row(campari_spritz)
builder.row(rose_lillet)
builder.row(negroni)
builder.row(long_island)
builder.row(old_fashioned)
builder.row(mojito)

builder.row(back)

coctails_keyboard = builder.as_markup()




