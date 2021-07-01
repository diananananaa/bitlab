import telebot
import os
import random

bot = telebot.TeleBot("1809638060:AAEn3-e0OLi7QmXc7Ij8SB4fN0XIZu3PI5c")


def log(message, answer):
    print("\n ------------")
    from datetime import datetime
    print(datetime.now())
    print("Сообщение от {0} {1}. (id = {2}) \n Текст - {3}".format(message.from_user.first_name,

                                                                   message.from_user.last_name,

                                                                   str(message.from_user.id),

                                                                   message.text))


@bot.message_handler(commands=["start"])
def handle_start(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
    user_markup.row('/start', '/stop')
    user_markup.row('фото', 'аудио', 'документы')
    user_markup.row('стикер', 'локация')

    bot.send_message(message.from_user.id, 'Добро пожаловать', reply_markup=user_markup)


@bot.message_handler(commands=["stop"])
def handle_start(message):

    hide_markup = telebot.types.ReplyKeyboardRemove()
    bot.send_message(message.from_user.id, 'До свидания', reply_markup=hide_markup)


@bot.message_handler(content_types=["text"])
def handle_text(message):
    if message.text == 'фото':

        directory = 'C:/Users/diano/Pictures/Camera Roll'
        img = open(directory + '/' + "S1.png", 'rb')
        bot.send_chat_action(message.from_user.id, 'upload_photo')
        bot.send_photo(message.from_user.id, img)
        img.close()

    elif message.text == 'документы':

        directory = '/Users/diano/Dropbox/Мой ПК (LAPTOP-06Q0G2HV)/Desktop/школьные конспекты/госы'
        all_files_in_directory = os.listdir(directory)
        print(all_files_in_directory)

        for files in all_files_in_directory:

            document = open(directory + '/' + files, 'rb')
            bot.send_chat_action(message.from_user.id, 'upload_document')
            bot.send_document(message.from_user.id, document)
            document.close()



@bot.message_handler(content_types=["text"])
def handle_text(message):
    answer = "Извините, я еще не научился отвечать на такие сообщения"

    if message.text.lower() == "привет":

        answer = "Приветствую"
        bot.send_message(message.chat.id, answer)
        log(message, answer)

    elif message.text.lower() == "как дела?":

        answer = "Хорошо,как у тебя?"
        bot.send_message(message.chat.id, answer)
        log(message, answer)

    elif message.text.lower() == "хорошо":

        answer = "Классно, хорошего дня"
        bot.send_message(message.chat.id, answer)
        log(message, answer)

    else:

        bot.send_message(message.chat.id, answer)
        log(message, answer)


bot.polling(none_stop=True, interval=0)