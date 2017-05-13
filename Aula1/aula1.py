import nltk
from nltk import tokenize
from nltk.corpus import machado

#Parte 1
#Só experimentando o tokenize como substituicao do split()

# tokenize = transformar na menor unidade compreendida pela máquina.
texto = "Veja nesta aula uma boa introdução prática a biblioteca NLTK (Natural Language Toolkit) em Python para Processamento de Linguagem Natural. Eu mostro passo a passo os recursos basicos dessa biblioteca para voce iniciar o estudo nessa area! Veja tambem como o Google utiliza essas tecnicas em seus projetos de pesquisa!"
textoSeparado = texto.replace('!', '.').replace('?', '?.').split('. ')

# separar em frases.
frases = tokenize.sent_tokenize(texto)
print(frases)

#Printa um exemplo em português do Machado de Assis
#print(machado.raw('romance/marm05.txt'))

# separar em palavras
tokens = nltk.word_tokenize(texto)
print(tokens)

#descobrir a frequencia das palavras
frequencia = nltk.FreqDist(frases)
print(frequencia)

# Part Of Speech Tagging
classes = nltk.pos_tag(tokens)
#print(classes)

stopwords = nltk.corpus.stopwords.words('portuguese')
#print(stopwords)
