import pickle
import nltk

text = "Veja nesta aula uma boa introducao pratica a biblioteca NLTK (Natural Language Toolkit) em Python para Processamento de Linguagem Natural. Eu mostro passo a passo os recursos basicos dessa biblioteca para voce iniciar o estudo nessa area! Veja tambem como o Google utiliza essas tecnicas em seus projetos de pesquisa!"
tagger = pickle.load(open('tagger.pkl'))
portuguese_sent_tokenizer = nltk.data.load("tokenizers/punkt/portuguese.pickle")
sentences = portuguese_sent_tokenizer.tokenize(text)
tags = [tagger.tag(nltk.word_tokenize(sentence)) for sentence in sentences]
print(sentences)
