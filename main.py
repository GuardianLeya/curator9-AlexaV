import telebot

bot = telebot.TeleBot('6757099147:AAHyq9iIRrkmsnop68XnlNYO7FKpWpHQBKc')


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'Мы Вас приветствуем!')


@bot.message_handler(commands=['run'])
def main(message):
    bot.send_message(message.chat.id, '*торопись!*беги!!!', parse_mode='markdown')


@bot.message_handler(commands=['link'])
def main(message):
    bot.send_message(message.chat.id, 'ЭТО [ССЫЛКА](https://pastebin.com/)', parse_mode='markdown')


bot.infinity_polling()
