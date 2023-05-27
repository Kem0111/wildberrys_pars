from config import dp
from aiogram.utils import executor


def start_bot():
    """
    Start the bot and run it in polling mode.
    """
    from handlers import client

    client.register_handlers_client(dp)
    executor.start_polling(dp, skip_updates=True)


if __name__ == '__main__':
    start_bot()
