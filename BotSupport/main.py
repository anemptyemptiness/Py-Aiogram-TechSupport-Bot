from aiogram import executor

from loader import dp
import handlers, middlewares
from set_bot_commands import set_default_commands

async def on_startup(dispatcher):
    # Уведомляет про запуск
    print("Бот успешно запущен")
    await set_default_commands(dispatcher)

if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)