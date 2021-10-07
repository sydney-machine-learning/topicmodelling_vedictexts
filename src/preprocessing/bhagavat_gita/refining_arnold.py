# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 15:17:36 2021

@author: Sweta
"""
import re
fileName = "../Gita/Bhagavad_EdwinArnold_refined"
with open(fileName + ".txt", 'r', encoding="utf-8") as f:
    data = f.read()
    f.close()
    
data = data.replace("Š", " - ")
data = data.replace("™", "'")
data = data.replace("ﬂ", "\"")
data = data.replace("ﬁ", "\"")
data = data.replace("\n", "")
data = re.sub(r'\d', "9", data)
data = re.sub(r'FN#99?', "", data)
data = data.replace("[]", "")


data = data.lower()
data = re.sub(r'\s+', " ", data)
data = data.replace("kunti's son", "arjuna")
data = data.replace("subhadra's", "subhadra")
data = data.replace("drupadi's", "drupadi")
data = data.replace("bhishma's", "bhishma")
data = data.replace("lion's", "lion")
data = data.replace("indra's", "indra")
data = data.replace("giant's", "giant")
data = data.replace("kasi's", "kasi")
data = data.replace("victory's", "victory")
data = data.replace("foemen's", "foemen")
data = data.replace("dhritirashtra's", "dhritirashtra")
data = data.replace("o'erwhelm", "overwhelm")
data = data.replace("swarga's", "swarga")
data = data.replace("bidd'st", "biddest")
data = data.replace("heav'n", "heaven")
data = data.replace("wisdom's", "wisdom")
data = data.replace("spirit's", "spirit")
data = data.replace("pritha's", "pritha")
data = data.replace("soul's", "soul")
data = data.replace("sankhya's", "sankhya")
data = data.replace("nature's", "nature")
data = data.replace("body's", "body")
data = data.replace("should'st", "should")
data = data.replace("th'", "the")
data = data.replace("man's", "man")
data = data.replace("shouldst", "should")
data = data.replace("finisheth", "finish")
data = data.replace("wendeth", "wend")
data = data.replace("brahmacharya's", "brahmacharya")
data = data.replace("knoweth", "know")
data = data.replace("bharatas", "bharata")
data = data.replace("teacheth", "teach")
data = data.replace("tis", "it is")
data = data.replace("seeth", "see")
data = data.replace("springeth", "spring")
data = data.replace("brahm", "brahma")
data = data.replace("performeth", "perform")
data = data.replace("ev'n", "even")
data = data.replace("say'st", "say")
data = data.replace("maketh", "make")
data = data.replace("speaketh", "speak")
data = data.replace("spake", "speak")
data = data.replace("heareth", "hear")
data = data.replace("vyasa's", "vyasa")
data = data.replace("krishna's", "krishna")
data = data.replace("brahmaans", "brahmaan")
data = data.replace("bindeth", "bind")
data = data.replace("standeth", "stand")
data = data.replace("vivaswata's", "vivaswata")
data = data.replace("all's", "all is")
data = data.replace("saith", "said")
data = data.replace("speak'st", "speak")
data = data.replace("tisunpleasing", "this is unpleasing")
data = data.replace("helpeth", "help")
data = data.replace("thou", "you")
data = data.replace("thy", "your")
data = data.replace("thine", "yours")
data = data.replace("thee", "you")
data = data.replace("thyself", "yourself")
data = data.replace("mayst", "may")



data = re.sub(r'\[[0-9]*\]', "", data)
data = re.sub(r'\s+', " ", data)
data = data.lower()
data = re.sub(r'\d', "", data)
data = re.sub(r'\s+', " ", data)




outputTextFile = open(fileName + "1.txt",'w', encoding="utf-8")
outputTextFile.write(data)
outputTextFile.close()
