from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message
import start
import replics.Greetings
from keyboards.profile_keyboard import profileInlineKeyboard
from modules.bot import HandlerDB
from keyboards.main_keyboard import mainKeyboard
from modules.filters.CustomFSM import StageFilter
from modules.filters.Roles import RoleFilter
from replics.ProfileInfo import ProfileInfo

router = Router()

db = HandlerDB.bot_connector


@router.message(Command("start"))
async def start_handler(message: Message):
    chat_id = message.chat.id
    username = message.from_user.first_name

    founded_user = db.findUser(chat_id)

    if founded_user is None:
        new_user = db.createUser(chat_id, username)
        await message.answer(replics.Greetings.GreetingsUnknownUser(), reply_markup=mainKeyboard())
        await start.sendMessageToCreator(text=f'Новый аккаунт {new_user.first_name}', reply_markup=mainKeyboard())
    else:
        await message.answer(replics.Greetings.GreetingsKnownUser(founded_user), reply_markup=mainKeyboard())


@router.message(F.text.contains('привет'))
async def message_with_text(message: Message):
    chat_id = message.chat.id
    username = message.chat.username

    founded_user = db.findUser(chat_id)

    if founded_user is None:
        db.createUser(chat_id, username)
        await message.answer(replics.Greetings.GreetingsUnknownUser(), reply_markup=mainKeyboard())
    else:
        await message.answer(replics.Greetings.GreetingsKnownUser(founded_user), reply_markup=mainKeyboard())


@router.message(
    F.text == '⚜️ Список пользователей ⚜️',
    RoleFilter('Администратор'),
    StageFilter('*'),
)
async def message_with_text(message: Message):
    list_users = [str(i) for i in db.getUsers()]
    await message.answer(text='\n'.join(list_users))

@router.message(
    F.text == '👤 Профиль 👤',
    RoleFilter('*'),
    StageFilter('*'),
)
async def message_with_text(message: Message):
    user = db.findUser(message.chat.id)
    db.setStageUser(user.chat_id, 'edit_profile')
    await message.answer(text=ProfileInfo(user), reply_markup=profileInlineKeyboard())

@router.message(F.sticker)
async def message_with_sticker(message: Message):
    await message.answer("Это стикер!")


@router.message(F.animation)
async def message_with_gif(message: Message):
    await message.answer("Это GIF!")