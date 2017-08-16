import sys
import time
import configparser
import telepot
import chats
from pprint import pprint

lastMessage = ''

def onChatMessage(msg):
    print(msg)
    content_type, chat_type, chat_id = telepot.glance(msg)
    # print(content_type, chat_type, chat_id)

    if (content_type == 'text'):
        print(msg['text'])
        if(msg['text'] == '/start'):
            botSays = 'Olá, eu sou o UnBChatBot, estou aqui para aqueles momentos que você quiser conversar!'
        else:
            botSays = chats.conversa(msg['text'])
            if(botSays == None and msg['text'] != 'a'):
                botSays = "Não compreendi o que você falou... Ainda não estou completo 😢"
        bot.sendMessage(chat_id=chat_id, text=botSays)
    else:
        bot.sendMessage(chat_id=chat_id, text="Dá pra mandar a porra de um texto?!?")

    # Atualiza ultima coisa falada pelo usuário
    lastMessage = msg['text']


config = configparser.ConfigParser()
config.read_file(open('config.ini'))

bot = telepot.Bot(config['DEFAULT']['token'])
bot.message_loop({'chat': onChatMessage},
                run_forever='Listening ...')
print('Listening ...')
