from core import decorators
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

@decorators.admin.user_admin
def init(update,context):
    pass
    #buttons = []
    #buttons.append(InlineKeyboardButton('TEST %s' % ('✅' if row['settings'] == 1 else '❌'), callback_data='data'))