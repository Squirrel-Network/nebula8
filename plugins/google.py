from core.utilities.message import message

def init(update, context):
    msg=str(update.message.text[7:]).strip()
    if msg != "":
        url = "https://www.google.com/search?&q={0}".format(msg.replace(' ','+'))
        message(update,context,url)
    else:
        message(update,context, text="Devi digitare un criterio di ricerca!")