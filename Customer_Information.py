from main import *
import main
#from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext

class CustomerInfo(StatesGroup):
    Name = State()
    Phone_number = State()
    Weight = State()
    BraSize = State()
    AssSize = State()
    EyeColor = State()
    Nationality = State()
    Religion = State()

@dp.message_handler(commands=['info'], state=None)
async def enter_test(message: types.Message):
    await bot.send_message(message.from_user.id, "Заповніть дані про себе\n Ваше ім'я")
    await CustomerInfo.Name.set()
@dp.message_handler(state=CustomerInfo.Name)
async def answer_Name(message: types.Message, state: FSMContext):
    answer=message.text
    await state.update_data(answer_Name=answer)

    await bot.send_message(message.from_user.id, "Заповніть дані про себе\n Номер телефону")
    await CustomerInfo.Phone_number.set()

@dp.message_handler(state=CustomerInfo.Phone_number)
async def answer_Phone_number(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(answer_Phone_number=answer)

    await bot.send_message(message.from_user.id, "Ваші дані прийняті 👌")
    await state.finish()


def oprosnik():
    @dp.message_handler(commands=['info'], state=None)
    async def enter_test(message: types.Message):
        await bot.send_message(message.from_user.id, "Заповніть дані про себе\n Ваше ім'я")
        await CustomerInfo.Name.set()

    @dp.message_handler(state=CustomerInfo.Name)
    async def answer_Name(message: types.Message, state: FSMContext):
        answer = message.text
        await state.update_data(answer_Name=answer)

        await bot.send_message(message.from_user.id, "Заповніть дані про себе\n Номер телефону")
        await CustomerInfo.Phone_number.set()

    @dp.message_handler(state=CustomerInfo.Phone_number)
    async def answer_Phone_number(message: types.Message, state: FSMContext):
        answer = message.text
        await state.update_data(answer_Phone_number=answer)

        await bot.send_message(message.from_user.id, "Ваші дані прийняті 👌")
        await state.finish()
    return CustomerInfo