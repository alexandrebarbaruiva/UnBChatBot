import random
import telepot
import re
import configparser
import nltk
import datetime

FRASES_INTRODUTORIAS = ['bom dia', 'boa tarde', 'boa noite', 'oi', 'olá', 'ola', '/start']
#FRASES_SOBRE_BOT
# ...
VERBOS_NEUTROS = ['correr', 'comer']
VERBOS_NEGATIVOS = ['morrer', 'matar', 'suicidar']

RESPOSTA_PARA_NEGATIVO = ['Ok', 'Ah, tá']

horario = datetime.datetime.now()
print(horario)
print('Hora {:%H}'.format(horario))


def listToRegex(lista):
    return (r'|'.join(lista))

def hasIntroduction(msg):
    result = re.match(listToRegex(FRASES_INTRODUTORIAS), msg, re.I)
    return result


def onChatMessage(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id)

    #msg['text'] = msg['text'].lower()
    if content_type == 'text':
        #bot.sendMessage(chat_id, msg['text'])

        # Onde residirá toda a conversa
        # TODO
        # REMOVER ACENTUAçÃO
        #
        tokenized = nltk.word_tokenize(msg['text'])
        #classes = nltk.pos_tag(tokenized)
        #print(classes)
        if hasIntroduction(msg['text']) is not None:
            hora = int('{:%H}'.format(horario))
            if hora >= 6 and hora <= 12:
                bot.sendMessage(chat_id, "Bom dia!")
            elif hora >12 and hora <18:
                bot.sendMessage(chat_id, "Boa Tarde!")
            else:
                bot.sendMessage(chat_id, "Boa Noite!")

        for word in tokenized:
            if word.lower() in VERBOS_NEGATIVOS:
                bot.sendMessage(chat_id, random.choice(RESPOSTA_PARA_NEGATIVO))

    elif content_type == 'sticker':
        bot.sendMessage(chat_id, 'Sticker legal')
    elif content_type == 'document':
        bot.sendMessage(chat_id, "Massa... O que eu tenho a ver com isso?")

config = configparser.ConfigParser()
config.read_file(open('config.ini'))
TOKEN = config['DEFAULT']['token']

bot = telepot.Bot(TOKEN)
bot.message_loop({'chat': onChatMessage,},
                run_forever='Listening ...')
