import wikipedia as wiki
from core.utilities.message import message
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from core.utilities.menu import build_menu
from core.database.repository.group import GroupRepository

def init(update, context):
    arg = update.message.text[5:]
    chat = update.effective_message.chat_id
    group = GroupRepository().getById(chat)
    lang = group['languages']
    wiki.set_lang(lang.lower())
    try:
        pg = wiki.page(wiki.search(arg)[0])
        title = pg.title
        pg_url = pg.url
        define = pg.summary
        button_list = [InlineKeyboardButton("Go to ==>", url=pg_url)]
        reply_markup = InlineKeyboardMarkup(build_menu(button_list, n_cols=1))
        text = "*{}:*\n\n{}".format(title, define)
        update.message.reply_markdown(text, reply_markup=reply_markup)
    except:
        message(update, context, "Sorry {} I didn't find what you were looking for".format(update.message.from_user.first_name))