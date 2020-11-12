from core.database.repository.group import GroupRepository
from core import decorators

@decorators.owner.init
def init(update, context):
    chat = str(update.effective_chat.id)
    welcome = "Lorem Ipsum Dolor"
    rules = "Example Rules"
    community = 1
    lang = "EN"
    data = [(chat,welcome,rules,community,lang)]
    GroupRepository().add(data)