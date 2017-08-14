from re import match
from re import search
import re

# TODO: Consertar possível problema
def remocao_abreviacoes(msg):
    abreviacoes_comuns = {'vc':'voce',
                          'vcs':'voces',
                          'gnt':'gente',
                          'gnts':'gente',
                          'blz':'beleza',
                          'bl':'beleza',
                          'qt':'quanto',
                          'qts':'quantos'}
    for palavra in abreviacoes_comuns:
        msg = msg.replace(palavra, abreviacoes_comuns[palavra])
    return msg

# TODO: Consertar possível problema
def remocao_intensidade(msg):
    intensidades_comuns = ['muito','demais','pouco','tão']
    for palavra in intensidades_comuns:
        msg = msg.replace(palavra + ' ', '')
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

# List to Regex
def LTR(lista):
    return(r'|'.join(lista))

def introducao(msg):
    frases_introdutorias1 = ['oi', 'ola']
    frases_introdutorias2 = ['bom dia', 'boa tarde', 'boa noite']
    frases_introdutorias3 = ['tudo bom', 'tudo bem']
    frases_introdutorias4 = ['como voce esta', 'como vc esta', 'voce esta bem', 'vc esta bem']
    frase_positiva = ['sim', 'tudo sim']
    frase_negativa = ['nao']
    frase_de_volta = ['e contigo', 'e com voce', 'e com vc', 'e cm vc', 'e com voce', 'e vc', 'e voce']
    comeco_brusco = ['estou triste', 'ando triste']

    res_cumprimento = search(LTR(frases_introdutorias1), msg, re.I)
    res_bom_dia = search(LTR(frases_introdutorias2), msg, re.I) # TODO time dependent
    res_tudo_bom1 = search(LTR(frases_introdutorias3), msg, re.I)
    res_tudo_bom2 = search(LTR(frases_introdutorias4), msg, re.I)

    res_avalp = search(LTR(frase_positiva), msg, re.I)
    res_avaln = search(LTR(frase_negativa), msg, re.I)
    res_avalv = search(LTR(frase_de_volta), msg, re.I)

    res_comeco_brusco = search(LTR(comeco_brusco), msg, re.I)

    # TODO Refatorar esse monte de ifs
    # https://www.youtube.com/watch?v=poz6W0znOfk
    if(res_cumprimento != None):
        if(res_tudo_bom1 != None):
            return('Olá! Tudo sim, e contigo?')
        return('Olá! Tudo bom?')

    elif(res_bom_dia != None):
        if(res_tudo_bom1 != None):
            return('Bom dia! Tudo bem, e contigo?')
        elif(res_tudo_bom2 != None):
            return('Bom dia! Estou bem, e você?')
        return('Bom dia! Como você está?')

    elif(res_tudo_bom1 != None):
        return('Tudo sim, e contigo?')
    elif(res_tudo_bom2 != None):
        return('Estou bem, e você?')

    elif(res_avalp != None):
        if(res_avalv != None):
            return('Também! E aí, quais as novidades?')
        return('Nossa, obrigado por perguntar se eu tô bem. Quais as novidades?')

    elif(res_avaln != None):
        if(res_avalv != None):
            return('Estou bem, mas o que houve contigo? Quer conversar sobre isso?')
        return('O que houve? Quer conversar sobre isso?')

    elif(res_comeco_brusco != None):
        return('O que houve? Quer conversar?')

    return (None)

# Função principal
# Onde toda a conversa começa e termina
def conversa(mensagem):

    # Tratamento da mensagem
    mensagem = mensagem.lower()
    mensagem = remocao_intensidade(mensagem)
    mensagem = remocao_acentos(mensagem)
    mensagem = remocao_abreviacoes(mensagem)

    print(mensagem)

    # Começo do diálogo
    if(introducao(mensagem) != None):
        return introducao(mensagem)
    else:
        return("WAT??")



# RASCUNHO
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