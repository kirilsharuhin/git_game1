import logging
from telegram.ext import Application, MessageHandler, filters, CommandHandler
from telegram import ReplyKeyboardMarkup

TOKEN = '6109988943:AAFdpBUb15CycWkzzWLZMwSdqTT2F9afiJI'
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)
o = []
oo = []
logger = logging.getLogger(__name__)

reply_keyboard1 = [['/aa', '/bb', '/cc', '/dd']]
markup1 = ReplyKeyboardMarkup(reply_keyboard1, one_time_keyboard=False)
reply_keyboard2 = [['/a', '/b', '/c', '/d']]
markup2 = ReplyKeyboardMarkup(reply_keyboard2, one_time_keyboard=False)
reply_keyboard3 = [['/help', '/authors', '/normal_game', '/hard_game']]
markup3 = ReplyKeyboardMarkup(reply_keyboard3, one_time_keyboard=False)
reply_keyboard4 = [['/authors', '/normal_game', '/hard_game']]
markup4 = ReplyKeyboardMarkup(reply_keyboard4, one_time_keyboard=False)
reply_keyboard5 = [['/help', '/normal_game', '/hard_game']]
markup5 = ReplyKeyboardMarkup(reply_keyboard5, one_time_keyboard=False)


async def start(update, context):
    await update.message.reply_text('Здравствуй, я ГеоБот! \n'
                                    'Я создан для того, чтобы Ты мог \n'
                                    'проверить свой уровень знания географии мира\n'
                                    'Вот основные команды бота:\n'
                                    '/normal_game - лёгкий тест\n'
                                    '/hard_game - очень трудный тест\n'
                                    '/help - помощь в управлении ботом\n'
                                    '/records - лучщие результаты в тестах\n'
                                    '/authors - информация об авторе')


async def help(update, context):
    await update.message.reply_text("Бот довольно прост в использовании. Об его основных командах\n"
                                    "можно узнать, нажав на /start")
    await update.message.reply_text("Можете начать любой тест: ", reply_markup=markup4)


async def author(update, context):
    await update.message.reply_text("Проект создан Ш. Кириллом")
    await update.message.reply_text("Можете начать любой тест: ", reply_markup=markup4)


async def records(update, context):
    await update.message.reply_text('молодец 10 из 10')


async def normal_game(update, context):
    await update.message.reply_text("Давайте начнём тест нормального уровня сложности.\n"
                                    "Как называется столица России?\n",
                                    "A) Москва\n",
                                    "Б) Вологда\n",
                                    "В) Питер\n",
                                    "Г) Резань\n",
                                    reply_markup=markup2)


async def a(update, context):
    o.append("a")
    if len(o) == 1:
        await update.message.reply_text("Сколько людей живет в Китае?\n",
                                        "A) 1,379 миллиарда\n",
                                        "Б) 5 миллиардов\n",
                                        "В) 9\n",
                                        "Г) Москва\n", reply_markup=markup2)
    if len(o) == 2:
        await update.message.reply_text("Какой самый большой остров?\n",
                                        "A) Гренландия\n",
                                        "Б) Мадагаскар\n",
                                        "В) Россия\n",
                                        "Г) 10\n", reply_markup=markup2)
    if len(o) == 3:
        await update.message.reply_text("В каком городе находится самая большая башня в мира?\n",
                                        "A) В Дубае\n",
                                        "Б) В Мадагаскаре\n",
                                        "В) В России\n",
                                        "Г) Африка\n", reply_markup=markup2)
    if len(o) == 4:
        await update.message.reply_text("Какую площадь занимает океан на Земле?"
                                        "A) 361 100 000 км 2\n",
                                        "Б) В Мадагаскаре\n",
                                        "В) 100000 км 5\n",
                                        "Г) 10000000 тыс км 2\n", reply_markup=markup2)
    if len(o) == 5:
        await update.message.reply_text(
            "Какой самый маленькая страна на Земле?"
            "A) Вологда\n",
            "Б) Ватикан\n",
            "В) Я не знаю\n",
            "Г) Китай\n", reply_markup=markup2)
    if len(o) == 6:
        await update.message.reply_text("Какая самая большая страна на Земле?"
                                        "A) Россия\n",
                                        "Б) США\n",
                                        "В) Ватикан\n",
                                        "Г) 69\n", reply_markup=markup2)
    if len(o) == 7:
        await update.message.reply_text("Сколько морей на Земле?"
                                        "A) 90\n",
                                        "Б) много\n",
                                        "В) 13\n",
                                        "Г) мало\n", reply_markup=markup2)
    if len(o) == 8:
        await update.message.reply_text(
            "Какое море на Земле самое большое?"
            "A) Саргассово\n",
            "Б) Эгейское\n",
            "В) Вологодское\n",
            "Г) не знаю\n", reply_markup=markup2)
    if len(o) == 9:
        await update.message.reply_text(
            "Когда зародилась планета Земля"
            "A) ооочень давно\n",
            "Б) давно\n",
            "В) 4 и 5 млн лет назад\n",
            "Г) 4 и 5 миллиардов лет назад\n", reply_markup=markup2)
    if len(o) == 10:
        oa = 0
        ob = 0
        oc = 0
        od = 0
        for i in o:
            if i == "a":
                oa += 1
            if i == "b":
                ob += 1
            if i == "c":
                oc += 1
            if i == "d":
                od += 1
        if oa == max(oa, ob, oc, od):
            await update.message.reply_text("Вы гений!!!")
            await update.message.reply_text("Вы смогли пройти этот тест на огромное количество баллов!!!")
            await update.message.reply_text("Можете выбрать что нибудь из этого:",
                                            reply_markup=markup3)
            await update.message.reply_text("Но честно говоря, я даже не ожидал, что")
            await update.message.reply_text("этот тэст пройдут!!!")
        elif ob == max(oa, ob, oc, od):
            await update.message.reply_text("Отличная попытка!!!")
            await update.message.reply_text("У Вас отлично развита логика, но на \n"
                                            "уроках географии Вас явно не было видно!!!")
            await update.message.reply_text("Попробуйте пройти этот тест снова)))",
                                            reply_markup=markup3)
            await update.message.reply_text("Удачи!!!")
            await update.message.reply_text("В следующий раз у Вас всё получится!!!")
        elif oc == max(oa, ob, oc, od):
            await update.message.reply_text("Неплохая попытка, но знаний по географии у Вас очень мало!!!")
            await update.message.reply_text("В следующий раз постарайтесь получше!!!")
            await update.message.reply_text("Пройдите тест ещо раз:",
                                            reply_markup=markup3)
            await update.message.reply_text("До свидания")
            await update.message.reply_text("Надеюсь что до скорого!!!")
        elif od == max(oa, ob, oc, od):
            await update.message.reply_text("Нормальная попытка!!!")
            await update.message.reply_text("Чувства юмора у Вас не занимать, но вот знания \n"
                                            "географии мира у Вас, походу, кто то точно занял!!!")
            await update.message.reply_text("Попытайтесь пройти тест ещё разик!!!",
                                            reply_markup=markup3)
            await update.message.reply_text("Удачи!!!")
            await update.message.reply_text("Не сдавайтесь!!!")
    o.clear()


