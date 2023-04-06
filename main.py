import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import random
import time
import json

group_id=219712405
token = "vk1.a.yOFWwqiumU60fgdATHGfC_vpVAQtviFS1Jgr6Bk4r5gWOkJI4ZzAPn71KcsSVB-P-TXLChr-Z8AhnROgoxwUHb_fbQvEJASMlzC-mJ2YfrOUKOi81wf-HKLmjmDsx8Bj6ukskuYt7k4q5mlrbuaeZ2MRQjz9-N4PIqK0L40lSfVtZkH9WFJKPDPbc9ZPaqn3kQUh9RICXKzjRtePjETJBw"
vk_session = vk_api.VkApi(token=token)
longpoll = VkBotLongPoll(vk_session, group_id)

def read(filename):
    with open(filename) as f:
        return json.load(f)

def write(data,filename):
    data=json.dumps(data)
    data=json.loads(str(data))
    with open(filename, 'w') as f:
        json.dump(data,f)

def main():
    group_list={"писечки":10,"попочки":11}
    data=read('data.json')
    for event in longpoll.listen():
        if event.type == VkBotEventType.MESSAGE_NEW:
            if event.obj['message']['text'].lower() in ["!инфо"]:
                vk_session.method('messages.send',{'peer_id':event.obj['message']['peer_id'], 'message': f"Группа {data[str(event.obj['message']['peer_id'])]}, \nПоследнее обновление расписания: {None}", 'random_id':0})

            if event.obj['message']['text'].lower() in ["!команды"]:
                vk_session.method('messages.send',{'peer_id':event.obj['message']['peer_id'], 'message': "\n".join(["!инфо","!команды","!расписание","!номер группы"]), 'random_id':0})

            if event.obj['message']['text'].lower() in ["!расписание"]:
                print(str(event.obj['message']['peer_id']))
                if str(event.obj['message']['peer_id']) in list(data.keys()):
                    #Серега, срать сюда
                    message="СЕРЁГА, ТВОЙ ВЫХОД"
                    vk_session.method('messages.send',{'peer_id':event.obj['message']['peer_id'], 'message': message, 'random_id':0})
                else:
                    vk_session.method('messages.send',{'peer_id':event.obj['message']['peer_id'], 'message': 'Укажите номер группы!', 'random_id':0})
            if event.obj['message']['text'].lower().startswith("!номер группы"):
                if event.obj['message']['text'].lower()[13:].replace(" ","") in group_list:
                    data[str(event.obj['message']['peer_id'])] = str(event.obj['message']['text'].lower()[13:].replace(" ",""))
                    write(data,'data.json')
                    vk_session.method('messages.send',{'peer_id':event.obj['message']['peer_id'], 'message':f"Расписание группы {event.obj['message']['text'].lower()[13:].replace(' ','')} закреплено за диалогом" , 'random_id':0})
                else:
                    vk_session.method('messages.send',{'peer_id':event.obj['message']['peer_id'], 'message':f"Группы {event.obj['message']['text'].lower()[13:].replace(' ','')} не существует" , 'random_id':0})








if __name__ == '__main__':
    main()