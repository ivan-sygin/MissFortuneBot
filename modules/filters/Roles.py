from typing import Union
from aiogram.filters import BaseFilter
from aiogram.types import Message, CallbackQuery
from modules.bot.HandlerDB import bot_connector


class RoleFilter(BaseFilter):

    def __init__(self, role: Union[str, list]):  # [2]
        self.role = role

    async def __call__(self, message: Message) -> bool:
        if isinstance(self.role, str):
            if self.role == '*':
                return True
            user_role = bot_connector.getRole(message.chat.id)
            if user_role != self.role:
                await message.answer(f'Это команда доступна только пользователям с ролью {self.role}')
            return user_role == self.role
        else:
            user_role = bot_connector.getRole(message.chat.id)
            if user_role not in self.role:
                await message.answer(f'Это команда доступна только пользователям с ролью {self.role}')
            return user_role in self.role


class RoleFilterCallback(BaseFilter):

    def __init__(self, role: Union[str, list]):  # [2]
        self.role = role

    async def __call__(self, callback_query: CallbackQuery) -> bool:
        if isinstance(self.role, str):
            if self.role == '*':
                return True
            user_role = bot_connector.getRole(callback_query.message.chat.id)
            if user_role != self.role:
                await callback_query.message.answer(f'Это команда доступна только пользователям с ролью {self.role}')
            return user_role == self.role
        else:
            user_role = bot_connector.getRole(callback_query.message.chat.id)
            if user_role not in self.role:
                await callback_query.message.answer(f'Это команда доступна только пользователям с ролью {self.role}')
            return user_role in self.role
