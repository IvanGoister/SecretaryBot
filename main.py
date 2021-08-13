import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

import Customer_Information
from configuration import API_TOKEN, TikTokLink, InstaLink
import markups as NavButt
from Customer_Information import *


from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext



class CastomerInfo(StatesGroup):
    Name = State()
    Phone_number = State()
    Weight = State()
    BraSize = State()
    AssSize = State()
    EyeColor = State()
    Nationality = State()
    Religion = State()



# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):

    await bot.send_message(message.from_user.id, 'Привіт {0.first_name}, цей бот ще маленький, і поки що нічого не вміє'.format(message.from_user), reply_markup=NavButt.MainMenu)

@dp.message_handler(commands=['stop'])
async def send_welcom(message: types.Message):

    await bot.send_message(message.from_user.id, "Цього бота просто так не зупинити")


@dp.message_handler()
async def bot_message(message: types.Message):

    #await message.answer("message.text")
    #print(message.text)
    if message.text == '🪡 Ввести параметри тіла':

        #await bot.send_message(message.from_user.id, 'Можете ввести параметри тіла, але поки що я з ними нічого зробити не можу 🤷‍♀️')

        await bot.send_message(message.from_user.id, "Заповніть дані про себе\n Ваше ім'я")
        await CastomerInfo.Name.set()

        @dp.message_handler(state=CastomerInfo.Name)
        async def answer_Name(message: types.Message, state: FSMContext):
            answer = message.text
            await state.update_data(answer_Name=answer)

            await bot.send_message(message.from_user.id, "Номер телефону")
            await CastomerInfo.Phone_number.set()

        @dp.message_handler(state=CastomerInfo.Phone_number)
        async def answer_Phone_number(message: types.Message, state: FSMContext):
            answer = message.text
            await state.update_data(answer_Phone_number=answer)

            await bot.send_message(message.from_user.id, "Ваші дані прийняті 👌")
            data=await state.get_data()
            name=data.get('answer_Name')
            number=data.get('answer_Phone_number')
            await bot.send_message(message.from_user.id, "{Name}, ваш номер {Number}".format(Name=name, Number=number))
            print(message.from_user.id, message.from_user.first_name, " --write-- "+name+' '+number)
            await state.finish()





    elif message.text == '🧷 Посилання':
        await bot.send_message(message.from_user.id, 'Посилання \n ⬇️⬇️⬇️️️', reply_markup=NavButt.LinksMenu)
    elif message.text == '🔙 Головне меню':
        await bot.send_message(message.from_user.id, 'Головне меню \n ⬇️⬇️⬇️⬇️️', reply_markup=NavButt.MainMenu)
    elif message.text == '📷 Instagram':
        await bot.send_message(message.from_user.id, InstaLink)
    elif message.text == '📺 TikTok':
        await bot.send_message(message.from_user.id, TikTokLink)

    print(message.from_user.id, message.from_user.first_name, " --write-- ", message.text)

@dp.message_handler()
async def bot_message(message: types.Message):
    if message.text == '🪡 Ввести параметри тіла':
        await bot.send_message(message.from_user.id, 'Можете !!!!ввести параметри тіла, але поки що я з ними нічого зробити не можу 🤷‍♀️')

"""
@dp.message_handler(commands=['info'])
async def enter_test(message: types.Message):
    await bot.send_message(message.from_user.id, "Заповніть дані про себе\n Ваше ім'я")
    await CastomerInfo.Name.set()
@dp.message_handler(state=CastomerInfo.Name)
async def answer_Name(message: types.Message, state: FSMContext):
    answer=message.text
    await state.update_data(answer_Name=answer)

    await bot.send_message(message.from_user.id, "Заповніть дані про себе\n Номер телефону")
    await CastomerInfo.Phone_number.set()

@dp.message_handler(state=CastomerInfo.Phone_number)
async def answer_Phone_number(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(answer_Phone_number=answer)

    await bot.send_message(message.from_user.id, "Ваші дані прийняті 👌")
    await state.finish()







"""


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)


