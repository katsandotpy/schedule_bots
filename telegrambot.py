import config
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton
import mysql.connector
from mysql.connector import Error


TOKEN = config.TOKEN
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

#соединение с бд
def create_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")
    return connection

connection = create_connection("localhost", "root", "Ddrkl#4321", 'schedule_bot')

###КУРСОР
def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)  ###МЕТОД ДЛЯ ВЫПОЛНЕНИЯ ЗАПРОСОВ
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")

###ЧТЕНИЕ ИЗ БД
def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")


#ПОИСК В ТАБЛИЦЕ ЮЗЕРОВ
def finduser(id):
    select_users = f"SELECT * FROM `userdata`"
    users = execute_read_query(connection, select_users)

    for user in users:
        print(user)
        if str(user[0])==id:
            return True
    return False

#ПОИСК В ФУЛ ТАБЛИЦЕ
def findfull(napr, form, tab):
    select_users = f"SELECT * FROM {tab}"
    users = execute_read_query(connection, select_users)

    for user in users:
        print(user)
        if user[0]==napr and user[1]==form:
            return True
    return False

###СОЗДАНИЕ ЗАПИСИ
def create(id, napr, forma):

    if id!='' and napr!='' and forma !='':
        create_users = f"""
        INSERT INTO
          `userdata` (`telegramid`, `napr`, `forma`)
        VALUES
          ('{id}', '{napr}', '{forma}');
        """
    try:
        execute_query(connection, create_users)
    except: pass

###УДАЛЕНИЕ ЗАПИСИ
def delete(id):
    if id!='':
        delete_users = f"""
        DELETE FROM 
          `userdata` WHERE '{id}'=`telegramid`;
        """
    try:
        execute_query(connection, delete_users)
    except: pass

def infouser(id):
    select_users = f"SELECT * FROM `userdata`"
    users = execute_read_query(connection, select_users)

    for user in users:
        print(user)
        mass = [str(user[1]), str(user[2])]
        return mass
    return False

def distribution(id):
    mass = infouser(id)
    if mass[0]=='pi' and mass[1]=='ochn':
        doc = open('files/' + 'очн. Прикладная информатика 1-4 курс Расписание Весна 2023.docx', 'rb')
        return doc
    elif mass[0]=='ur' and mass[1]=='ochn':
        doc = open('files/' +'Юриспруденция 1-4 курс Расписание Весна 2023.docx', 'rb')
        return doc
    elif mass[0]=='ek' and mass[1]=='ochn':
        doc = open('files/' + 'очн. Экономика 1-4 курс Расписание Весна 2023.docx', 'rb')
        return doc
    elif mass[0]=='rso' and mass[1]=='ochn':
        doc = open('files/' + 'очн. РСО 3 курс Расписание Весна 2023 (2).docx', 'rb')
        return doc
    elif mass[0]=='fin' and mass[1]=='ochn':
        doc = open('files/' + 'о СПО 1-2 курс  Расписание ВЕСНА 2023 .docx', 'rb')
        return doc
    elif mass[0]=='ped' and mass[1]=='zaochn':
        doc = open('files/статья.docx', 'rb')
        return doc
    elif mass[0]=='rso' and mass[1]=='zaochn':
        doc = open('files/статья.docx', 'rb')
        return doc
    elif mass[0]=='gmu' and mass[1]=='zaochn':
        doc = open('files/статья.docx', 'rb')
        return doc
    elif mass[0]=='mj' and mass[1]=='zaochn':
        doc = open('files/статья.docx', 'rb')
        return doc
    elif mass[0]=='ek' and mass[1]=='zaochn':
        doc = open('files/статья.docx', 'rb')
        return doc
    elif mass[0]=='ur' and mass[1]=='ochzaochn':
        doc = open('files/статья.docx', 'rb')
        return doc
    elif mass[0]=='gmu' and mass[1]=='ochzaochn':
        doc = open('files/статья.docx', 'rb')
        return doc
    elif mass[0]=='ek' and mass[1]=='ochzaochn':
        doc = open('files/статья.docx', 'rb')
        return doc
    elif mass[0]=='pi' and mass[1]=='ochzaochn':
        doc = open('files/статья.docx', 'rb')
        return doc

def change(forma, napravlenie):
    if forma == 'Очная':
        form = 'ochn'
    elif forma == 'Заочная':
        form = 'zaochn'
    elif forma == 'Очно-заочная':
        form = 'ochzaochn'
    if napravlenie == 'ПИ':
        napr = 'pi'
    elif napravlenie == 'ЮР':
        napr = 'ur'
    elif napravlenie == 'ЭК':
        napr = 'ek'
    elif napravlenie == 'РС':
        napr = 'rso'
    elif napravlenie == 'ФН':
        napr = 'fin'
    elif napravlenie == 'ГМ':
        napr = 'gmu'
    elif napravlenie == 'ПО':
        napr = 'ped'
    elif napravlenie == 'МЖ':
        napr = 'mj'
    return form, napr



