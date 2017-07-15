import nltk
import tokenizer
from nltk.corpus import machado

#Parte 1
#Só experimentando o tokenize como substituicao do split()
texto = "Veja nesta aula uma boa introdução pratica a biblioteca NLTK (Natural Language Toolkit) em Python para Processamento de Linguagem Natural. Eu mostro passo a passo os recursos basicos dessa biblioteca para voce iniciar o estudo nessa area! Veja tambem como o Google utiliza essas tecnicas em seus projetos de pesquisa!"
textoSeparado = texto.replace('!', '.').replace('?', '?.').split('. ')
frases = tokenizer.tokenize(texto)
#print(frases)

#Printa um exemplo em português do Machado de Assis
#print(machado.raw('romance/marm05.txt'))

#Parte 2

tokens = nltk.word_tokenize(texto)
#print(tokens)

classes = nltk.pos_tag(tokens)
print(classes)

stopwords = nltk.corpus.stopwords.words('portuguese')
#print(stopwords)
