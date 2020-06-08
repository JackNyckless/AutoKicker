import vk_api
from vk_api.bot_longpoll import VkBotEventType, VkBotLongPoll
import requests


#Ключ доступа сообщества - УКАЗАТЬ!
token = 'f6cc9bf9cbe5021acd93c1ad71e478bde987d0e209f0cd26fd575a7fbc8f44775d057cbce2e5ff2d2c0eb'

#id сообщества (положительное число) - УКАЗАТЬ!
group = 144234283

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
