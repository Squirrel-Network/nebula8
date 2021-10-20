from functools import wraps
from core.utilities.functions import get_owner_list

OWNER_LIST = get_owner_list()

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