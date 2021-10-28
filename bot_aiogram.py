import requests
import datetime
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from config import token_weather, TOKEN

# OBJECT OF CLASS
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# BUTTONS
single_button_1 = KeyboardButton('☁Check weather☁')

world_for_buttons1 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
world_for_buttons1.add(single_button_1)

single_button_2 = KeyboardButton('Отправить свой контакт ☎️', request_contact=True)
single_button_3 = KeyboardButton('Отправить свою локацию 🗺️', request_location=True)
world_for_buttons2 = ReplyKeyboardMarkup(resize_keyboard=True)
world_for_buttons2.add(single_button_2, single_button_3)


# FUNCTION
@dp.message_handler(commands='start')
async def start_command(message: types.Message):
    await bot.send_message(message.from_user.id, "Hi, i'm bot..", reply_markup=world_for_buttons1)


@dp.message_handler()
async def process_hi6_command(message: types.Message):
    if 'contact' in message:
        await bot.send_message(message.from_user.id, "You can send me:", reply_markup=world_for_buttons2)


@dp.message_handler()
async def get_weather(message: types.Message):
    dict_emoji_weather = {'Clouds': '☁',
                          'Clear': 'Clear sky',
                          'Snow': '❄',
                          'Rain': '🌧️',
                          'Thunderstorm': '⛈'
                          }
    try:
        r = requests.get(
            f'http://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={token_weather}&units=metric')
        data = r.json()

        city = data['name']
        weather = data['main']['temp']
        humidity = data['main']['humidity']
        sunrise = datetime.datetime.fromtimestamp(data['sys']['sunrise']).strftime('%H:%M:%S')
        sunset = datetime.datetime.fromtimestamp(data['sys']['sunset']).strftime('%H:%M:%S')
        len_of_the_day = datetime.datetime.fromtimestamp(data['sys']['sunset']) - \
                         datetime.datetime.fromtimestamp(data['sys']['sunrise'])
        code_emoji_weather = data['weather'][0]['main']
        if code_emoji_weather in dict_emoji_weather:
            emoji_weather = dict_emoji_weather[code_emoji_weather]
        else:
            emoji_weather = ""
        await bot.send_message(message.from_user.id,
                               f'***{datetime.datetime.now().strftime("%d-%m-%Y")}***\n'
                               f'       ***{datetime.datetime.now().strftime("%H:%M")}***\n'
                               f'Weather in the: {city}\n'
                               f'Temp: {weather}°C {emoji_weather}\n'
                               f'Humidity: {humidity}%\n'
                               f'Sunrise: {sunrise} AM\n'
                               f'Sunset: {sunset} PM\n'
                               f'Length of the day: {len_of_the_day}\n'
                               )
    except:
        await bot.send_message(message.from_user.id, 'Write the city: ')


@dp.message_handler()
async def get_courses():
    pass


if __name__ == '__main__':
    executor.start_polling(dp)
