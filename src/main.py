import logging
from Enum_classes import *
from config import *
from aiogram import types, executor
from exceptions import *
import keyboards as kb
from functions import get_mess


@dp.message_handler(commands=["admin"])
async def start(message: types.Message):
    id = message.from_user.id
    if id not in admins:
        logging.debug(f"{id} not in admins")
        raise No_admins
    admin: Admin = admins.get(id)
    bot_message_id = admin.bot_message_id
    await bot.delete_message(chat_id=id, message_id=message.message_id)
    if bot_message_id != 0 and False:
        logging.info(str(admin))
        await bot.edit_message_text(chat_id=id,
                                    message_id=bot_message_id,
                                    text=get_mess(path="templates/about_by_admin"),
                                    reply_markup=kb.admin_main_keyboard)
        logging.info("edit mes successful")

    else:
        mes = await bot.send_message(chat_id=id,
                                     text=get_mess("templates/about_by_admin"),
                                     reply_markup=kb.admin_main_keyboard)
        admin.bot_message_id = mes.message_id
        admins.update_info(admin)


@dp.message_handler(lambda message: message.from_user.id in admins)
async def message_admin(message: types.Message):
    id = message.from_user.id
    admin = admins.get(id)
    if admin.flag is Admin_flags.input_user_by_statictic:
        if message.text.isdigit():
            user_id = int(message.text)
            user = users.get(user_id)
        else:
            username = message.text
            user = users.get_by_username(username)

        await bot.edit_message_text(chat_id=id,
                                    message_id=admin.bot_message_id,
                                    text="as",
                                    reply_markup=kb.NONE)


@dp.callback_query_handler(lambda call: call.from_user.id in admins)
async def call_admin(call: types.CallbackQuery):
    id = call.from_user.id
    admin = admins.get(id)
    if call.data == "user":
        await bot.edit_message_text(chat_id=id,
                                    message_id=admin.bot_message_id,
                                    text=get_mess("templates/action_admin_user"),
                                    reply_markup=kb.admin_users_keyboard)

    elif call.data == "statistic":
        await bot.edit_message_text(chat_id=id,
                                    message_id=admin.bot_message_id,
                                    text=get_mess("templates/about_statistic_by_admin"),
                                    reply_markup=kb.admin_users_statistic_keyboard)

    elif call.data == "one_user_statistic":
        await bot.edit_message_text(chat_id=id,
                                    message_id=admin.bot_message_id,
                                    text=get_mess("templates/input_user_id"),
                                    reply_markup=kb.admin_users_statistic_keyboard)
        admin.flag = Admin_flags.input_user_by_statictic



    elif call.data == "change_balance":
        await bot.edit_message_text(chat_id=id,
                                    text=get_mess("templates/input_user_id"),
                                    reply_markup=kb.admin_change_balance_keyboard)

    # elif call.data == "change_referral_lvl":
    #     await bot.edit_message_text(chat_id=id,
    #                                 text="",
    #                                 reply_markup=kb.)
    #
    # elif call.data == "change_status":
    #     await bot.edit_message_text(chat_id=id,
    #                                 text="",
    #                                 reply_markup=kb.)

    admins.update_info(admin)


if __name__ == "__main__":
    executor.start_polling(dispatcher=dp, skip_updates=True)
