import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from top2vec import Top2Vec

def load_file(cleaned_text_path):
	'''
	load file from given path
	'''
	with open(cleaned_text_path, 'r', encoding='utf-8-sig') as f:
		data = f.read()
		f.close()

	return data

