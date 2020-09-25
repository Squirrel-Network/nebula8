from functools import wraps
from config import Config

OWNER_LIST= Config.OWNER

def init(func):
    @wraps(func)
    def wrapped(update, context):
        if update.effective_user is not None:
            user_id = update.effective_user.id
            if user_id not in OWNER_LIST:
                print("Unauthorized access denied for {}.".format(user_id))
                return
        else:
            return False
        return func(update, context)
    return wrapped