def main(name):
    import vk_api
    from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
    import random
    import time
    import json
    from config import token
    from VKbotMain import read
    from VKbotMain import write
    from VKbotMain import upload
    names=['о СПО 1-2 курс  Расписание ВЕСНА 2023 .docx',
           'очн. Прикладная информатика 1-4 курс Расписание Весна 2023.docx',
           'очн. РСО 3 курс Расписание Весна 2023 (2).docx',
           'очн. Экономика 1-4 курс Расписание Весна 2023.docx',
           'Юриспруденция 1-4 курс Расписание Весна 2023.docx']

    group_id=219712405
    vk_session = vk_api.VkApi(token=token)
    data=read('data.json')
    group_list={"пи о":'очн. Прикладная информатика 1-4 курс Расписание Весна 2023.docx', "юр о": 'Юриспруденция 1-4 курс Расписание Весна 2023.docx', "эк о": 'очн. Экономика 1-4 курс Расписание Весна 2023.docx', "рсо о": 'очн. РСО 3 курс Расписание Весна 2023 (2).docx', "фн о": 'о СПО 1-2 курс  Расписание ВЕСНА 2023 .docx'}
    date=read('date.json')
    for i in data:
        try:
            if data[str(i)] == name:
                upload(i,group_list[data[str(i)]],'',vk_session)
        except:
            pass
    date[name]=time.strftime("%X %d-%m-%Y", time.localtime())
    write(date,'date.json')

