from functools import wraps 
from core.database.repository.user import UserRepository


def get_owner_list() -> list:
    rows = UserRepository().getOwners()
    arr_owners = []
    for a in rows:
        owners = int(a['tg_id'])
        arr_owners.append(owners)
    return arr_owners

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