from aiogram import Dispatcher, types
from read_response import read_messages
from validator import is_valid_article
from wildberrys_scraper import get_product_position
from utils import join_request


async def on_start(message: types.Message):
    response = await read_messages()
    await message.answer(response['start'])


async def start_cmd_handler(message: types.Message):
    await on_start(message)


async def show_result_handler(message: types.Message):

    response = await read_messages()
    request = message.text.strip().split()

    if not await is_valid_article(request[-1]):
        await message.answer(response['invalid_article'].format(request[-1]))
    else:
        response = await get_product_position(join_request(request[:-1]),
                                              int(request[-1]))
        await message.answer(response)


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(
        start_cmd_handler,
        commands=['start', 'help']
    )
    dp.register_message_handler(
        show_result_handler,
        content_types=types.ContentTypes.TEXT
    )
