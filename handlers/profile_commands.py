from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message,CallbackQuery
import start
import replics.Greetings
from keyboards.profile_keyboard import profileInlineKeyboard, profileAcceptKeyboard
from modules.bot import HandlerDB
from keyboards.main_keyboard import mainKeyboard, closeMessage
from modules.filters.CustomFSM import StageFilter, StageFilterCallback
from modules.filters.Roles import RoleFilter, RoleFilterCallback
from replics.ProfileInfo import ProfileInfo, ProfileWantUpdate


router = Router()
db = HandlerDB.bot_connector

@router.callback_query(
    F.data == "closeMessage",
)
async def message_with_text(callback_query: CallbackQuery):
    await callback_query.message.delete()
    await start.bot.answer_callback_query(callback_query.id)

@router.callback_query(
    F.data == "ask_for_upgrade",
    RoleFilterCallback('Пользователь'),
    StageFilterCallback('edit_profile'),
)
async def message_with_text(callback_query: CallbackQuery):
    user = db.findUser(callback_query.message.chat.id)
    await start.sendMessageToCreator(
        text=ProfileWantUpdate(user, "Администратор"),
        reply_markup=profileAcceptKeyboard(user.chat_id, 'Администратор')
    )
    await callback_query.message.answer(text="Запрос отправлен", reply_markup=closeMessage())
    await start.bot.answer_callback_query(callback_query.id)

@router.callback_query(
    F.data[:13] == "accept_rankup",
    RoleFilterCallback('Создатель'),
    StageFilterCallback('*'),
)
async def message_with_text(callback_query: CallbackQuery):
    data = callback_query.data.split("|")[1:]
    user = db.findUser(data[0])
    db.setRoleUser(user.chat_id, data[1])
    await start.bot.send_message(
        chat_id=user.chat_id,
        text=f"Вы были повышены до роли {data[1]}",
        reply_markup=closeMessage()
    )
    await callback_query.message.delete()
    await start.bot.answer_callback_query(callback_query.id)

@router.callback_query(
    F.data[:11] == "deny_rankup",
    RoleFilterCallback('Создатель'),
    StageFilterCallback('*'),
)
async def message_with_text(callback_query: CallbackQuery):
    data = callback_query.data.split("|")[1:]
    user = db.findUser(data[0])
    await start.bot.send_message(
        chat_id=user.chat_id,
        text=f"Вам было отказно в повышении",
        reply_markup=closeMessage()
    )
    await callback_query.message.delete()
    await start.bot.answer_callback_query(callback_query.id)