def init(fn):
  def wrapper(update,context):
    chat = update.effective_chat
    if chat.type == 'supergroup' or chat.type == 'group':
      return fn(update,context)
    else:
      return False
  return wrapper