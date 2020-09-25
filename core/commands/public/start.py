from languages.getLang import languages

def init(update, context):
    bot = context.bot
    languages(update,context)
    bot.send_message(update.effective_chat.id, languages.helps)