async def b(update, context):
    o.append("b")
    if len(o) == 1:
        await update.message.reply_text("Сколько людей живет в Китае?\n",
                                        "A) 1,379 миллиарда\n",
                                        "Б) 5 миллиардов\n",
                                        "В) 9\n",
                                        "Г) Москва\n", reply_markup=markup2)
    if len(o) == 2:
        await update.message.reply_text("Какой самый большой остров?\n",
                                        "A) Гренландия\n",
                                        "Б) Мадагаскар\n",
                                        "В) Россия\n",
                                        "Г) 10\n", reply_markup=markup2)
    if len(o) == 3:
        await update.message.reply_text("В каком городе находится самая большая башня в мира?\n",
                                        "A) В Дубае\n",
                                        "Б) В Мадагаскаре\n",
                                        "В) В России\n",
                                        "Г) Африка\n", reply_markup=markup2)
    if len(o) == 4:
        await update.message.reply_text("Какую площадь занимает океан на Земле?"
                                        "A) 361 100 000 км 2\n",
                                        "Б) В Мадагаскаре\n",
                                        "В) 100000 км 5\n",
                                        "Г) 10000000 тыс км 2\n", reply_markup=markup2)
    if len(o) == 5:
        await update.message.reply_text(
            "Какой самый маленькая страна на Земле?"
            "A) Вологда\n",
            "Б) Ватикан\n",
            "В) Я не знаю\n",
            "Г) Китай\n", reply_markup=markup2)
    if len(o) == 6:
        await update.message.reply_text("Какая самая большая страна на Земле?"
                                        "A) Россия\n",
                                        "Б) США\n",
                                        "В) Ватикан\n",
                                        "Г) 69\n", reply_markup=markup2)
    if len(o) == 7:
        await update.message.reply_text("Сколько морей на Земле?"
                                        "A) 90\n",
                                        "Б) много\n",
                                        "В) 13\n",
                                        "Г) мало\n", reply_markup=markup2)
    if len(o) == 8:
        await update.message.reply_text(
            "Какое море на Земле самое большое?"
            "A) Саргассово\n",
            "Б) Эгейское\n",
            "В) Вологодское\n",
            "Г) не знаю\n", reply_markup=markup2)
    if len(o) == 9:
        await update.message.reply_text(
            "Когда зародилась планета Земля"
            "A) ооочень давно\n",
            "Б) давно\n",
            "В) 4 и 5 млн лет назад\n",
            "Г) 4 и 5 миллиардов лет назад\n", reply_markup=markup2)
    if len(o) == 10:
        oa = 0
        ob = 0
        oc = 0
        od = 0
        for i in o:
            if i == "a":
                oa += 1
            if i == "b":
                ob += 1
            if i == "c":
                oc += 1
            if i == "d":
                od += 1
        if oa == max(oa, ob, oc, od):
            await update.message.reply_text("Вы гений!!!")
            await update.message.reply_text("Вы смогли пройти этот тест на огромное количество баллов!!!")
            await update.message.reply_text("Можете выбрать что нибудь из этого:",
                                            reply_markup=markup3)
            await update.message.reply_text("Но честно говоря, я даже не ожидал, что")
            await update.message.reply_text("этот тэст пройдут!!!")
        elif ob == max(oa, ob, oc, od):
            await update.message.reply_text("Отличная попытка!!!")
            await update.message.reply_text("У Вас отлично развита логика, но на \n"
                                            "уроках географии Вас явно не было видно!!!")
            await update.message.reply_text("Попробуйте пройти этот тест снова)))",
                                            reply_markup=markup3)
            await update.message.reply_text("Удачи!!!")
            await update.message.reply_text("В следующий раз у Вас всё получится!!!")
        elif oc == max(oa, ob, oc, od):
            await update.message.reply_text("Неплохая попытка, но знаний по географии у Вас очень мало!!!")
            await update.message.reply_text("В следующий раз постарайтесь получше!!!")
            await update.message.reply_text("Пройдите тест ещо раз:",
                                            reply_markup=markup3)
            await update.message.reply_text("До свидания")
            await update.message.reply_text("Надеюсь что до скорого!!!")
        elif od == max(oa, ob, oc, od):
            await update.message.reply_text("Нормальная попытка!!!")
            await update.message.reply_text("Чувства юмора у Вас не занимать, но вот знания \n"
                                            "географии мира у Вас, походу, кто то точно занял!!!")
            await update.message.reply_text("Попытайтесь пройти тест ещё разик!!!",
                                            reply_markup=markup3)
            await update.message.reply_text("Удачи!!!")
            await update.message.reply_text("Не сдавайтесь!!!")
    o.clear()


