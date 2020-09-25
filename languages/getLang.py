from config import Config
from core.database.repository.get_group_language import GroupLanguageRepository
from languages import (EN,IT)

def get(update, context):
    chat = update.effective_message.chat_id
    row = GroupLanguageRepository().getById([chat])
    return row['languages']

def languages(update,context):
    LANGUAGE = get(update,context)

    if LANGUAGE == "IT":
        setLang = IT.Italian
    elif LANGUAGE == "EN":
        setLang = EN.English

    languages.start = setLang.START_COMMAND
    languages.helps = setLang.HELP_COMMAND
    return LANGUAGE