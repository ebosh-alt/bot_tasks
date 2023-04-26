from aiogram import types


def create_keyboard(name_buttons: list | dict, ) -> types.InlineKeyboardMarkup:
    keyboard = types.InlineKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
    array = []

    for name_button in name_buttons:
        if type(name_button) is list:
            array.append(
                types.InlineKeyboardButton(text=name_button, callback_data=name_button)
            )
        else:
            array.append(
                types.InlineKeyboardButton(text=name_button, callback_data=name_buttons[name_button])
            )
    keyboard.add(*array)
    return keyboard


admin_main_name_button = {
    "👥 Пользователи": "users"
}

admin_users_name_button = {
    "Статистика": "statistic",
    "Изменение баланса": "change_balance",
    "Изменение рефералльного уровня": "change_referral_lvl",
    "Измение статуса": "change_status",
    "Назад": "back_to_main_keyboard_admin"
}

admin_users_statistic_keyboard = {
    "Одного пользователя": "one_user_statistic",
    "Общая статистика": "full_statistic",
    "Назад": "users"
    }

admin_change_balance_name_button = {
    "Увеличить": "increase",
    "Уменьшить": "decrease"
}

admin_back_to_choice_statistic = create_keyboard({"Назад": "statistic"})
admin_main_keyboard = create_keyboard(admin_main_name_button)
admin_users_keyboard = create_keyboard(admin_users_name_button)
admin_users_statistic_keyboard = create_keyboard(admin_users_statistic_keyboard)
admin_change_balance_keyboard = create_keyboard(admin_change_balance_name_button)
NONE = types.InlineKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)














