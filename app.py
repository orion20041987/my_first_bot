# from aiogram import executor
#
# from loader import dp

# print('new string')

#
# import middlewares, filters, handlers
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands
from loader import db


async def on_startup(dp):
    # Уведомляет про запуск
    await on_startup_notify(dp)
    await set_default_commands(dp)
    print(db.select_all())


if __name__ == '__main__':
    from aiogram import executor
    from handlers import dp

    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)
