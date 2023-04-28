from aiogram import types
from jinja2 import Environment, PackageLoader, select_autoescape
from config import users, documents, countries


def create_keyboard(name_buttons: list, ) -> types.ReplyKeyboardMarkup:
    keyboard = types.ReplyKeyboardMarkup(row_width=len(name_buttons), resize_keyboard=True, one_time_keyboard=True)
    array = []
    for name_button in name_buttons:
        array.append(
            types.KeyboardButton(text=name_button)
        )
    keyboard.add(*array)
    return keyboard


def inl_create_keyboard(buttons: list, ):
    keyboard = types.InlineKeyboardMarkup(row_width=len(buttons), resize_keyboard=True)
    array = []
    for button in buttons:
        if len(button) == 1:
            array.append(
                types.InlineKeyboardButton(text=button[0])
            )
        if len(button) == 2:
            array.append(
                types.InlineKeyboardButton(text=button[0], url=button[1])
            )
        if len(button) == 3:
            array.append(
                types.InlineKeyboardButton(text=button[0], url=button[1], callback_data="pay")
            )
    keyboard.add(*array)
    return keyboard


def get_mess(path: str, **kwargs):
    env = Environment(
        loader=PackageLoader(package_name='main', package_path="", encoding="utf-8"),
        autoescape=select_autoescape(['html', 'xml'])
    )
    tmpl = env.get_template(path)
    return tmpl.render(kwargs)


def get_statistic_profile(id: int | str):
    if id.isdigit():
        id = int(id)
        user = users.get(id)
    else:
        user = users.get_by_username(id)
    if user:
        country = countries.get(user.country_id).name
        document = documents.get(user.country_id).name
        referral_boss = users.get_referral_boss(user.referral_boss_id)
        if referral_boss is None:
            referral_boss = "босса нет"
        mess = get_mess(path="templates/profile_user", lastname=user.lastname, firstname=user.firstname,
                        patronymic=user.patronymic, id=user.id, username=user.username, counrty=country,
                        document=document, withdrawal_account=user.withdrawal_account, balance=user.balance,
                        referral_link=user.referral_link, referral_boss=referral_boss)
        return mess


def get_full_statistic():
    count_user = len(users)
    count_user_today = users.get_users_by_time(time=24)
    count_user_week = users.get_users_by_time(time=168)
    count_user_month = users.get_users_by_time(time=720)
    count_not_verified_task = 0
    count_confirmed_task = 0
    count_rejected_task = 0
    current_balance = users.get_all_balance()
    total_earnings = users.get_total_earnings()
    balance_withdrawn = total_earnings - current_balance


if __name__ == "__main__":
    s = get_mess("templates/profile_user", firstname="s", patronymic="v", id=0,
                 username="sas", lastname="sa", counrty="sa", document="sasc", withdrawal_account="as",
                 balance=100)
    print(s)
