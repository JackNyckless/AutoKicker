import vk_api
from vk_api.bot_longpoll import VkBotEventType, VkBotLongPoll
import requests


#Ключ доступа сообщества - УКАЗАТЬ!
token = ''

#id сообщества (положительное число) - УКАЗАТЬ!
group =

#Сервисный ключ - УКАЗАТЬ!
access_key = ''



vk = vk_api.VkApi(token=token)

longpoll = VkBotLongPoll(vk, group)




for event in longpoll.listen():

    if event.type == VkBotEventType.GROUP_JOIN:

        id = event.object.user_id
        requests.post('https://api.vk.com/method/groups.removeUser', data={'access_token': access_key,
                                                                                  "group_id": group,
                                                                                  "user_id": id,
                                                                                  'v': "5.101"})