from core import decorators
from core.utilities.menu import build_menu
from languages.getLang import languages
from core.commands.admin import set_lang
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ChatPermissions
from core.database.repository.group import GroupRepository
from telegram.ext import CallbackQueryHandler

permission_false = ChatPermissions(
    can_send_messages=False,
    can_send_media_messages=False,
    can_send_polls=False,
    can_send_other_messages=False,
    can_add_web_page_previews=False,
    can_change_info=False,
    can_invite_users=False,
    can_pin_messages=False
    )
permission_true = ChatPermissions(
    can_send_messages=True,
    can_send_media_messages=True,
    can_send_polls=True,
    can_send_other_messages=True,
    can_add_web_page_previews=True,
    can_change_info=False,
    can_invite_users=False,
    can_pin_messages=False
    )

def keyboard_settings(update,context,editkeyboard = False):
    bot = context.bot
    chat = update.message.chat_id
    group = GroupRepository().getById(chat)
    list_buttons = []
    list_buttons.append(InlineKeyboardButton('Welcome %s' % ('✅' if group['set_welcome'] == 1 else '❌'), callback_data='setWelcome'))
    list_buttons.append(InlineKeyboardButton('Silence %s' % ('✅' if group['set_silence'] == 1 else '❌'), callback_data='setSilence'))
    list_buttons.append(InlineKeyboardButton('Languages', callback_data='lang'))
    list_buttons.append(InlineKeyboardButton('Filters', callback_data='Filters'))
    list_buttons.append(InlineKeyboardButton("Close", callback_data='close'))
    menu = build_menu(list_buttons,2)
    if editkeyboard == False:
        keyboard_menu = bot.send_message(chat,"Group Settings",reply_markup=InlineKeyboardMarkup(menu),parse_mode='HTML')
    if editkeyboard == True:
        keyboard_menu = bot.edit_message_reply_markup(chat,update.message.message_id,reply_markup=InlineKeyboardMarkup(menu))
    return keyboard_menu

def keyboard_filters(update,context,editkeyboard = False):
    bot = context.bot
    chat = update.message.chat_id
    group = GroupRepository().getById(chat)
    list_buttons = []
    list_buttons.append(InlineKeyboardButton('Exe Filters %s' % ('✅' if group['exe_filter'] == 1 else '❌'), callback_data='exe_filters'))
    list_buttons.append(InlineKeyboardButton('Zip Filters', callback_data='zip_filters'))
    list_buttons.append(InlineKeyboardButton('TarGZ Filters', callback_data='targz_filters'))
    list_buttons.append(InlineKeyboardButton("Close", callback_data='close'))
    menu = build_menu(list_buttons,2)
    if editkeyboard == False:
        keyboard_menu = bot.send_message(chat,"Filters Settings",reply_markup=InlineKeyboardMarkup(menu),parse_mode='HTML')
    if editkeyboard == True:
        keyboard_menu = bot.edit_message_reply_markup(chat,update.message.message_id,reply_markup=InlineKeyboardMarkup(menu))
    return keyboard_menu

@decorators.public.init
@decorators.admin.user_admin
@decorators.delete.init
def init(update,context):
    keyboard_settings(update,context)

@decorators.admin.user_admin
def update_settings(update,context):
    bot = context.bot
    languages(update,context)
    query = update.callback_query
    chat = update.effective_message.chat_id
    group = GroupRepository().getById(chat)
    # Set Welcome
    if query.data == 'setWelcome':
        row = group['set_welcome']
        if row == 1:
            data = [(0,chat)]
            GroupRepository().SetWelcome(data)
            return keyboard_settings(query,context,True)
        else:
            data = [(1,chat)]
            GroupRepository().SetWelcome(data)
            return keyboard_settings(query,context,True)
    # Set Global Silence
    if query.data == 'setSilence':
        row = group['set_silence']
        if row == 0:
            data = [(1,chat)]
            GroupRepository().setSilence(data)
            bot.set_chat_permissions(update.effective_chat.id, permission_false)
            return keyboard_settings(query,context,True)
        else:
            data = [(0,chat)]
            GroupRepository().setSilence(data)
            bot.set_chat_permissions(update.effective_chat.id, permission_true)
            return keyboard_settings(query,context,True)
    if query.data == 'Filters':
        return keyboard_filters(query, context, True)
    if query.data == 'exe_filters':
        row = group['exe_filter']
        if row == 0:
            data = [(1, chat)]
            GroupRepository().setExeFilter(data)
            query.edit_message_text("<b>EXE FILTERS ACTIVATED!</b>",parse_mode='HTML')
        else:
            data = [(0, chat)]
            GroupRepository().setExeFilter(data)
            query.edit_message_text("<b>EXE FILTERS DEACTIVATED!</b>",parse_mode='HTML')
    if query.data == 'zip_filters':
        query.edit_message_text("ZIP FILTERS ACTIVATED\nUnder Construction",parse_mode='HTML')
    if query.data == 'targz_filters':
        query.edit_message_text("TARGZ FILTERS ACTIVATED\nUnder Construction",parse_mode='HTML')
    if query.data == 'lang':
        set_lang.init(update, context)
        query.edit_message_text("You have closed the settings menu and open languages menu",parse_mode='HTML')
    # Close Menu
    if query.data == 'close':
        query.edit_message_text(languages.close_menu_msg, parse_mode='HTML')