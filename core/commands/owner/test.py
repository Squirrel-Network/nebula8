#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright SquirrelNetwork

import time
from core import decorators
import pandas
import matplotlib.pyplot as plt
from matplotlib import style


#from core.utilities.message import message
from core.utilities.functions import chat_object
#from telegram.utils.helpers import mention_html
from core.utilities.functions import chat_status_object_by_id
from core.database.repository.group import GroupRepository
from telegram.error import Unauthorized
from core.utilities.message import message
from core.database.db_connect import SqlAlchemyConnection
#from telegram import InlineKeyboardButton, InlineKeyboardMarkup
#from core.utilities.menu import build_menu

@decorators.owner.init
def init(update,context):
    chat = chat_object(update)

    db = SqlAlchemyConnection()
    engine = db.engine

    colors = [
        '#0066cc',
        '#cc0000',
        '#009933',
        '#009999',
        '#cc0066',
        '#cc6600',
        '#cccc00',
        '#66cc00',
        '#66cccc',
        '#6666ff'
        ]
    style.use('seaborn-pastel')

    # Read data from database
    df = pandas.read_sql("SELECT COUNT(*) AS message, u.tg_username as username, u.tg_id FROM nebula_updates nu INNER JOIN users u ON u.tg_id = nu.tg_user_id WHERE DATE BETWEEN DATE_SUB(NOW(), INTERVAL 30 DAY) AND NOW() AND nu.tg_group_id = %s GROUP BY nu.tg_user_id ORDER BY message DESC LIMIT 10" % chat.id, engine)
    #Reverse Dataframe
    df = df[::-1]
    df.plot(kind="barh", x="username", y="message",figsize=(18,10),grid=True,color=colors,title="Top 10 users with the most updates in the last 30 days in the group {}".format(chat.title))
    #Save Dataframe to Jpeg
    plt.savefig('/var/www/naos.hersel.it/charts/{}.jpg'.format(chat.id))

    caption = "TEST"
    img = "https://naos.hersel.it/charts/{}.jpg".format(chat.id)
    message(update, context, caption, 'HTML', 'photo', None, img)

#@decorators.owner.init
#def init(update,context):
    #context.job_queue.run_repeating(callback_all_chat,interval=10.0,first=0.0, name="[NIGHT_SCHEDULE_JOB]",context=update.effective_chat.id)

#@decorators.owner.init
#def init(update,context):
    #context.job_queue.run_repeating(callback_all_chat, interval=20.0, first=0.0, name="[GET_STATUS_ALL_GROUPS]")

def callback_all_chat(context):
    rows = GroupRepository().getAll()
    for a in rows:
        try:
            chat_id = a['id_group']
            x = chat_status_object_by_id(context,chat_id)
            time.sleep(2)
            print(x)
        except Unauthorized:
            print("NOT FOUND")

def callback_night(context):
    chat_id = context.job.context
    context.bot.send_message(chat_id=chat_id, text="TEST_NIGHT_SCHEDULE")
    print(chat_id)

def callback_chat(context):
    chat_id = context.job.context
    print(chat_id)
    #x = chat_status_object_by_id(context,chat_id)
    #context.bot.send_message(chat_id=chat_id, text="TEST_NIGHT_SCHEDULE")
    #print(x)