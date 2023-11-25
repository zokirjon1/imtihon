import asyncio
import logging
import os
import sys

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from users import *
from dotenv import load_dotenv

load_dotenv('.env')
dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    user_id = message.from_user.id
    username = message.from_user.username
    created = message.date

    user = User_chat(user_id=user_id, username=username, created=created)
    session = Session()
    session.add(user)
    session.commit()


@dp.message()
async def user_chat_handler(message: Message):
    message_id = message.from_user.id
    colum_message = message.text
    created = message.date

    mes = Message(message_id=message_id, colum_message=colum_message, created=created)
    session = Session()
    session.add(mes)
    session.commit()


async def main() -> None:
    bot = Bot(os.getenv('TOKEN'), parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