async def c(update, context):
    o.append("c")
    if len(o) == 1:
        await update.message.reply_text("Сколько людей живет в Китае?\n",
                                        "A) 1,379 миллиарда\n",
                                        "Б) 5 миллиардов\n",
                                        "В) 9\n",
                                        "Г) Москва\n", reply_markup=markup2)
    if len(o) == 2:
        await update.message.reply_text("Какой самый большой остров?\n",
                                        "A) Гренландия\n",
                                        "Б) Мадагаскар\n",
                                        "В) Россия\n",
                                        "Г) 10\n", reply_markup=markup2)
    if len(o) == 3:
        await update.message.reply_text("В каком городе находится самая большая башня в мира?\n",
                                        "A) В Дубае\n",
                                        "Б) В Мадагаскаре\n",
                                        "В) В России\n",
                                        "Г) Африка\n", reply_markup=markup2)
    if len(o) == 4:
        await update.message.reply_text("Какую площадь занимает океан на Земле?"
                                        "A) 361 100 000 км 2\n",
                                        "Б) В Мадагаскаре\n",
                                        "В) 100000 км 5\n",
                                        "Г) 10000000 тыс км 2\n", reply_markup=markup2)
    if len(o) == 5:
        await update.message.reply_text(
            "Какой самый маленькая страна на Земле?"
            "A) Вологда\n",
            "Б) Ватикан\n",
            "В) Я не знаю\n",
            "Г) Китай\n", reply_markup=markup2)
    if len(o) == 6:
        await update.message.reply_text("Какая самая большая страна на Земле?"
                                        "A) Россия\n",
                                        "Б) США\n",
                                        "В) Ватикан\n",
                                        "Г) 69\n", reply_markup=markup2)
    if len(o) == 7:
        await update.message.reply_text("Сколько морей на Земле?"
                                        "A) 90\n",
                                        "Б) много\n",
                                        "В) 13\n",
                                        "Г) мало\n", reply_markup=markup2)
    if len(o) == 8:
        await update.message.reply_text(
            "Какое море на Земле самое большое?"
            "A) Саргассово\n",
            "Б) Эгейское\n",
            "В) Вологодское\n",
            "Г) не знаю\n", reply_markup=markup2)
    if len(o) == 9:
        await update.message.reply_text(
            "Когда зародилась планета Земля"
            "A) ооочень давно\n",
            "Б) давно\n",
            "В) 4 и 5 млн лет назад\n",
            "Г) 4 и 5 миллиардов лет назад\n", reply_markup=markup2)
    if len(o) == 10:
        oa = 0
        ob = 0
        oc = 0
        od = 0
        for i in o:
            if i == "a":
                oa += 1
            if i == "b":
                ob += 1
            if i == "c":
                oc += 1
            if i == "d":
                od += 1
        if oa == max(oa, ob, oc, od):
            await update.message.reply_text("Вы гений!!!")
            await update.message.reply_text("Вы смогли пройти этот тест на огромное количество баллов!!!")
            await update.message.reply_text("Можете выбрать что нибудь из этого:",
                                            reply_markup=markup3)
            await update.message.reply_text("Но честно говоря, я даже не ожидал, что")
            await update.message.reply_text("этот тэст пройдут!!!")
        elif ob == max(oa, ob, oc, od):
            await update.message.reply_text("Отличная попытка!!!")
            await update.message.reply_text("У Вас отлично развита логика, но на \n"
                                            "уроках географии Вас явно не было видно!!!")
            await update.message.reply_text("Попробуйте пройти этот тест снова)))",
                                            reply_markup=markup3)
            await update.message.reply_text("Удачи!!!")
            await update.message.reply_text("В следующий раз у Вас всё получится!!!")
        elif oc == max(oa, ob, oc, od):
            await update.message.reply_text("Неплохая попытка, но знаний по географии у Вас очень мало!!!")
            await update.message.reply_text("В следующий раз постарайтесь получше!!!")
            await update.message.reply_text("Пройдите тест ещо раз:",
                                            reply_markup=markup3)
            await update.message.reply_text("До свидания")
            await update.message.reply_text("Надеюсь что до скорого!!!")
        elif od == max(oa, ob, oc, od):
            await update.message.reply_text("Нормальная попытка!!!")
            await update.message.reply_text("Чувства юмора у Вас не занимать, но вот знания \n"
                                            "географии мира у Вас, походу, кто то точно занял!!!")
            await update.message.reply_text("Попытайтесь пройти тест ещё разик!!!",
                                            reply_markup=markup3)
            await update.message.reply_text("Удачи!!!")
            await update.message.reply_text("Не сдавайтесь!!!")
    o.clear()


