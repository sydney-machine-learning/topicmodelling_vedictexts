# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 15:17:36 2021

@author: Sweta
"""
import re
import nltk
from nltk.corpus import stopwords
from scipy import spatial
from sent2vec.vectorizer import Vectorizer


fileName = "../Gita/Bhagavad_EdwinArnold"
with open(fileName + "_refined1.txt", 'r', encoding="utf-8") as f:
    data = f.read()
    f.close()
    
data = data.replace("chapter i dhritirashtra: ", "dhritirashtra: ")
data = data.replace("here endeth chapter i. of the bhagavad-gita, entitled \"arjun-vishad,\" or \"the book of the distress of arjuna.\" ", "")
data = data.replace("chapter ii sanjaya.", "\n")
data = data.replace("here endeth chapter ii. of the bhagavad-gita, entitled \"sankhya-yog,\" or \"the book of doctrines.\" ", "")
data = data.replace("chapter iii arjuna.", "\n")
data = data.replace("here endeth chapter iii. of the bhagavad-gita, entitled \"karma-yog,\" or \"the book of virtue in work.\"", "")
data = data.replace("chapter iv krishna.", "\n")
data = data.replace("here endeth chapter iv. of the bhagavad-gita, entitled \"jnana yog,\" or \"the book of the religion of knowledge,\"", "")
data = data.replace("chapter v arjuna.", "\n")
data = data.replace("here ends chapter v. of the bhagavad-gita, entitled \"karmasanyasayog,\" or \"the book of religion by renouncing fruit of works.\"", "")
data = data.replace("chapter vi krishna.", "\n")
data = data.replace("here endeth chapter vi. of the bhagavad-gita, entitled \"atmasanyamayog,\" or \"the book of religion by self-restraint.\"", "")
data = data.replace("chapter vii krishna.", "\n")
data = data.replace("here endeth chapter vii. of the bhagavad-gita, entitled \"vijnanayog,\" or \"the book of religion by discernment.\"", "")
data = data.replace("chapter viii arjuna.", "\n")
data = data.replace("here endeth chapter viii. of the bhagavad-gita, entitled \"aksharaparabrahmaayog,\" or \"the book of religion by devotion to the one supreme god.\"", "")
data = data.replace("chapter ix krishna.", "\n")
data = data.replace("here ends chapter ix. of the bhagavad-gita, entitled \"rajavidyarajaguhyayog,\" or \"the book of religion by the kingly knowledge and the kingly mystery.\"", "")
data = data.replace("chapter x krishna.", "\n")
data = data.replace("here endeth chapter x. of the bhagavad-gita, entitled \"vibhuti yog,\" or \"the book of religion by the heavenly perfections.\"", "")
data = data.replace("chapter xi arjuna.", "\n")
data = data.replace("here endeth chapter xi. of the bhagavad-gita, entitled \"viswarupadarsanam,\" or \"the book of the manifesting of the one and manifold.\"", "")
data = data.replace("chapter xii arjuna.", "\n")
data = data.replace("here endeth chapter xii. of the bhagavad-gita, entitled \"bhaktiyog,\" or\"the book of the religion of faith.\"", "")
data = data.replace("chapter xiii arjuna.", "\n")
data = data.replace("here ends chapter xiii. of the bhagavad-gita, entitled \"kshetrakshetrajnavibhagayog,\" or \"the book of religion by separation of matter and spirit.\"", "")
data = data.replace("chapter xiv krishna.", "\n")
data = data.replace("here ends chapter xiv. of the bhagavad-gita entitled \"gunatrayavibhagayog,\" or \"the book of religion by separation from the qualities.\"", "")
data = data.replace("chapter xv krishna.", "\n")
data = data.replace("here ends chapter xv. of the bhagavad-gita entitled \"purushottamapraptiyog,\" or \"the book of religion by attaining the supreme.\"", "")
data = data.replace("chapter xvi krishna.", "\n")
data = data.replace(" . . . . . . . . . . . . here endeth chapter xvi. of the bhagavad-gita, entitled \"daivasarasaupadwibhagayog,\" or \"the book of the separateness of the divine and undivine.\"", "")
data = data.replace("chapter xvii arjuna.", "\n")
data = data.replace("here endeth chapter xvii. of the bhagavad-gita, entitled \"sraddhatrayavibhagayog,\" or \"the book of religion by the threefold kinds of faith.\"", "")
data = data.replace("chapter xviii arjuna.", "\n")
data = data.replace("here ends, with chapter xviii., entitled \"mokshasanyasayog,\" or \"the book of religion by deliverance and renunciation,\" the bhagavad-gita. some repetitionary lines are here omitted. technical phrases of vedic religion. the whole of this passage is highly involved and difficult to render. i feel convinced sankhyanan and yoginan must be transposed here in sense. i am doubtful of accuracy here. a name of the sun. wiyout desire of fruit. that is,\"joy and sorrow, success and failure, heat and cold,\"&c. i.e., the body. the sanskrit has this play on the double meaning of atman. so in original. beings of low and devilish nature. krishna. i read here janma, \"birth;\" not jara,\"age\" i have discarded ten lines of sanskrit text here as an undoubted interpolation by some vedanthis ist the sanskrit poem here rises to an elevation of style and manner which i have endeavoured to mark by change of metre. ahinsa. the nectar of immortality. called \"the jap.\" the compound form of sanskrit words. \"kamalapatraksha\" these are all divine or deified orders of the hindoo pantheon. \"hail to you, god of gods! be favourable!\" the wind. \"not peering about,\"anapeksha. the calcutta edition of the mahabharata has these three opening lines. this is the nearest possible version of kshetrakshetrajnayojnanan yat tajnan matan mama. i omit two lines of the sanskrit here, evidently interpolated by some vedanthis ist. wombs. i do not consider the sanskrit verses here-which are somewhat freely rendered - \"an attack on the authority of the vedas,\" with mr davies, but a beautiful lyrical episode, a new \"parable of the fig-tree.\" i omit a verse here, evidently interpolated. \"of the asuras,\"lit. i omit the ten concluding shlokas, with mr davis. rakshasas and yakshas are unembodied but capricious beings of great power, gifts, and beauty, same times also of benignity. these are spirits of evil wandering ghosts. yatayaman, food which has remained after the watches of the night. in india this would probably \"go bad.\" i omit the concluding shlokas, as of very doubtful authenticity. end of the project gutenberg etext, the bhagavad-gita, translated by sir edwin arnold", "")
data = data.replace("?", ".")
data = data.replace("!", ".")
data = "".join([character if (character.isalnum() or character == "." or character ==" " or character == "\n") else " " for character in data])
data = re.sub(r'  ', " ", data)
data = data.replace(". .", ".")

paragraphs = data.split("\n")
paragraphs = paragraphs[:18]
stopwrds = stopwords.words('english')
stopwrds.remove('not')
stopwrds.remove('no')
stopwrds.append('.')
tokenized_paragraphs = []
for paragraph in paragraphs:
    sentences = nltk.sent_tokenize(paragraph)
    sentences = [nltk.word_tokenize(sentence) for sentence in sentences if len(nltk.word_tokenize(sentence))>2]
    for i in range(len(sentences)):
        sentences[i] = [word for word in sentences[i] if word not in stopwrds]
    sentences = [sentence for sentence in sentences if (len(sentence)>2)]
    tokenized_paragraphs.append(sentences)
    
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import os
from subprocess import check_output
from wordcloud import WordCloud, STOPWORDS
import string
import re 
import nltk

#%%
plt.figure(figsize = (10,10))
wordcloud = WordCloud(
                      background_color = 'white',
                      stopwords=stopwrds,
                      max_words = 50,
                      max_font_size = 120,
                      random_state = 42
                    ).generate(data)

#Plotting the word cloud
plt.imshow(wordcloud)
plt.title("WORD CLOUD for whole book", fontsize = 20)
plt.axis('off')
plt.show()
#%%   
for i in range(len(paragraphs)): 
    plt.figure(figsize = (10,10))
    wordcloud = WordCloud(
                          background_color = 'white',
                          stopwords=stopwrds,
                          max_words = 50,
                          max_font_size = 120,
                          random_state = 42,
                        ).generate(paragraphs[i])
    
    #Plotting the word cloud
    plt.imshow(wordcloud)
    plt.title("WORD CLOUD for chapter " + str(i+1), fontsize = 20)
    plt.axis('off')
    plt.show()

#%%
from nltk import ngrams
from collections import Counter
unigrams=[]
for paragraph in paragraphs:
    paragraph = paragraph.replace(".", " ")
    paragraph = paragraph.replace("  ", " ")
    tokenized_paragraph = paragraph.split()
    tokenized_paragraph = [word for word in tokenized_paragraph if word not in stopwrds]
    unigrams.append(Counter(tokenized_paragraph))

#%%

vectorizer = Vectorizer()
vectorizer.bert(paragraphs[:3])
vectors_bert = vectorizer.vectors

#%%
dist_1 = spatial.distance.cosine(vectors_bert[0], vectors_bert[1])
dist_2 = spatial.distance.cosine(vectors_bert[0], vectors_bert[2])