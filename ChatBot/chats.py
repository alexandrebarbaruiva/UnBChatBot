from re import match
from re import search
import re

def remocao_acentos(msg):
    indesejados = {'á':'a',
                   'ã':'a',
                   'à':'a',
                   'â':'a',
                   'é':'e',
                   'ê':'e',
                   'í':'i',
                   'ì':'i',
                   'ó':'o',
                   'õ':'o',
                   'ô':'o',
                   'ú':'u'}
    for letra in indesejados:
        msg = msg.replace(letra, indesejados[letra])
    return msg

# List to Regex
def LTR(lista):
    return(r'|'.join(lista))

def introducao(msg):
    frases_introdutorias1 = ['oi', 'ola']
    frases_introdutorias2 = ['bom dia', 'boa tarde', 'boa noite']
    frases_introdutorias3 = ['tudo bom', 'como voce esta', 'tudo bem']
    frase_positiva = ['sim', 'tudo sim']
    frase_negativa = ['nao']
    frase_de_volta = ['e contigo', 'e com voce', 'e com vc', 'e cm vc', 'e com voce', 'e vc', 'e voce']

    res_cumprimento = search(LTR(frases_introdutorias1), msg, re.I)
    res_bom_dia = search(LTR(frases_introdutorias2), msg, re.I) # TODO time dependent
    res_tudo_bom = search(LTR(frases_introdutorias3), msg, re.I)

    res_avalp = search(LTR(frase_positiva), msg, re.I)
    res_avaln = search(LTR(frase_negativa), msg, re.I)
    res_avalv = search(LTR(frase_de_volta), msg, re.I)

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

    if(res_avalp != None and res_avalv != None):
        return('Também! E aí, quais as novidades?')

    if(res_avaln != None and res_avalv != None):
        return('Estou bem, mas o que houve contigo? Quer conversar sobre isso?')
    return(None)

# Função principal
# Onde toda a conversa começa e termina
def conversa(mensagem):
    mensagem = mensagem.lower()
    mensagem = remocao_acentos(mensagem)
    #if(introducao(mensagem) != None):
    return introducao(mensagem)
