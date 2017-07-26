from re import match
from re import search
import re


frases_introdutorias1 = ['oi', 'olá', 'ola']
frases_introdutorias2 = ['bom dia', 'boa tarde', 'boa noite']
frases_introdutorias3 = ['tudo bom', 'como você está']

# List to Regex
def LTR(lista):
    return(r'|'.join(lista))

def introducao(msg):
    res_cumprimento = search(LTR(frases_introdutorias1), msg, re.I)
    res_bom_dia = search(LTR(frases_introdutorias2), msg, re.I) # TODO time dependent
    res_tudo_bom = search(LTR(frases_introdutorias3), msg, re.I)
    print(str(res_tudo_bom) + ' ' + str(msg))
    if(res_cumprimento != None and res_tudo_bom != None):
        return('Olá! Tudo sim, e contigo?')
    elif(res_cumprimento != None):
        return('Olá! Tudo bom?')
    if(res_bom_dia != None and res_tudo_bom != None):
        return('Bom dia! Tudo bem, e contigo?')
    elif(res_bom_dia != None):
        return('Bom dia! Como você está?')
    elif(res_tudo_bom != None):
        return('Tudo sim, e contigo?')
    return(None)

def conversa(mensagem):
    mensagem = mensagem.lower()
    #if(introducao(mensagem) != None):
    return introducao(mensagem)
