def init(fn):
  def wrapper(*args,**kwargs):
    message = args[0].message
    if message.chat.type == 'private':
      return fn(*args,**kwargs)
    else:
      print("Private Only")
      return False
  return wrapper