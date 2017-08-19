from re import match
from re import search
import re

def remocao_abreviacoes(msg):
    abreviacoes_comuns = {'vc':'voce',
                          'vcs':'voces',
                          'gnt':'gente',
                          'gnts':'gente',
                          'blz':'beleza',
                          'bl':'beleza',
                          'qt':'quanto',
                          'qts':'quantos',
                          'cm':'com'}
    for palavra in abreviacoes_comuns:
        msg = msg.replace((' ' + palavra), ' ' + abreviacoes_comuns[palavra])
        msg = msg.replace((palavra + ' '), abreviacoes_comuns[palavra] + ' ')
    return msg

def remocao_intensidade(msg):
    intensidades_comuns = ['muito','demais','pouco','tão']
    for palavra in intensidades_comuns:
        msg = msg.replace((' ' + palavra), '')
        msg = msg.replace((palavra + ' '), '')
    return msg

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

def formatarMensagem(mensagem):
    mensagem = mensagem.lower()
    mensagem = remocao_intensidade(mensagem)
    mensagem = remocao_acentos(mensagem)
    mensagem = remocao_abreviacoes(mensagem)
    return mensagem

# List to Regex
def LTR(lista):
    return(r'|'.join(lista))

def verifica(frases, msg):
    return search(LTR(frases), msg, re.I)

def introducao(msg):
    frases_introdutorias1 = ['oi', 'ola', 'hello']
    frases_introdutorias2 = ['bom dia', 'boa tarde', 'boa noite']
    frases_introdutorias3 = ['tudo bom', 'tudo bem']
    frases_introdutorias4 = ['como voce esta', 'voce esta bem']
    frase_positiva = ['sim', 'tudo sim', 'tudo']
    frase_negativa = ['nao']
    frase_de_volta = ['e contigo', 'e com voce', 'e com voce', 'e voce']
    comeco_brusco = ['estou triste', 'ando triste']

    res_bom_dia = verifica(frases_introdutorias2, msg) # TODO time dependent

    # TODO Refatorar esse monte de ifs
    # https://www.youtube.com/watch?v=poz6W0znOfk
    if(verifica(frases_introdutorias1, msg) != None):
        if(verifica(frases_introdutorias3, msg) != None):
            return('Olá! Tudo sim, e contigo?')
        return('Olá! Tudo bom?')

    elif(res_bom_dia != None):
        if(verifica(frases_introdutorias3, msg) != None):
            return('Bom dia! Tudo bem, e contigo?')
        elif(verifica(frases_introdutorias4, msg) != None):
            return('Bom dia! Estou bem, e você?')
        return('Bom dia! Como você está?')

    elif(verifica(frases_introdutorias3, msg) != None):
        return('Tudo sim, e contigo?')
    elif(verifica(frases_introdutorias4, msg) != None):
        return('Estou bem, e você?')

    elif(verifica(frase_positiva, msg) != None):
        if(verifica(frase_de_volta, msg) != None):
            return('Também! E aí, quais as novidades?')
        return('Nossa, obrigado por perguntar se eu tô bem. Quais as novidades?')

    elif(verifica(frase_negativa, msg) != None):
        if(verifica(frase_de_volta, msg) != None):
            return('Estou bem, mas o que houve contigo? Quer conversar sobre isso?')
        return('O que houve? Quer conversar sobre isso?')

    elif(verifica(comeco_brusco, msg) != None):
        return('O que houve? Quer conversar?')

    return (None)

# Função principal
# Onde toda a conversa começa e termina

# def conversa(mensagem, id)
def conversa(mensagem):
    # verifica conversa anterior com id para continuar conversa

    # Tratamento da mensagem
    mensagem = formatarMensagem(mensagem)
    print(mensagem)

    # Começo do diálogo
    if(introducao(mensagem) != None):
        return introducao(mensagem)



# FIXME/REWORK
# Criar um objeto chamado conversa
# Nele contem informações sobre a conversa, tal como o que foi dito anteriormente,

# class Chatbot(){
#     ultimaMSG = ""
#     dialogoAtual =
#        {
#           introducao = 0,
#           dialogoNormal = 0,
#
#     }
# }
