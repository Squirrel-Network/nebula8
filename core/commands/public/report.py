from core.handlers.logs import telegram_loggers, staff_loggers
from core.utilities.message import message, reply_message

def init(update,context):
    if update.effective_message.reply_to_message:
        chat = update.effective_chat
        msg = update.effective_message.reply_to_message
        format_link = "https://t.me/c/{}/{}".format(str(chat.id)[3:],msg.message_id)
        format_message = "#Report\nGroup Id: <code>{}</code>\nGroup Title: {}\nMessage: <i>{}</i>\nLink: {}".format(chat.id,chat.title,msg.text,format_link)
        reply_message(update,context,"<b>Segnalazione effettuata! un admin prenderà in carico la tua richiesta!</b>")
        telegram_loggers(update,context,format_message)
        staff_loggers(update,context,format_message)
    else:
        chat = update.effective_chat
        user = "@"+update.message.from_user.username
        format_message = "#Report\nUser: {}\nGroup Id: <code>{}</code>\nGroup Title: {}".format(user,str(chat.id)[3:],chat.title)
        reply_message(update,context,"<b>Segnalazione effettuata! un admin prenderà in carico la tua richiesta!</b>")
        telegram_loggers(update,context,format_message)
        staff_loggers(update,context,format_message)