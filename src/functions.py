from aiogram import types
from jinja2 import Environment, PackageLoader, select_autoescape

env = Environment(
    loader=PackageLoader(package_name='main', package_path=""),
    autoescape=select_autoescape(['html', 'xml'])
)


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
    tmpl = env.get_template(path)
    return tmpl.render()


if __name__ == "__main__":
    print(get_mess("templates/about_by_admin"))
