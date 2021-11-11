"""
Run experiments for different version of topic model

   		dimReduction 	Clustering
1. 		UMAP			HDBSCAN
2. 		UMAP			KMeans
3. 		PCA				HDBSCAN
4. 		PCA				KMeans

Sentence Embedding models
1. SBERT
2. Universal Sentence Encoder

"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


from topics.topic_model import TopicModel
import argparse


parser = argparse.ArgumentParser()
#UMAP arguments
parser.add_argument('--feature', dest='feature', default=False, action='store_true')
parser.add_argument('--version', type=str, default = 'v11',help='version of the experiment')
parser.add_argument('--resume_epoch', type=int, help='initial epoch to resume training')

args = parser.parse_args()

#umap Args
n_neighbors = args.n_neighbors
n_components = args.n_components
metric = args.metric
random_state = args.random_state

if use_umap:
	umap_args = {'n_neighbors': int(n_neighbors),
	             'n_components': int(n_components),
	             'metric': metric,
	             "random_state": int(random_state)
	             }


hdbscan_args = {'min_cluster_size': 10,
                'min_samples':5,
                'metric': 'euclidean',
                'cluster_selection_method': 'eom'
             }