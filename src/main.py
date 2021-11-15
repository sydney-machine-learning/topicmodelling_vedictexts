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
import os, sys, time
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


from topics.topic_model import TopicModel
import argparse
import yaml

doc_root = '../assets'
#####################################
parser = argparse.ArgumentParser()
parser.add_argument('--version', type=str, default = 'v1',help='version of the experiment')
parser.add_argument('--file-name', type=str,help='file name which you want to use from assets')
parser.add_argument('--texts', type=str, default = 'upanishad',help='whether to use Gita or Upanishads')
# parser.add_argument('--dim', type = str, default='umap', help='umap or pca for dimensionality reduction')
# parser.add_argument('--nn', type=int, default = 10, help='n_neighbors parameters for umap')
# parser.add_argument('--nc', type = int, default = 5, help = 'n_components parameters for umap')
# parser.add_argument('--metric', type = str, default = 'cosine', help = 'metric parameters for umap')
# parser.add_argument('--random-state', type = int, default = 42, help = 'random_state parameter of umap')
# parser.add_argument('--cluster', type=str, default = 'hdbscan',help='hdbscan or k-means for clustering')

args = parser.parse_args()
config_root = 'config'
config_path = os.path.join(config_root, '{}.yml'.format(args.version))
cfg = yaml.safe_load(open(config_path))
############################################################################################

#umap Args
if cfg['dim_red'] == 'umap':
	n_neighbors = cfg['nn']
	n_components = cfg['nc']
	metric = cfg['metric']
	random_state = cfg['random_seed']
	dim_red_args = {'n_neighbors': int(n_neighbors),
	             'n_components': int(n_components),
	             'metric': metric,
	             "random_state": int(random_state)
	             }

#PCA args
if cfg['dim_red'] == 'pca':
	if cfg['nc'].isalpha():
		n_components = cfg['nc']
	else:
		n_components = int(cfg['nc'])

	svd_solver = cfg['ss']
	dim_red_args = {'n_components': n_components,
	             'svd_solver': svd_solver
	             }
#HDBSCAN Args
if cfg['cluster'] == 'hdbscan':
	mcs = cfg['mcs']
	ms = cfg['ms']
	metric = cfg['metric']
	csm = cfg['csm']
	cluster_args = {'min_cluster_size': int(mcs),
	                'min_samples':int(ms),
	                'metric': metric,
	                'cluster_selection_method': csm
	             }

#K-Means Clustering
if cfg['cluster'] == 'kmeans':
	cluster_args = {'n_clusters': int(cfg['ncls']),
				   'init': cfg['init']
				}
#cleaned docs saved in txt file with each documents seperated by '\n'
if args.texts == 'upanishad':
	cleaned_doc_path = os.path.join(doc_root, 'upanishads_clean', args.file_name)
elif args.texts == 'gita':
	cleaned_doc_path = os.path.join(doc_root, 'gita_clean', args.file_name)
with open(cleaned_doc_path, r) as f:
	data = f.read()

documents = data.strip().split('\n')
if cfg['dim_red'] == 'umap' and cfg['cluster'] == 'hdbscan':
	model = TopicModel(documents= documents, speed='deep-learn', workers=8, min_count = 0, embedding_model='distiluse-base-multilingual-cased', umap_args = dim_red_args, hdbscan_args = cluster_args)

if cfg['dim_red'] == 'umap' and cfg['cluster'] == 'kmeans':
	model = TopicModel(documents= documents, speed='deep-learn', workers=8, min_count = 0, embedding_model='distiluse-base-multilingual-cased', umap_args = dim_red_args, kmeans_args = cluster_args)
