async def d(update, context):
    o.append("d")
    if len(o) == 1:
        await update.message.reply_text("Сколько людей живет в Китае?\n",
                                        "A) 1,379 миллиарда\n",
                                        "Б) 5 миллиардов\n",
                                        "В) 9\n",
                                        "Г) Москва\n", reply_markup=markup2)
    if len(o) == 2:
        await update.message.reply_text("Какой самый большой остров?\n",
                                        "A) Гренландия\n",
                                        "Б) Мадагаскар\n",
                                        "В) Россия\n",
                                        "Г) 10\n", reply_markup=markup2)
    if len(o) == 3:
        await update.message.reply_text("В каком городе находится самая большая башня в мира?\n",
                                        "A) В Дубае\n",
                                        "Б) В Мадагаскаре\n",
                                        "В) В России\n",
                                        "Г) Африка\n", reply_markup=markup2)
    if len(o) == 4:
        await update.message.reply_text("Какую площадь занимает океан на Земле?"
                                        "A) 361 100 000 км 2\n",
                                        "Б) В Мадагаскаре\n",
                                        "В) 100000 км 5\n",
                                        "Г) 10000000 тыс км 2\n", reply_markup=markup2)
    if len(o) == 5:
        await update.message.reply_text(
            "Какой самый маленькая страна на Земле?"
            "A) Вологда\n",
            "Б) Ватикан\n",
            "В) Я не знаю\n",
            "Г) Китай\n", reply_markup=markup2)
    if len(o) == 6:
        await update.message.reply_text("Какая самая большая страна на Земле?"
                                        "A) Россия\n",
                                        "Б) США\n",
                                        "В) Ватикан\n",
                                        "Г) 69\n", reply_markup=markup2)
    if len(o) == 7:
        await update.message.reply_text("Сколько морей на Земле?"
                                        "A) 90\n",
                                        "Б) много\n",
                                        "В) 13\n",
                                        "Г) мало\n", reply_markup=markup2)
    if len(o) == 8:
        await update.message.reply_text(
            "Какое море на Земле самое большое?"
            "A) Саргассово\n",
            "Б) Эгейское\n",
            "В) Вологодское\n",
            "Г) не знаю\n", reply_markup=markup2)
    if len(o) == 9:
        await update.message.reply_text(
            "Когда зародилась планета Земля"
            "A) ооочень давно\n",
            "Б) давно\n",
            "В) 4 и 5 млн лет назад\n",
            "Г) 4 и 5 миллиардов лет назад\n", reply_markup=markup2)
    if len(o) == 10:
        oa = 0
        ob = 0
        oc = 0
        od = 0
        for i in o:
            if i == "a":
                oa += 1
            if i == "b":
                ob += 1
            if i == "c":
                oc += 1
            if i == "d":
                od += 1
        if oa == max(oa, ob, oc, od):
            await update.message.reply_text("Вы гений!!!")
            await update.message.reply_text("Вы смогли пройти этот тест на огромное количество баллов!!!")
            await update.message.reply_text("Можете выбрать что нибудь из этого:",
                                            reply_markup=markup3)
            await update.message.reply_text("Но честно говоря, я даже не ожидал, что")
            await update.message.reply_text("этот тэст пройдут!!!")
        elif ob == max(oa, ob, oc, od):
            await update.message.reply_text("Отличная попытка!!!")
            await update.message.reply_text("У Вас отлично развита логика, но на \n"
                                            "уроках географии Вас явно не было видно!!!")
            await update.message.reply_text("Попробуйте пройти этот тест снова)))",
                                            reply_markup=markup3)
            await update.message.reply_text("Удачи!!!")
            await update.message.reply_text("В следующий раз у Вас всё получится!!!")
        elif oc == max(oa, ob, oc, od):
            await update.message.reply_text("Неплохая попытка, но знаний по географии у Вас очень мало!!!")
            await update.message.reply_text("В следующий раз постарайтесь получше!!!")
            await update.message.reply_text("Пройдите тест ещо раз:",
                                            reply_markup=markup3)
            await update.message.reply_text("До свидания")
            await update.message.reply_text("Надеюсь что до скорого!!!")
        elif od == max(oa, ob, oc, od):
            await update.message.reply_text("Нормальная попытка!!!")
            await update.message.reply_text("Чувства юмора у Вас не занимать, но вот знания \n"
                                            "географии мира у Вас, походу, кто то точно занял!!!")
            await update.message.reply_text("Попытайтесь пройти тест ещё разик!!!",
                                            reply_markup=markup3)
            await update.message.reply_text("Удачи!!!")
            await update.message.reply_text("Не сдавайтесь!!!")
    o.clear()


async def hard_game(update, contex):
    await update.message.reply_text('Давайте начнём очень трудный тест?')
    await update.message.reply_text("Как называется самая высокая гора в Канаде?\n"
                                    "А) Логан \n"
                                    "Б) Эверест\n"
                                    "В) Белуга\n"
                                    "Г) Россомаха\n", reply_markup=markup1)


