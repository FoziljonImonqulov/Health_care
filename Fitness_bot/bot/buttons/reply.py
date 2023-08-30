from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def _exercises():
    design = [
        [KeyboardButton('Healthy dairy 😎'), KeyboardButton('What is news today? 🔊')],
        [KeyboardButton('Warmup,recovery🏃'), KeyboardButton('Yoga,Stretching 🧘')],
        [KeyboardButton("HIIT,Cardio ♥ "), KeyboardButton('Strength 💪')]
    ]
    markup = ReplyKeyboardMarkup(design, resize_keyboard=True, one_time_keyboard=True)
    return markup


def contact():
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    markup.add(KeyboardButton("Phone number 📱", request_contact=True))
    return markup


def warm_up():
    desing = [
        [KeyboardButton('Warm up'), KeyboardButton('Full body rolling')],
        [KeyboardButton('Legs rolling'), KeyboardButton('Back rolling')],
        [KeyboardButton('🔙 back')]
    ]
    markup = ReplyKeyboardMarkup(desing, one_time_keyboard=True, resize_keyboard=True)
    return markup


def yoga():
    desing = [
        [KeyboardButton('Full body flexibility'), KeyboardButton('Morning Yoga')],
        [KeyboardButton('Full body stretching')],
        [KeyboardButton('🔙 back')]
    ]
    markup = ReplyKeyboardMarkup(desing, one_time_keyboard=True, resize_keyboard=True)
    return markup


def strength():
    desing = [
        [KeyboardButton('Insane Six Pack'), KeyboardButton('Complex lower body')],
        [KeyboardButton('Complex upper body')],
        [KeyboardButton('🔙 back')]
    ]
    markup = ReplyKeyboardMarkup(desing, one_time_keyboard=True, resize_keyboard=True)
    return markup


def cardio():
    desing = [
        [KeyboardButton('HIIT'), KeyboardButton('Ligth cardio')],
        [KeyboardButton('Ploy metrics')],
        [KeyboardButton('🔙 back')]
    ]
    markup = ReplyKeyboardMarkup(desing, one_time_keyboard=True, resize_keyboard=True)
    return markup


def location_():
    design = [
        [KeyboardButton('🚅 Eltib berish', request_location=True)],
        [KeyboardButton('Boshqa filiallar')]
    ]
    markup = ReplyKeyboardMarkup(design, resize_keyboard=True, one_time_keyboard=True)
    return markup