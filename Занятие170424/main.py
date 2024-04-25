import asyncio

from aiogram import Bot, Dispatcher, Router, F
from aiogram.types import Message, BotCommand, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from aiogram.filters import Command 

bot = Bot(token="6672145932:AAEHwzobK6mPnRVqqq0AK--r_dmcCtY4Vv4")
dp = Dispatcher()

router = Router()

@router.message(Command ("start" ))
async def start_handler(msg: Message):
    await bot.set_my_commands([
        BotCommand(command= 'start' ,description='Запуск бота'), 
        BotCommand(command= 'help', description='Справка'), 
        BotCommand(command='delete', description='Отчислиться'),
    ])

    inline_markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Вперёд', callback_data='Next')]
    ])
    await msg.answer(text="Страница 1", reply_markup=inline_markup)


@router.callback_query(F.data == 'Next')
async def callback_query_handler(callback_query: CallbackQuery):
    inline_markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Назад', callback_data='back')]
    ])
    await callback_query.message.edit_text(text='Страница 2', reply_markup=inline_markup)

@router. callback_query(F.data == 'back')
async def next_handler(callback_query: CallbackQuery):
    inline_markup = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Вперёд', callback_data='Next')]
    ])
    await callback_query.message.edit_text(
        text="Страница 1",
        reply_markup=inline_markup)


async def main():
    await dp.start_polling(bot)


dp.include_routers(router)

if __name__ == '__main__':
    asyncio.run(main())