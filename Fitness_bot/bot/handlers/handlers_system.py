from aiogram import types
from aiogram.dispatcher.filters import Text

from Fitness_bot.DB.db_system import DB
from Fitness_bot.bot.buttons.reply import contact, warm_up, yoga, strength, cardio, _exercises, location_
from Fitness_bot.bot.buttons.texts import welcome
from Fitness_bot.bot.dispatcher import dp


@dp.message_handler(commands='start')
async def start_(message: types.Message):
    if not DB().if_exists(message.from_user.id):
        DB().add_user(message.from_user.id, message.from_user.is_bot, message.from_user.first_name,
                      message.from_user.last_name, message.from_user.username, message.from_user.language_code)
    await message.answer(welcome.format(message.from_user.first_name))
    await message.answer("Please share your phone number to use our Fitify bot!!!", reply_markup=contact())


@dp.message_handler(Text('🔙 back'))
async def back_(message: types.Message):
    await message.answer("What doy you want?  ", reply_markup=_exercises())


@dp.message_handler(content_types=types.ContentTypes.CONTACT)
async def phone_number(message: types.Message):
    phone_num = message.contact.phone_number
    DB().update_number(user_id=message.from_user.id, phone_number=phone_num)
    await message.answer("What doy you want?  ", reply_markup=_exercises())


@dp.message_handler(Text('Warmup,recovery🏃'))
async def warmup_(message: types.Message):
    await message.answer('Choose your exercise', reply_markup=warm_up())


@dp.message_handler(Text('Yoga,Stretching 🧘'))
async def yoga_(message: types.Message):
    await message.answer('Choose your exercise', reply_markup=yoga())


@dp.message_handler(Text('Strength 💪'))
async def strength_(message: types.Message):
    await message.answer('Choose your exercise', reply_markup=strength())


@dp.message_handler(Text("HIIT,Cardio ♥ "))
async def cardio_(message: types.Message):
    await message.answer('Choose your exercise', reply_markup=cardio())


@dp.message_handler(commands='gif')
async def gif_(message: types.Message):
    await message.bot.send_animation(message.chat.id,
                                     'https://seven.app/media/images/Warm-Up-Champion-Female-jumping-jacks.gif')


@dp.message_handler(Text('🚅 Eltib berish'))
async def delivery_(message: types.Message):
    await message.answer("Geo-Location", reply_markup=location_())


@dp.message_handler(content_types=types.ContentTypes.LOCATION)
async def cach_location(message:types.Message):
    lat = message.location.latitude
    long = message.location.longitude

    await message.answer(f"{lat},{long}")



