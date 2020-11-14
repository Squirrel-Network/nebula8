class Strings(object):
    SERVER_INFO = "<b>Server Status:</b>\nCpu: <code>{cpu}%</code>\nRam: <code>{ram}%</code>\nBoot Time: <code>{boot}</code>"
    ERROR_HANDLING = "Attention there was an error in sending the command\nContact support with the command /support"
    BAN_LOG = "<b>#Log User Banned!</b>\nUser_Id: {id}\n"\
              'Username: <a href="tg://user?id={id}">{username}</a>\n'\
              "Group: {chat}\n"\
              "Motivation: {motivation}"
    SUPERBAN_LOG = "<b>#Log User Superbanned!</b>\nUser_Id: {}\nMotivation: {}\nDatetime: <code>{}</code>\nOperator_id: {}"