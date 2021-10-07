# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 15:17:36 2021

@author: Sweta
"""
import re
fileName = "../Gita/Output/Gita-According-to-Gandhi"
with open(fileName + ".txt", 'r', encoding="utf-8") as f:
    data = f.read()
    f.close()
    
data = re.sub(r'\n[0-9]+\n', "", data)




outputTextFile = open(fileName + "_refined1.txt",'w', encoding="utf-8")
outputTextFile.write(data)
outputTextFile.close()