async def aa(update, context):
    oo.append("aa")
    if len(oo) == 2:
        await update.message.reply_text("Какая самая большая столица в Северной Америке?\n"
                                        "А) Мехико \n"
                                        "Б) Мексика\n"
                                        "В) Нью-Йорк\n"
                                        "Г) Париж", reply_markup=markup1)
    if len(oo) == 4:
        await update.message.reply_text("Какая река самая короткая в мире?\n"
                                        "А) Репруа \n"
                                        "Б) Репируя\n"
                                        "В) Денизи\n"
                                        "Г) Вологда", reply_markup=markup1)
    if len(oo) == 6:
        await update.message.reply_text("Какой стране принадлежат Канарские острова?\n"
                                        "А) Испании \n"
                                        "Б) Франции\n"
                                        "В) Нидерландам\n"
                                        "Г) Вологде", reply_markup=markup1)
    if len(oo) == 8:
        await update.message.reply_text("Какие две страны граничат непосредственно к северу от Венгрии?\n"
                                        "А) Словакия и Словения \n"
                                        "Б) Словакия и Франции\n"
                                        "В) Нидерланды и Франция\n"
                                        "Г) Вологда и Франция", reply_markup=markup1)
    if len(oo) == 10:
        await update.message.reply_text(
            "Какую страну также называют Нидерландами?\n"
            "А) Голландия \n"
            "Б) Словакия\n"
            "В) Венгрия\n"
            "Г) Россия", reply_markup=markup1)
    if len(oo) == 12:
        await update.message.reply_text("Какую страну также называют Нидерландами?\n"
                                        "А) Восточное Антарктическое плато \n"
                                        "Б) Северное Антлантическое плато\n"
                                        "В) Венгерская равнина\n"
                                        "Г) Россия", reply_markup=markup1)
    if len(oo) == 14:
        await update.message.reply_text("Сколько крупных островов составляют Гавайи?\n"
                                        "А) 8 \n"
                                        "Б) 9\n"
                                        "В) 7\n"
                                        "Г) 69", reply_markup=markup1)
    if len(oo) == 16:
        await update.message.reply_text(
            "Какая самая длинная река в Великобритании?\n"
            "А) Северн\n"
            "Б) Реден\n"
            "В) Санир\n"
            "Г) Золотуха", reply_markup=markup1)
    if len(oo) == 18:
        await update.message.reply_text(
            "В какой стране вы бы нашли город Дрезден?\n"
            "А) Германия\n"
            "Б) Франция\n"
            "В) Айзербайджан\n"
            "Г) Россия", reply_markup=markup1)
    if len(oo) == 20:
        ooa = 0
        oob = 0
        ooc = 0
        ood = 0
        for i in oo:
            if i == "aa":
                ooa += 1
            if i == "bb":
                oob += 1
            if i == "cc":
                ooc += 1
            if i == "dd":
                ood += 1
        if ooa == max(ooa, oob, ooc, ood):
            await update.message.reply_text("Урааааааа!!! Поздравляю!!!")
            await update.message.reply_text("Вы...набрали огромнейшее количество \n"
                                            "баллов за этот труднейший тест!!!")
            await update.message.reply_text("Можете пройти его ещё раз, если Вам так хочется!!!",
                                            reply_markup=markup3)
            await update.message.reply_text("Надеюсь на то, что Вы порекомендуете \n"
                                            "своим друзьям и знакомым этот великолепный \n"
                                            "телеграм-бот!!!")
            await update.message.reply_text("Хорошего дня!!!")
        elif oob == max(ooa, oob, ooc, ood):
            await update.message.reply_text("Неплохая попытка!!!")
            await update.message.reply_text("Вы набрали не так мало баллов, как в теории могли бы, \n"
                                            "но Вам ещё есть куда расти!!!")
            await update.message.reply_text("Надеюсь, Вам понравился бот, можете пройти тест ещё раз!!!",
                                            reply_markup=markup3)
            await update.message.reply_text("Попробуйте уличшить Ваши знания по географии!!!")
            await update.message.reply_text("Удачи Вам!!!")
        elif ooc == max(ooa, oob, ooc, ood):
            await update.message.reply_text("Неплохая попытка!!!")
            await update.message.reply_text("Вы набрали не так мало баллов, как в теории могли бы, \n"
                                            "но Вам ещё есть куда расти!!!")
            await update.message.reply_text("Надеюсь, Вам понравился бот, можете пройти тест ещё раз!!!",
                                            reply_markup=markup3)
            await update.message.reply_text("Попробуйте уличшить Ваши знания по географии!!!")
            await update.message.reply_text("Удачи Вам!!!")
        elif ood == max(ooa, oob, ooc, ood):
            await update.message.reply_text("Не самая плохая попытка, хотя, наверное самая...")
            await update.message.reply_text("Вы очень юморной человек, но вот знаний \n"
                                            "географии Вам не хватает!!!")
            await update.message.reply_text("Пройдите тест ещё раз, но теперь нормально!!!",
                                            reply_markup=markup3)
            await update.message.reply_text("Желаю Вам всего хорошего!!!")
            await update.message.reply_text("Надеюсь, Вам понравился бот!!!")
    oo.clear()


