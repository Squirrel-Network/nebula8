from core.handlers.logs import telegram_loggers, staff_loggers
from core.utilities.message import reply_message
from core.utilities.strings import Strings

def init(update,context):
    chat = update.effective_chat
    if str(update.effective_message.text).lower().startswith("@admin"):
        if update.effective_message.reply_to_message:
            msg = update.effective_message.reply_to_message
            format_link = "https://t.me/c/{}/{}".format(str(chat.id)[3:],msg.message_id)
            format_message = Strings.REPORT_MSG.format(chat.id,chat.title,msg.text,format_link)
            reply_message(update,context,"<b>Segnalazione effettuata! un admin prenderà in carico la tua richiesta!</b>")
            telegram_loggers(update,context,format_message)
            staff_loggers(update,context,format_message)
        else:
            msg_id = update.effective_message.message_id
            user_id = update.message.from_user.id
            user_first = update.message.from_user.first_name
            format_link = "https://t.me/c/{}/{}".format(str(chat.id)[3:],msg_id)
            format_message = '#Report\nUser: <a href="tg://user?id={}">{}</a>\nGroup Id: <code>{}</code>\nGroup Title: {}\nLink: {}'.format(user_id,user_first,str(chat.id)[3:],chat.title,format_link)
            reply_message(update,context,"<b>Segnalazione effettuata! un admin prenderà in carico la tua richiesta!</b>")
            telegram_loggers(update,context,format_message)
            staff_loggers(update,context,format_message)