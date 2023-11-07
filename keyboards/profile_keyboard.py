import aiogram
from aiogram import types


def profileInlineKeyboard():
    buttons = [
        [
            ['⏫ Запросить повышение роли ⏫', 'ask_for_upgrade'],
        ],
        [
            ['⚙️ Настройки ⚙️', 'settings_profile'],
        ],
        [
            ['⬅️ Назад ⬅️', 'go_back'],
        ]
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

def profileAcceptKeyboard(chat_id,role):
    buttons = [
        [
            ['✅', f'accept_rankup|{chat_id}|{role}'],
            ['❌', f'deny_rankup|{chat_id}|{role}'],
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