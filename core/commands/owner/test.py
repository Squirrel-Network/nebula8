import json
from core.database.repository.group import GroupRepository
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from core.utilities.message import message
from core.utilities.menu import build_menu
from core import decorators

def buttons_welcome(update,context):
    chat = update.effective_message.chat_id
    buttons = GroupRepository().getById(chat)
    if buttons:
        try:
            x = buttons['welcome_buttons']
            y = json.loads(x)
            arr_buttons = []
            for key, value in y.items():
                arr_buttons.append(InlineKeyboardButton(text=key, url=value))
            menu = build_menu(arr_buttons, 2)
            var = update.message.reply_text("TEST", reply_markup=InlineKeyboardMarkup(menu),parse_mode='HTML')
            return var
        except ValueError:
            print("no")


@decorators.owner.init
def init(update,context):
    buttons_welcome(update,context)