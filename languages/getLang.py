from config import Config
from core.database.repository.group_language import GroupLanguageRepository
from languages import (EN,IT)

def get(update, context):
    chat = update.effective_message.chat_id
    row = GroupLanguageRepository().getById([chat])
    if row is None:
        return None
    else:
        return row['languages']

def languages(update,context):
    LANGUAGE = get(update,context)

    if LANGUAGE == "" or LANGUAGE is None:
        LANGUAGE = Config.DEFAULT_LANGUAGE

    if LANGUAGE == "IT":
        setLang = IT.Italian
    elif LANGUAGE == "EN":
        setLang = EN.English

    languages.start = setLang["START_COMMAND"]
    languages.helps = setLang["HELP_COMMAND"]
    languages.group_info = setLang["GROUP_INFO"]
    languages.bot_welcome = setLang["BOT_WELCOME"]
    return LANGUAGE