async def bb(update, context):
    oo.append("bb")
    if len(oo) == 2:
        await update.message.reply_text("Какая самая большая столица в Северной Америке?\n"
                                        "А) Мехико \n"
                                        "Б) Мексика\n"
                                        "В) Нью-Йорк\n"
                                        "Г) Париж", reply_markup=markup1)
    if len(oo) == 4:
        await update.message.reply_text("Какая река самая короткая в мире?\n"
                                        "А) Репруа \n"
                                        "Б) Репируя\n"
                                        "В) Денизи\n"
                                        "Г) Вологда", reply_markup=markup1)
    if len(oo) == 6:
        await update.message.reply_text("Какой стране принадлежат Канарские острова?\n"
                                        "А) Испании \n"
                                        "Б) Франции\n"
                                        "В) Нидерландам\n"
                                        "Г) Вологде", reply_markup=markup1)
    if len(oo) == 8:
        await update.message.reply_text("Какие две страны граничат непосредственно к северу от Венгрии?\n"
                                        "А) Словакия и Словения \n"
                                        "Б) Словакия и Франции\n"
                                        "В) Нидерланды и Франция\n"
                                        "Г) Вологда и Франция", reply_markup=markup1)
    if len(oo) == 10:
        await update.message.reply_text(
            "Какую страну также называют Нидерландами?\n"
            "А) Голландия \n"
            "Б) Словакия\n"
            "В) Венгрия\n"
            "Г) Россия", reply_markup=markup1)
    if len(oo) == 12:
        await update.message.reply_text("Какую страну также называют Нидерландами?\n"
                                        "А) Восточное Антарктическое плато \n"
                                        "Б) Северное Антлантическое плато\n"
                                        "В) Венгерская равнина\n"
                                        "Г) Россия", reply_markup=markup1)
    if len(oo) == 14:
        await update.message.reply_text("Сколько крупных островов составляют Гавайи?\n"
                                        "А) 8 \n"
                                        "Б) 9\n"
                                        "В) 7\n"
                                        "Г) 69", reply_markup=markup1)
    if len(oo) == 16:
        await update.message.reply_text(
            "Какая самая длинная река в Великобритании?\n"
            "А) Северн\n"
            "Б) Реден\n"
            "В) Санир\n"
            "Г) Золотуха", reply_markup=markup1)
    if len(oo) == 18:
        await update.message.reply_text(
            "В какой стране вы бы нашли город Дрезден?\n"
            "А) Германия\n"
            "Б) Франция\n"
            "В) Айзербайджан\n"
            "Г) Россия", reply_markup=markup1)
    if len(oo) == 20:
        ooa = 0
        oob = 0
        ooc = 0
        ood = 0
        for i in oo:
            if i == "aa":
                ooa += 1
            if i == "bb":
                oob += 1
            if i == "cc":
                ooc += 1
            if i == "dd":
                ood += 1
        if ooa == max(ooa, oob, ooc, ood):
            await update.message.reply_text("Урааааааа!!! Поздравляю!!!")
            await update.message.reply_text("Вы...набрали огромнейшее количество \n"
                                            "баллов за этот труднейший тест!!!")
            await update.message.reply_text("Можете пройти его ещё раз, если Вам так хочется!!!",
                                            reply_markup=markup3)
            await update.message.reply_text("Надеюсь на то, что Вы порекомендуете \n"
                                            "своим друзьям и знакомым этот великолепный \n"
                                            "телеграм-бот!!!")
            await update.message.reply_text("Хорошего дня!!!")
        elif oob == max(ooa, oob, ooc, ood):
            await update.message.reply_text("Неплохая попытка!!!")
            await update.message.reply_text("Вы набрали не так мало баллов, как в теории могли бы, \n"
                                            "но Вам ещё есть куда расти!!!")
            await update.message.reply_text("Надеюсь, Вам понравился бот, можете пройти тест ещё раз!!!",
                                            reply_markup=markup3)
            await update.message.reply_text("Попробуйте уличшить Ваши знания по географии!!!")
            await update.message.reply_text("Удачи Вам!!!")
        elif ooc == max(ooa, oob, ooc, ood):
            await update.message.reply_text("Неплохая попытка!!!")
            await update.message.reply_text("Вы набрали не так мало баллов, как в теории могли бы, \n"
                                            "но Вам ещё есть куда расти!!!")
            await update.message.reply_text("Надеюсь, Вам понравился бот, можете пройти тест ещё раз!!!",
                                            reply_markup=markup3)
            await update.message.reply_text("Попробуйте уличшить Ваши знания по географии!!!")
            await update.message.reply_text("Удачи Вам!!!")
        elif ood == max(ooa, oob, ooc, ood):
            await update.message.reply_text("Не самая плохая попытка, хотя, наверное самая...")
            await update.message.reply_text("Вы очень юморной человек, но вот знаний \n"
                                            "географии Вам не хватает!!!")
            await update.message.reply_text("Пройдите тест ещё раз, но теперь нормально!!!",
                                            reply_markup=markup3)
            await update.message.reply_text("Желаю Вам всего хорошего!!!")
            await update.message.reply_text("Надеюсь, Вам понравился бот!!!")
    oo.clear()


