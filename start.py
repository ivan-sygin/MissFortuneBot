import asyncio
import os
from handlers import default_commands, profile_commands
from aiogram import Bot, Dispatcher, types


bot = Bot(token=os.environ['TOKEN_TG_BOT'])
admin_chat_id = os.environ['ADMIN_CHAT_ID']


async def sendMessageToCreator(text: str, reply_markup=None, **kwargs):
    await bot.send_message(
        chat_id=admin_chat_id,
        text=text,
        reply_markup=reply_markup,
        **kwargs
    )


async def main():
    global bot
    dp = Dispatcher()

    dp.include_router(default_commands.router)
    dp.include_router(profile_commands.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
