import logging
from aiogram import Bot, Dispatcher, executor, types
from configuration import API_TOKEN, TikTokLink, InstaLink
import markups as NavButt


# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):

    await bot.send_message(message.from_user.id, 'Привіт {0.first_name}, цей бот ще маленький, і поки що нічого не вміє'.format(message.from_user), reply_markup=NavButt.MainMenu)

@dp.message_handler(commands=['stop'])
async def send_welcome(message: types.Message):

    await bot.send_message("Цього бота просто так не зупинити")


@dp.message_handler()
async def bot_message(message: types.Message):

    #await message.answer("message.text")
    #print(message.text)
    if message.text == '🪡 Ввести параметри тіла':
        await bot.send_message(message.from_user.id, 'Можете ввести параметри тіла, але поки що я з ними нічого зробити не можу 🤷‍♀️')

    elif message.text == '🧷 Посилання':
        await bot.send_message(message.from_user.id, 'Посилання \n ⬇️⬇️⬇️️️', reply_markup=NavButt.LinksMenu)
    elif message.text == '🔙 Головне меню':
        await bot.send_message(message.from_user.id, 'Головне меню \n ⬇️⬇️⬇️⬇️️', reply_markup=NavButt.MainMenu)
    elif message.text == '📷 Instagram':
        await bot.send_message(message.from_user.id, InstaLink)
    elif message.text == '📺 TikTok':
        await bot.send_message(message.from_user.id, TikTokLink)

    print(message.from_user.id, message.from_user.first_name, " --write-- ", message.text)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)


