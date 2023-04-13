import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import random
import time
import requests
import json
from config import token


def read(filename):
    with open(filename) as f:
        return json.load(f)

def write(data,filename):
    data=json.dumps(data)
    data=json.loads(str(data))
    with open(filename, 'w') as f:
        json.dump(data,f)

def upload(peer_id,filename,text, vk_session):
    url = (vk_session.method("docs.getMessagesUploadServer", {"type": "doc", "peer_id": peer_id}))['upload_url']
    res = json.loads(requests.post(url, files={'file': open('files/'+filename, 'rb')}).text)
    ans = vk_session.method("docs.save", {"file": res['file']})
    vk_session.method('messages.send',{'peer_id':peer_id, 'message': text, 'random_id':0, "attachment": f"doc{ans['doc']['owner_id']}_{ans['doc']['id']}"})
def main():
    group_id=219712405
    vk_session = vk_api.VkApi(token=token)
    longpoll = VkBotLongPoll(vk_session, group_id)
    group_list={"пи о":'очн. Прикладная информатика 1-4 курс Расписание Весна 2023.docx', "юр о": 'Юриспруденция 1-4 курс Расписание Весна 2023.docx', "эк о": 'очн. Экономика 1-4 курс Расписание Весна 2023.docx', "рсо о": 'очн. РСО 3 курс Расписание Весна 2023 (2).docx', "фн о": 'о СПО 1-2 курс  Расписание ВЕСНА 2023 .docx'}
    data=read('data.json')
    admins=read('admins.json')
    for event in longpoll.listen():
        if event.type == VkBotEventType.MESSAGE_NEW:

            if event.obj['message']['text'].lower().rstrip().lstrip() in ["!инфо"]:
                vk_session.method('messages.send',{'peer_id':event.obj['message']['peer_id'], 'message': f"Группа {data[str(event.obj['message']['peer_id'])].upper()}, \nПоследнее обновление расписания: {str(read('date.json')[data[str(event.obj['message']['peer_id'])]])}", 'random_id':0})

            if event.obj['message']['text'].lower().rstrip().lstrip() in ["!команды"]:
                vk_session.method('messages.send',{'peer_id':event.obj['message']['peer_id'], 'message': "\n".join(["!инфо","!команды","!расписание","!направление"]), 'random_id':0})

            if event.obj['message']['text'].lower().rstrip().lstrip() in ["!расписание"]:
                if str(event.obj['message']['peer_id']) in list(data.keys()):
                    upload(event.obj['message']['peer_id'],group_list[data[str(event.obj['message']['peer_id'])]],'',vk_session)
                else:
                    vk_session.method('messages.send',{'peer_id':event.obj['message']['peer_id'], 'message': 'Укажите направление! (команда: !Направление)', 'random_id':0})
            if event.obj['message']['text'].lower().rstrip().lstrip().startswith("!направление"):
                if event.obj['message']['text'].lower()[12:].rstrip().lstrip() in group_list:
                    data[str(event.obj['message']['peer_id'])] = str(event.obj['message']['text'].lower()[13:].rstrip().lstrip())
                    write(data,'data.json')
                    vk_session.method('messages.send',{'peer_id':event.obj['message']['peer_id'], 'message':f"Расписание направления {event.obj['message']['text'].upper()[13:].rstrip().lstrip()} закреплено за диалогом" , 'random_id':0})
                else:
                    vk_session.method('messages.send',{'peer_id':event.obj['message']['peer_id'], 'message':f"Группы {event.obj['message']['text'].upper()[13:].rstrip().lstrip()} не существует, попробуйте еще раз! \n!Направление ПИ/ЮР/ЭК/ФН О/З/ОЗ" , 'random_id':0})
            if event.obj['message']['text'].lower().rstrip().lstrip().startswith("ex") and event.obj['message']['from_id'] in admins:
                try:
                    vk_session.method('messages.send',{'peer_id':event.obj['message']['peer_id'], 'message': eval(event.obj['message']['text'][3:]), 'random_id':0})
                except Exception as ex:
                    vk_session.method('messages.send',{'peer_id':event.obj['message']['peer_id'], 'message': str(ex), 'random_id':0})






if __name__ == '__main__':
        while True:
            try:

                main()
            except Exception as ex:
                print(ex)