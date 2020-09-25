def init(fn):
  def wrapper(*args,**kwargs):
    message = args[0].message
    if message.chat.type == 'supergroup' or message.chat.type == 'group':
      return fn(*args,**kwargs)
    else:
      return False
  return wrapper