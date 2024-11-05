import telebot
import random
from secrets import secrets
from wishes import wishes
from telebot import types

token = secrets.get('BOT_API_TOKEN')
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    start_button = types.KeyboardButton("Старт 🚀")
    action_button = types.KeyboardButton("Пожелание ✨")
    markup.add(start_button, action_button)
    bot.send_message(message.chat.id, text='Привет 👋, {0.first_name}. Если хочешь получить хорошее пожелание на день нажми'
                                           '\nна кнопку "Пожелание ✨". Если хочешь отвлечься'.format(message.from_user), reply_markup = markup)

@bot.message_handler(content_types=['text'])
def buttons(message):
    if(message.text == "Старт 🚀"):
        bot.send_message(message.chat.id, text = "Я могу присылать хорошие пожелания на день, чтобы поднять тебе настроение."
                                                 '\nПросто нажми на кнопку "Пожелание ✨" и увидишь магию')
    elif(message.text == "Пожелание ✨"):
        bot.send_message(message.chat.id, text=f"{random.choice(wishes)}")
    else:
        bot.send_message(message.chat.id, text="Я могу отвечать только на нажатие кнопок")

bot.polling(none_stop=True, interval=0)