import nltk
from nltk import tokenize

#Parte 1
texto = "Veja nesta aulá uma introducao pratica a biblioteca NLTK (Natural Language Toolkit) em Python para Processamento de Linguagem Natural. Eu mostro passo a passo os recursos basicos dessa biblioteca para voce iniciar o estudo nessa area! Veja tambem como o Google utiliza essas tecnicas em seus projetos de pesquisa!"
textoSeparado = texto.replace('!', '.').replace('?', '?.').split('. ')
frases = tokenize.sent_tokenize(texto)
#print(frases)

#Parte 2

tokens = nltk.word_tokenize(texto)
#print(tokens)

classes = nltk.pos_tag(tokens)

print(classes)
