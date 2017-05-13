import telepot
import configparser

def onChatMessage(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id)
    msg['text'] = msg['text'].lower()
    if content_type == 'text':
        #bot.sendMessage(chat_id, msg['text'])
        
        # Onde residirá toda a conversa
        if msg['text'] == 'bom dia' or msg['text'] == 'boa tarde' or msg['text'] == 'olá' or msg['text'] == 'oi':
            bot.sendMessage(chat_id, "Olá, tudo bom?")

    elif content_type == 'sticker':
        bot.sendMessage(chat_id, 'Sticker legal')
    elif content_type == 'document':
        bot.sendMessage(chat_id, "Massa... O que eu tenho a ver com isso?")

config = configparser.ConfigParser()
config.read_file(open('config.ini'))

bot = telepot.Bot(config['DEFAULT']['token'])
bot.message_loop({'chat': onChatMessage,},
                run_forever='Listening ...')
