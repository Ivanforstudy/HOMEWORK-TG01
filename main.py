import asyncio
import requests
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart, Command
from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher()

# Здесь вам нужно вставить ваш API-ключ от OpenWeatherMap
WEATHER_API_KEY = '2c17201e9c93190d6d99de4b64a98cbe'
WEATHER_URL = 'http://api.openweathermap.org/data/2.5/weather'

@dp.message(Command('weather'))
async def get_weather(message: types.Message):
    city = 'Санкт-Петербург'
    params = {
        'q': city,
        'appid': WEATHER_API_KEY,
        'units': 'metric',  # Используем метрическую систему для температуры
        'lang': 'ru'        # Запрашиваем данные на русском языке
    }
    response = requests.get(WEATHER_URL, params=params)
    data = response.json()

    if response.status_code == 200:
        temperature = data['main']['temp']
        weather_description = data['weather'][0]['description']
        await message.answer(f'Погода в {city}:\nТемпература: {temperature}°C\nОписание: {weather_description}')
    else:
        await message.answer('Не удалось получить данные о погоде.')

@dp.message(Command('help'))
async def help_command(message: types.Message):
    await message.answer('Этот бот умеет выполнять команды: \n /start \n /help \n /weather')

@dp.message(CommandStart)
async def start_command(message: types.Message):
    await message.answer('Приветики! Я бот!')



async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())