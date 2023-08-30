import asyncio

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from Fitness_bot.utils.util import BOT_TOKEN

loop = asyncio.get_event_loop()
bot = Bot(BOT_TOKEN, loop=loop)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