async def cc(update, context):
    oo.append("cc")
    if len(oo) == 2:
        await update.message.reply_text("Какая самая большая столица в Северной Америке?\n"
                                        "А) Мехико \n"
                                        "Б) Мексика\n"
                                        "В) Нью-Йорк\n"
                                        "Г) Париж", reply_markup=markup1)
    if len(oo) == 4:
        await update.message.reply_text("Какая река самая короткая в мире?\n"
                                        "А) Репруа \n"
                                        "Б) Репируя\n"
                                        "В) Денизи\n"
                                        "Г) Вологда", reply_markup=markup1)
    if len(oo) == 6:
        await update.message.reply_text("Какой стране принадлежат Канарские острова?\n"
                                        "А) Испании \n"
                                        "Б) Франции\n"
                                        "В) Нидерландам\n"
                                        "Г) Вологде", reply_markup=markup1)
    if len(oo) == 8:
        await update.message.reply_text("Какие две страны граничат непосредственно к северу от Венгрии?\n"
                                        "А) Словакия и Словения \n"
                                        "Б) Словакия и Франции\n"
                                        "В) Нидерланды и Франция\n"
                                        "Г) Вологда и Франция", reply_markup=markup1)
    if len(oo) == 10:
        await update.message.reply_text(
            "Какую страну также называют Нидерландами?\n"
            "А) Голландия \n"
            "Б) Словакия\n"
            "В) Венгрия\n"
            "Г) Россия", reply_markup=markup1)
    if len(oo) == 12:
        await update.message.reply_text("Какую страну также называют Нидерландами?\n"
                                        "А) Восточное Антарктическое плато \n"
                                        "Б) Северное Антлантическое плато\n"
                                        "В) Венгерская равнина\n"
                                        "Г) Россия", reply_markup=markup1)
    if len(oo) == 14:
        await update.message.reply_text("Сколько крупных островов составляют Гавайи?\n"
                                        "А) 8 \n"
                                        "Б) 9\n"
                                        "В) 7\n"
                                        "Г) 69", reply_markup=markup1)
    if len(oo) == 16:
        await update.message.reply_text(
            "Какая самая длинная река в Великобритании?\n"
            "А) Северн\n"
            "Б) Реден\n"
            "В) Санир\n"
            "Г) Золотуха", reply_markup=markup1)
    if len(oo) == 18:
        await update.message.reply_text(
            "В какой стране вы бы нашли город Дрезден?\n"
            "А) Германия\n"
            "Б) Франция\n"
            "В) Айзербайджан\n"
            "Г) Россия", reply_markup=markup1)
    if len(oo) == 20:
        ooa = 0
        oob = 0
        ooc = 0
        ood = 0
        for i in oo:
            if i == "aa":
                ooa += 1
            if i == "bb":
                oob += 1
            if i == "cc":
                ooc += 1
            if i == "dd":
                ood += 1
        if ooa == max(ooa, oob, ooc, ood):
            await update.message.reply_text("Урааааааа!!! Поздравляю!!!")
            await update.message.reply_text("Вы...набрали огромнейшее количество \n"
                                            "баллов за этот труднейший тест!!!")
            await update.message.reply_text("Можете пройти его ещё раз, если Вам так хочется!!!",
                                            reply_markup=markup3)
            await update.message.reply_text("Надеюсь на то, что Вы порекомендуете \n"
                                            "своим друзьям и знакомым этот великолепный \n"
                                            "телеграм-бот!!!")
            await update.message.reply_text("Хорошего дня!!!")
        elif oob == max(ooa, oob, ooc, ood):
            await update.message.reply_text("Неплохая попытка!!!")
            await update.message.reply_text("Вы набрали не так мало баллов, как в теории могли бы, \n"
                                            "но Вам ещё есть куда расти!!!")
            await update.message.reply_text("Надеюсь, Вам понравился бот, можете пройти тест ещё раз!!!",
                                            reply_markup=markup3)
            await update.message.reply_text("Попробуйте уличшить Ваши знания по географии!!!")
            await update.message.reply_text("Удачи Вам!!!")
        elif ooc == max(ooa, oob, ooc, ood):
            await update.message.reply_text("Неплохая попытка!!!")
            await update.message.reply_text("Вы набрали не так мало баллов, как в теории могли бы, \n"
                                            "но Вам ещё есть куда расти!!!")
            await update.message.reply_text("Надеюсь, Вам понравился бот, можете пройти тест ещё раз!!!",
                                            reply_markup=markup3)
            await update.message.reply_text("Попробуйте уличшить Ваши знания по географии!!!")
            await update.message.reply_text("Удачи Вам!!!")
        elif ood == max(ooa, oob, ooc, ood):
            await update.message.reply_text("Не самая плохая попытка, хотя, наверное самая...")
            await update.message.reply_text("Вы очень юморной человек, но вот знаний \n"
                                            "географии Вам не хватает!!!")
            await update.message.reply_text("Пройдите тест ещё раз, но теперь нормально!!!",
                                            reply_markup=markup3)
            await update.message.reply_text("Желаю Вам всего хорошего!!!")
            await update.message.reply_text("Надеюсь, Вам понравился бот!!!")
    oo.clear()


