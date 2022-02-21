#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright SquirrelNetwork

import datetime
from core.utilities.functions import member_status_object, chat_status_object
from core.database.repository.dashboard import DashboardRepository
from core.utilities.message import message

def init(update,context):
    reply = update.message.reply_to_message
    if reply:
        message(update,context,"Questo comando al momento non può essere utilizzato in risposta ad un messaggio!")
    else:
        user_status = member_status_object(update,context)
        chat_status = chat_status_object(update, context)
        if user_status.status == 'creator':
            user = user_status.user
            username = "@"+user.username
            save_date = datetime.datetime.utcnow().isoformat()
            row = DashboardRepository().getById(user.id)
            if row:
                if row['enable'] == 0:
                    message(update,context,"Mi dispiace sei stato disabilitato a questa funzionalità, Contatta un amministratore su: https://t.me/nebulabot_support")
                else: 
                    data = [(username, save_date, user.id, chat_status.id)]
                    DashboardRepository().update(data)
                    message(update,context,"Ho aggiornato i dati sul database!")
            else:
                data = [(user.id,username,chat_status.id,1,save_date,save_date)]
                DashboardRepository().add(data)
                message(update,context,"<i>UNDER CONSTRUCTION {}</i>\n\nSeguici su: https://github.com/Squirrel-Network/nebula8".format(data))
        else:
            msg = "Non sei il proprietario del gruppo non puoi usare questo comando"
            message(update,context,msg)