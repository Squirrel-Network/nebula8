#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright SquirrelNetwork
# Credits LakyDev

import json
from core.database.redis_connect import RedisConnect
from time import time


class Flood_Manager_Python(RedisConnect):
    def check_flood_wait(self,update) -> int:
        # 0 = No Flood
        # 1 = Flood Start
        # 2 = Flood Wait

        user_id = update.effective_user.id
        chat_id = update.effective_chat.id

        id_data = f'{chat_id}:{user_id}'
        now_time = int(time())
        if not self.hexists('groups',chat_id):
            self.update_group_data(chat_id, 5, 5, 30)
            raise Exception('Chat not found')
        else:
            chat_data = json.loads(self.hget('groups',chat_id))
            self.hget('groups', chat_id)
            get_data = {
                'messages': 1,
                'last_message': now_time,
            }
            if self.hexists('flood_wait', id_data):
                get_data = json.loads(self.hget('flood_wait', id_data))
                if get_data['messages'] >= chat_data['max_message']:
                    mute_time = (get_data['last_message'] + chat_data['mute_time']) - now_time
                    if mute_time > 0:
                        return 2
                    else:
                        get_data['last_message'] = now_time
                        get_data['messages'] = 1
                else:
                    limit_exceeded = now_time - get_data['last_message'] > chat_data['max_time']
                    get_data['messages'] = 0 if limit_exceeded else get_data['messages'] + 1
                    get_data['last_message'] = now_time if limit_exceeded else get_data['last_message']
            self.hset('flood_wait', id_data, json.dumps(get_data))
            return 1 if get_data['messages'] >= chat_data['max_message'] else 0

    def update_group_data(self, chat_id, max_time, max_message, mute_time):
        self.hset('groups', chat_id, json.dumps({'max_time': max_time, 'max_message': max_message,'mute_time': mute_time}))


#print(check_flood_wait('-1001497049823', 1065189838))