# команда start
@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    tgid = str(message.from_user.id)
    findid = finduser(tgid)
    kb = [
        [
            types.KeyboardButton(text="Да."),
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
    )
    await message.answer(
        "Привет! Я занимаюсь рассылкой расписания, для начала необходимо пройти авторизацию. Продолжить?",
        reply_markup=keyboard)
    #если в базе данных не найдено айди
    if findid==False:

        @dp.message_handler(text=["Да."])
        async def yes(message: types.Message):
            kb = [
                [
                    types.KeyboardButton(text="Очная"),
                    types.KeyboardButton(text="Очно-заочная"),
                    types.KeyboardButton(text="Заочная"),
                ],
            ]
            keyboard = types.ReplyKeyboardMarkup(
                keyboard=kb,
                resize_keyboard=True,
            )
            await message.reply("Отлично. Выберите вашу форму обучения.", reply_markup=keyboard)


            @dp.message_handler(text=['Очная', 'Заочная', 'Очно-заочная'])
            async def formmm(message: types.Message):
                kb = [
                    [
                        types.KeyboardButton(text="ПИ"),
                        types.KeyboardButton(text="ЮР"),
                        types.KeyboardButton(text="ЭК"),
                        types.KeyboardButton(text="РС"),
                        types.KeyboardButton(text="ФН"),
                        types.KeyboardButton(text="ГМ"),
                        types.KeyboardButton(text="ПО"),
                        types.KeyboardButton(text="МЖ"),
                    ],
                ]
                keyboard = types.ReplyKeyboardMarkup(
                    keyboard=kb,
                    resize_keyboard=True,
                )
                forma = message.text
                print(forma)

                await message.reply("Теперь выберите ваше направление подготовки.", reply_markup=keyboard)

                @dp.message_handler(text=['ПИ', 'ЮР', 'ЭК', 'РС', 'ФН', 'ГМ', 'ПО', 'МЖ'])
                async def jjj(message: types.Message):

                    napravlenie = message.text
                    print(napravlenie)

                    mass = [change(forma, napravlenie)]
                    print(mass)
                    form = mass[0][0]
                    napr = mass[0][1]
                    findd = findfull(napr, form, 'userdatafull')

                    create(tgid, napr, form)
                    kb = [
                        [
                            types.KeyboardButton(text="Продолжить"),
                        ],
                    ]
                    keyboard = types.ReplyKeyboardMarkup(
                        keyboard=kb,
                        resize_keyboard=True,
                    )
                    await message.answer(
                        "Вы авторизованы. Вы можете запросить расписание, обновленное расписание будут приходить автоматически.",
                        reply_markup=keyboard)


                    @dp.message_handler(text=["Продолжить"])
                    async def prod(message: types.Message):
                        kb = [
                            [
                                types.KeyboardButton(text="Запросить расписание"),
                                types.KeyboardButton(text="Информация")
                            ],
                        ]
                        keyboard = types.ReplyKeyboardMarkup(
                            keyboard=kb,
                            resize_keyboard=True,
                        )
                        await message.answer("Выберите действие.", reply_markup=keyboard)

                        # файл с расписанием
                        @dp.message_handler(text=["Запросить расписание"])
                        async def schuedle(message: types.Message):
                            doc = distribution(tgid)
                            await bot.send_document(chat_id=message.chat.id, document=doc)

                        #информация
                        @dp.message_handler(text=["Информация"])
                        async def information(message: types.Message):
                            await message.reply(
                                "Это бот для студентов ННГУ ДФ. Вам будет автоматически приходить актуальное расписание, в случае необходимости вы можете запросить повторную отправку. Если вы ошиблись группой, вы можете очистить данные с помощью команды /deletedata и заново пройти авторизацию.")

    #если в базе данных есть айди
    elif findid==True:
        @dp.message_handler(text=["Да."])
        async def yes1(message: types.Message):
            kb = [
                [
                    types.KeyboardButton(text="Запросить расписание"),
                    types.KeyboardButton(text="Информация")
                ],
            ]
            keyboard = types.ReplyKeyboardMarkup(
                keyboard=kb,
                resize_keyboard=True,
            )
            await message.answer("Вы авторизованы. Выберите действие", reply_markup=keyboard)

            # файл с расписанием
            @dp.message_handler(text=["Запросить расписание"])
            async def schuedle(message: types.Message):
                doc = distribution(tgid)
                await bot.send_document(chat_id=message.chat.id, document=doc)

            # информация
            @dp.message_handler(text=["Информация"])
            async def information(message: types.Message):
                await message.reply(
                    "Это бот для студентов ННГУ ДФ. Вам будет автоматически приходить актуальное расписание, в случае необходимости вы можете запросить повторную отправку. Если вы ошиблись группой, вы можете очистить данные с помощью команды /deletedata и заново пройти авторизацию.")


#удаление записи в бд
@dp.message_handler(commands=['deletedata'])
async def cmd_start(message: types.Message):
    tgid = str(message.from_user.id)
    if finduser(tgid) == True:
        delete(tgid)
        await message.reply(
            "Данные удалены. Вы можете заново пройти авторизацию, использовав команду '/start'.")
    else: await message.reply(
            "Ваших данных нет в базе. Вы можете пройти авторизацию, использовав команду '/start'.")





#исполнение
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

