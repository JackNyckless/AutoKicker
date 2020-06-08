import vk_api
from vk_api.bot_longpoll import VkBotEventType, VkBotLongPoll
import requests


#Ключ доступа сообщества - УКАЗАТЬ!
token = 'a4d703b179d1e117aea4d2603f7b5ce9c7b48f17c15440ef904bcae55d1d579873168d322ba482aac9519'

#id сообщества (положительное число) - УКАЗАТЬ!
group = 152524817

#Сервисный ключ - УКАЗАТЬ!
access_key = 'cf8ec30ead56531f5776d0d7bf458653c3f312b910e5b0b9f9a7a2cc34304643f7219de6dadec03765f8d'



vk = vk_api.VkApi(token=token)

longpoll = VkBotLongPoll(vk, group)




for event in longpoll.listen():

    if event.type == VkBotEventType.GROUP_JOIN:

        id = event.object.user_id
        requests.post('https://api.vk.com/method/groups.removeUser', data={'access_token': access_key,
                                                                                  "group_id": group,
                                                                                  "user_id": id,
                                                                                  'v': "5.101"})
