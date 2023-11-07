from typing import Union
from aiogram.filters import BaseFilter
from aiogram.types import Message,CallbackQuery
from modules.bot.HandlerDB import bot_connector


class StageFilter(BaseFilter):

    def __init__(self, stage: Union[str, list]):  # [2]
        self.stage = stage

    async def __call__(self, message: Message) -> bool:
        if isinstance(self.stage, str):
            if self.stage == '*':
                return True
            user_stage = bot_connector.getStage(message.chat.id)
            return user_stage == self.stage
        else:
            user_stage = bot_connector.getStage(message.chat.id)
            return user_stage in self.stage


class StageFilterCallback(BaseFilter):

    def __init__(self, stage: Union[str, list]):  # [2]
        self.stage = stage

    async def __call__(self, callback_query: CallbackQuery) -> bool:
        if isinstance(self.stage, str):
            if self.stage == '*':
                return True
            user_stage = bot_connector.getStage(callback_query.message.chat.id)
            return user_stage == self.stage
        else:
            user_stage = bot_connector.getStage(callback_query.message.chat.id)
            return user_stage in self.stage
