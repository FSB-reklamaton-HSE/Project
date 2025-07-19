import asyncio
import os

from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, F
from aiogram.types import CallbackQuery, Message
from aiogram.filters import CommandStart, Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.enums.parse_mode import ParseMode
from aiogram.client.bot import DefaultBotProperties

from llama_generate import generate_text
from keyboards import (
    ikb_start_desription
)
from texts import (
    START_MESSAGE,
    QUESTION_1,
    QUESTION_2,
    QUESTION_3,
    QUESTION_4,
    QUESTION_5,
    INCORRECT_COMMAND,
    DESCRIPTION_MESSAGE,
    PROMPT
)



# Загрузка BOT_TOKEN из .env файла
load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")


# Инициализация бота с HTML-разметкой по умолчанию
bot = Bot(
    token=BOT_TOKEN,
    default=DefaultBotProperties(parse_mode=ParseMode.HTML)
)
dp = Dispatcher()


class OrderAdd(StatesGroup):
    question_1 = State()
    question_2 = State()
    question_3 = State()
    question_4 = State()
    question_5 = State()


@dp.message(CommandStart())
async def start(message: Message) -> None:
    await message.answer(text=(START_MESSAGE + '\n\n' + DESCRIPTION_MESSAGE), reply_markup=ikb_start_desription())


@dp.message(Command('create_description'))
async def add_card_command(message: Message) -> None:
    await message.answer(text=DESCRIPTION_MESSAGE, reply_markup=ikb_start_desription())


@dp.callback_query(F.data == 'start_desription')
async def cb_start(callback: CallbackQuery, state: FSMContext):
    await callback.answer()
    await state.set_state(OrderAdd.question_1)
    await state.update_data(
        answers=[f"Меня зовут: {callback.from_user.full_name}"]
    )
    await callback.message.answer(QUESTION_1)


@dp.message(OrderAdd.question_1)
async def answer1(message: Message, state: FSMContext):
    data = await state.get_data()
    ans = data.get("answers", [])
    ans.append(message.text)
    await state.update_data(answers=ans)
    await state.set_state(OrderAdd.question_2)
    await message.answer(QUESTION_2)
    
@dp.message(OrderAdd.question_2)
async def answer2(message: Message, state: FSMContext):
    data = await state.get_data()
    ans = data.get("answers", [])
    ans.append(message.text)
    await state.update_data(answers=ans)
    await state.set_state(OrderAdd.question_3)
    await message.answer(QUESTION_3)
    
@dp.message(OrderAdd.question_3)
async def answer3(message: Message, state: FSMContext):
    data = await state.get_data()
    ans = data.get("answers", [])
    ans.append(message.text)
    await state.update_data(answers=ans)
    await state.set_state(OrderAdd.question_4)
    await message.answer(QUESTION_4)
    
@dp.message(OrderAdd.question_4)
async def answer4(message: Message, state: FSMContext):
    data = await state.get_data()
    ans = data.get("answers", [])
    ans.append(message.text)
    await state.update_data(answers=ans)
    await state.set_state(OrderAdd.question_5)
    await message.answer(QUESTION_5)
    
@dp.message(OrderAdd.question_5)
async def answer5(message: Message, state: FSMContext):
    data = await state.get_data()
    ans = data.get("answers", [])
    ans.append(message.text)
    # print(" ".join(ans))
    desripton = generate_text(text=(". ".join(ans)), prompt=PROMPT)
    await state.clear()
    await message.answer(text=desripton)




@dp.message(F.text)
async def other_text(message: Message) -> None:
    """
    Обработчик прочих текстовых сообщений.
    
    Args:
        message (Message): Входящее сообщение
    """
    if message.chat.type == "private":
        await message.answer(text=INCORRECT_COMMAND)


async def main() -> None:
    """Основная функция запуска бота."""
    await dp.start_polling(bot)


if __name__ == "__main__":   
    asyncio.run(main())