async def dd(update, context):
    oo.append("dd")
    if len(oo) == 2:
        await update.message.reply_text("Какая самая большая столица в Северной Америке?\n"
                                        "А) Мехико \n"
                                        "Б) Мексика\n"
                                        "В) Нью-Йорк\n"
                                        "Г) Париж", reply_markup=markup1)
    if len(oo) == 4:
        await update.message.reply_text("Какая река самая короткая в мире?\n"
                                        "А) Репруа \n"
                                        "Б) Репируя\n"
                                        "В) Денизи\n"
                                        "Г) Вологда", reply_markup=markup1)
    if len(oo) == 6:
        await update.message.reply_text("Какой стране принадлежат Канарские острова?\n"
                                        "А) Испании \n"
                                        "Б) Франции\n"
                                        "В) Нидерландам\n"
                                        "Г) Вологде", reply_markup=markup1)
    if len(oo) == 8:
        await update.message.reply_text("Какие две страны граничат непосредственно к северу от Венгрии?\n"
                                        "А) Словакия и Словения \n"
                                        "Б) Словакия и Франции\n"
                                        "В) Нидерланды и Франция\n"
                                        "Г) Вологда и Франция", reply_markup=markup1)
    if len(oo) == 10:
        await update.message.reply_text(
            "Какую страну также называют Нидерландами?\n"
            "А) Голландия \n"
            "Б) Словакия\n"
            "В) Венгрия\n"
            "Г) Россия", reply_markup=markup1)
    if len(oo) == 12:
        await update.message.reply_text("Какую страну также называют Нидерландами?\n"
                                        "А) Восточное Антарктическое плато \n"
                                        "Б) Северное Антлантическое плато\n"
                                        "В) Венгерская равнина\n"
                                        "Г) Россия", reply_markup=markup1)
    if len(oo) == 14:
        await update.message.reply_text("Сколько крупных островов составляют Гавайи?\n"
                                        "А) 8 \n"
                                        "Б) 9\n"
                                        "В) 7\n"
                                        "Г) 69", reply_markup=markup1)
    if len(oo) == 16:
        await update.message.reply_text(
            "Какая самая длинная река в Великобритании?\n"
            "А) Северн\n"
            "Б) Реден\n"
            "В) Санир\n"
            "Г) Золотуха", reply_markup=markup1)
    if len(oo) == 18:
        await update.message.reply_text(
            "В какой стране вы бы нашли город Дрезден?\n"
            "А) Германия\n"
            "Б) Франция\n"
            "В) Айзербайджан\n"
            "Г) Россия", reply_markup=markup1)
    if len(oo) == 20:
        ooa = 0
        oob = 0
        ooc = 0
        ood = 0
        for i in oo:
            if i == "aa":
                ooa += 1
            if i == "bb":
                oob += 1
            if i == "cc":
                ooc += 1
            if i == "dd":
                ood += 1
        if ooa == max(ooa, oob, ooc, ood):
            await update.message.reply_text("Урааааааа!!! Поздравляю!!!")
            await update.message.reply_text("Вы...набрали огромнейшее количество \n"
                                            "баллов за этот труднейший тест!!!")
            await update.message.reply_text("Можете пройти его ещё раз, если Вам так хочется!!!",
                                            reply_markup=markup3)
            await update.message.reply_text("Надеюсь на то, что Вы порекомендуете \n"
                                            "своим друзьям и знакомым этот великолепный \n"
                                            "телеграм-бот!!!")
            await update.message.reply_text("Хорошего дня!!!")
        elif oob == max(ooa, oob, ooc, ood):
            await update.message.reply_text("Неплохая попытка!!!")
            await update.message.reply_text("Вы набрали не так мало баллов, как в теории могли бы, \n"
                                            "но Вам ещё есть куда расти!!!")
            await update.message.reply_text("Надеюсь, Вам понравился бот, можете пройти тест ещё раз!!!",
                                            reply_markup=markup3)
            await update.message.reply_text("Попробуйте уличшить Ваши знания по географии!!!")
            await update.message.reply_text("Удачи Вам!!!")
        elif ooc == max(ooa, oob, ooc, ood):
            await update.message.reply_text("Неплохая попытка!!!")
            await update.message.reply_text("Вы набрали не так мало баллов, как в теории могли бы, \n"
                                            "но Вам ещё есть куда расти!!!")
            await update.message.reply_text("Надеюсь, Вам понравился бот, можете пройти тест ещё раз!!!",
                                            reply_markup=markup3)
            await update.message.reply_text("Попробуйте уличшить Ваши знания по географии!!!")
            await update.message.reply_text("Удачи Вам!!!")
        elif ood == max(ooa, oob, ooc, ood):
            await update.message.reply_text("Не самая плохая попытка, хотя, наверное самая...")
            await update.message.reply_text("Вы очень юморной человек, но вот знаний \n"
                                            "географии Вам не хватает!!!")
            await update.message.reply_text("Пройдите тест ещё раз, но теперь нормально!!!",
                                            reply_markup=markup3)
            await update.message.reply_text("Желаю Вам всего хорошего!!!")
            await update.message.reply_text("Надеюсь, Вам понравился бот!!!")
    oo.clear()


def main():
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler("help", help))
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("records", records))
    application.add_handler(CommandHandler("author", author))
    application.add_handler(CommandHandler("normal_game", normal_game))
    application.add_handler(CommandHandler("hard_game", hard_game))
    application.add_handler(CommandHandler("a", a))
    application.add_handler(CommandHandler("b", b))
    application.add_handler(CommandHandler("c", c))
    application.add_handler(CommandHandler("d", d))
    application.add_handler(CommandHandler("aa", aa))
    application.add_handler(CommandHandler("bb", bb))
    application.add_handler(CommandHandler("cc", cc))
    application.add_handler(CommandHandler("dd", dd))

    application.run_polling()


if __name__ == '__main__':
    main()
