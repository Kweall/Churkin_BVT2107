import telebot
import random
from telebot import types
token = "5034193292:AAFmltHCQL31CeS9FB0UzfgeK_UrOnGVwC4"
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.row("Хочу", "/help")
    bot.send_message(message.chat.id, 'Привет! Хочешь узнать свежую информацию о МТУСИ?', reply_markup=keyboard)


@bot.message_handler(commands=['help'])
def start_message(message):
    bot.send_message(message.chat.id, 'Я умею много чего (на самом деле не очень много).\n'
                                      'Список команд:\n'
                                      '/start - Начать диалог\n'
                                      '/randomnumber - выбираю любое число от 0 до 1000\n'
                                      '/grustno - попытаюсь помочь преодолеть грусть\n'
                                      'А еще ты можешь спросить у меня "кто ты?", "сколько тебе лет?", "как дела?"\n')


@bot.message_handler(commands=['randomnumber'])
def start_message(message):
    bot.send_message(message.chat.id, random.randint(0,1000))

@bot.message_handler(commands=['grustno'])
def start_message(message):
    a = random.randint(1,3)
    b = a
    if b == 1:
        bot.send_message(message.chat.id, 'Наелся мужик дрожжей - теперь ходит, бродит')
    if b == 2:
        bot.send_message(message.chat.id, 'Подползает червячок к своей маме, спрашивает: "Мам, а где папа?", а она отвечает: "С мужиками на рыбалку поехал"')
    if b == 3:
        bot.send_message(message.chat.id, 'Хулиганы избили оптимиста до полужизни')


@bot.message_handler(content_types=['text'])
def answer(message):
    if message.text.lower() == "хочу":
        bot.send_message(message.chat.id, 'Тогда тебе сюда – https://mtuci.ru/')
    if message.text.lower() == "кто ты?":
        bot.send_message(message.chat.id, 'Я обычный телеграм-бот, который был создан микрочелом')
    if message.text.lower() == "сколько тебе лет?":
        bot.send_message(message.chat.id, 'Неважно (я несовершеннолетний)')
    if message.text.lower() == "как дела?":
        bot.send_message(message.chat.id, 'Как дела могут быть у бота? У меня всегда всё хорошо. Надеюсь, у тебя тоже :) Если тебе грустно, введи команду "/grustno"')


bot.polling()