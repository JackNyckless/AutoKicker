import vk_api
from vk_api.bot_longpoll import VkBotEventType, VkBotLongPoll
import requests


#Ключ доступа сообщества - УКАЗАТЬ!
token = '725b7f6741c618f049f1d4336563c215b99df229f6425e5a34e2ea30e30d8ffacd4b12595dd7f4c1bb541'

#id сообщества (положительное число) - УКАЗАТЬ!
group = 144234283

#Сервисный ключ - УКАЗАТЬ!
access_key = 'b21afb1850961c0f70f7fee938243317e5a4fef14e16f348d37a0e5985b3ce10c576ba47d22813cbc9250'



vk = vk_api.VkApi(token=token)

longpoll = VkBotLongPoll(vk, group)




for event in longpoll.listen():

    if event.type == VkBotEventType.GROUP_JOIN:

        id = event.object.user_id
        requests.post('https://api.vk.com/method/groups.removeUser', data={'access_token': access_key,
                                                                                  "group_id": group,
                                                                                  "user_id": id,
                                                                                  'v': "5.101"})
