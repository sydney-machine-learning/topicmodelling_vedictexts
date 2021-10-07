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

def set_seed(seed = 42):
    '''Sets the seed of the entire notebook so results are the same every time we run.
    This is for REPRODUCIBILITY.'''
    np.random.seed(seed)
    random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed(seed)
    # When running on the CuDNN backend, two further options must be set
    torch.backends.cudnn.deterministic = True
    torch.backends.cudnn.benchmark = True
    Set a fixed value for the hash seed
    os.environ['PYTHONHASHSEED'] = str(seed)
set_seed()

