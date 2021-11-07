import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import torch

from top2vec import Top2Vec
import umap
import hdbscan
from get_embeddings import *


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
    #Set a fixed value for the hash seed
    os.environ['PYTHONHASHSEED'] = str(seed)
# set_seed()


def train_topics_model(documents, embedding_model='distiluse-base-multilingual-cased', num_topics = 10, speed = 'learn', random_state = 42):
    """
    Returns model and topics
    embedding_models: `universal-sentence-encoder`
                      `universal-sentence-encoder_-multilingual`
                      `distiluse-base-multilingual-cased`
    speed:            `learn`
                      `deep-learn`
                      `fast-learn`
    """
    umap_args = {"random_state": random_state}
    model = Top2Vec(documents = documents, speed = speed, workers = 8, min_count = 2, embedding_model= embedding_model, umap_args = umap_args)
    if model.get_num_topics() > num_topics:
      topic_words, word_scores, topic_nums = model.get_topics(num_topics)
    else:
      topic_words, word_scores, topic_nums = model.get_topics()

    return model, topic_words, word_scores, topic_nums


def get_words(model, num_words = 20, num_topics = 10):
    """
    get n random words from each topics
    """
    reduced_flag = False
    if model.get_num_topics() > num_topics:
      reduced_topic_lists = model.hierarchical_topic_reduction(num_topics = num_topics)
      reduced_flag = True
    
    topic_words, word_scores, topic_nums = model.get_topics(reduced=reduced_flag)

    return topic_words[:,:num_words], word_scores[:,:num_words], topic_nums


def save_all_topics(model, embedding_model, path = 'principal_upanishads_topic.json'):
    '''
    Save the topics of a particular datasets as json file

    Args:
    -----
    model: trained model
    embedding_model: name of the embedding model
    path: path to save the topics
    '''
    topic_words, word_scores, topic_nums = model.get_topics()
    topic_dict = {}
    topic_dict = {'embedding_model':{'topic-words':topic_words.tolist(), 'word_score': word_scores.tolist()}}
    with open(path, 'w') as fp:
        json.dump(topic_dict, fp, indent = 2)


def plot2d_df(result, palet, img_name = 'no_name_2d_plot.pdf'):

    clrs = sns.color_palette(palet).as_hex()
    # color_palette = [cpt for cpt in clrs]
    #palette = sns.color_palette(palet)
    x = result['x_embeddings']
    y = result['y_embeddings']
    # z = result['z_embeddings']
    fig = plt.figure(figsize=(24,16))
    ax = fig.add_subplot(111)
    
    ax.set_xlabel('UMAP Embedding (dim = 1)')
    ax.set_ylabel('UMAP Embedding (dim = 2)')

    fig.patch.set_facecolor('lavender')
    ax.set_facecolor('lavender')

    result = result.sort_values(by=['Labels'])
    for idx, topics in enumerate(result.Labels.unique()):
        ax.scatter(x[result.Labels == topics],y[result.Labels == topics],label = topics, c = clrs[idx])
    
    ax = plt.gca()

    #set y-axes to right side
    ax.yaxis.set_label_position("right")
    ax.yaxis.tick_right()

    handles, labels = ax.get_legend_handles_labels()
    # sort both labels and handles by labels
    labels, handles = zip(*natsorted(zip(labels, handles), key=lambda t: t[0]))
    ax.legend(handles, labels, loc='center right', bbox_to_anchor=(0.15, 0.75), title="Labels")
    plt.tight_layout()
    plt.savefig(img_name, bbox_inches = 'tight',dpi = 200, facecolor=fig.get_facecolor(), edgecolor='none')




def plot3d_df(result, palet, img_name = 'no_name_image_3d.pdf'):

    result = result.sort_values(by=['Labels'])
    fig = plt.figure(figsize=(24,16))
    ax = fig.add_subplot(111, projection='3d')

    fig.patch.set_facecolor('lavender')
    ax.set_facecolor('lavender')

    x = result['x_embeddings']
    y = result['y_embeddings']
    z = result['z_embeddings']
    
    ax.set_xlabel('UMAP Embedding (dim = 1)', labelpad = 40.0)
    ax.set_ylabel('UMAP Embedding (dim = 2)', labelpad = 40.0)
    ax.set_zlabel('UMAP Embedding (dim = 3)', labelpad = 40.0)

    clrs = sns.color_palette(palet).as_hex()

    for idx, topics in enumerate(result.Labels.unique()):
        ax.scatter(x[result.Labels == topics],y[result.Labels == topics],
                   z[result.Labels == topics],label = topics, c = clrs[idx])
    
    handles, labels = ax.get_legend_handles_labels()
    # sort both labels and handles by labels
    labels, handles = zip(*natsorted(zip(labels, handles), key=lambda t: t[0]))
    ax.legend(handles, labels, loc='best', bbox_to_anchor=(0.15, 1.0), title="Labels")
    plt.tight_layout()
    plt.savefig(img_name, dpi = 150)



