import sys
import time
import configparser
import telepot
import chats


def onChatMessage(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id)
    
    if (content_type == 'text'):
        botSays = chats.conversa(msg['text'])
        if(botSays == None):
            botSays = "Não compreendi o que você falou... Ainda não estou completo 😢"
        bot.sendMessage(chat_id=chat_id, text=botSays)
    else:
        bot.sendMessage(chat_id=chat_id, text="Dá pra mandar a porra de um texto?!?")


config = configparser.ConfigParser()
config.read_file(open('config.ini'))

bot = telepot.Bot(config['DEFAULT']['token'])
bot.message_loop({'chat': onChatMessage,},
                run_forever='Listening ...')
print('Listening ...')
