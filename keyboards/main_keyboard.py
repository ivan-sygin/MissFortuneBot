import aiogram
from aiogram import types


def mainKeyboard():
    buttons = [
        [
            '👤 Профиль 👤',
            '⚙️ Настройки ⚙️',
        ],
        [
            '⚜️ Список пользователей ⚜️',
        ],
    ]

    markup = []
    for row in buttons:
        markup.append([])
        for text in row:
            markup[-1].append(
                types.KeyboardButton(text=text)
            )
    keyboard = types.ReplyKeyboardMarkup(keyboard=markup, resize_keyboard=True)
    return keyboard

def closeMessage():
    buttons = [
        [
            ['Закрыть', 'closeMessage'],
        ],
    ]
    markup = []
    for row in buttons:
        markup.append([])
        for button in row:
            markup[-1].append(
                types.InlineKeyboardButton(text=button[0], callback_data=button[1])
            )
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=markup)
    return keyboard