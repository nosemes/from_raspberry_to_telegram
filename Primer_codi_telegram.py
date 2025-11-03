import random
import telebot
from telebot import custom_filters



bot = telebot.TeleBot("8398261892:AAEf-fgq_UVzA25Uxs8ZXJx-LVwrlBpjZoM") 


@bot.message_handler(commands=['start'])
def not_admin(message):
    temperatura = random.randrange(20,30)
    humitat = random.randrange(50,70)
    bot.send_message(message.chat.id, f'T={temperatura} H={humitat}')
    

# Do not forget to register
bot.add_custom_filter(custom_filters.ChatFilter())
bot.polling(none_stop=True)



'''
Hem instalat telebot amb pip install telebot davant el dubte també fes pip3 install telebot
'''
