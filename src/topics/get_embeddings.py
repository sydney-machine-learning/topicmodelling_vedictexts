import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from top2vec import Top2Vec
import umap
import hdbscan

def get_embeddings_df_2d(model, num_reduced_topics = 10, sigma = None, random_state = 42 ):
    """
    2d plot the documents embedding
    """
    umap_args = {
      "n_neighbors": 15,
      "n_components": 2, # 5 -> 2 for plotting 
      "metric": "cosine",
      "random_state":random_state
      }
    if not sigma:
    	sigma = [3,3] #default value
    umap_data = umap.UMAP(**umap_args).fit_transform(model._get_document_vectors(norm=False))

    #get dataframe of the result 
    result = pd.DataFrame(umap_data, columns=['x_embeddings', 'y_embeddings'])
    result['Labels'] = np.array( ['Topic-'+ str(x+1) if x != -1 else 'outliers' for x in list(model.doc_top) ] )

    #### Hierarchical Topic Reduction ##########################
    new_label = []
    if model.get_num_topics() > num_reduced_topics:
      reduced_topic_lists = model.hierarchical_topic_reduction(num_topics = num_reduced_topics)
      ######################################

      ###get new labels
      for top_doc in model.doc_top:
        for idx, reduced_list in enumerate(reduced_topic_lists):
          if top_doc in reduced_list:
            new_label.append("Topic-"+str(idx+1))
            break
      ##################################
      result["Labels"] = np.array(new_label)
    else:
      result["Labels"] = result['Labels']

    #remove outliers
    result = result[np.abs(result.x_embeddings-result.x_embeddings.mean()) <= (sigma[0]*result.x_embeddings.std())]
    result = result[np.abs(result.y_embeddings-result.y_embeddings.mean()) <= (sigma[1]*result.y_embeddings.std())]
    return result

def get_embeddings_df_3d(model, num_reduced_topics = 10, sigma = None, random_state = 42):
	"""
 	2d plot the documents embedding
 	"""
 	umap_args = {
 	  "n_neighbors": 15,
 	  "n_components": 3, # 5 -> 2 for plotting 
 	  "metric": "cosine",
 	  "random_state":random_state
 	  }
 	
 	if not sigma:
 		sigma = [3, 3, 3]

 	umap_data = umap.UMAP(**umap_args).fit_transform(model._get_document_vectors(norm=False))
	result = pd.DataFrame(umap_data, columns=['x_embeddings', 'y_embeddings', 'z_embeddings'])
	result['Labels'] = model.doc_top
	#get dataframe of the result 
	result['Labels'] = np.array( ['Topic-'+ str(x+1) if x != -1 else 'outliers' for x in list(model.doc_top) ] )
	#### Hierarchical Topic Reduction ##########################
	new_label = []
	if model.get_num_topics() > num_reduced_topics:
	  reduced_topic_lists = model.hierarchical_topic_reduction(num_topics = num_reduced_topics)
	  ######################################
	  ###get new labels
	  for top_doc in model.doc_top:
	    for idx, reduced_list in enumerate(reduced_topic_lists):
	      if top_doc in reduced_list:
	        new_label.append("Topic-"+str(idx+1))
	        break
	  ##################################
	  result["Labels"] = np.array(new_label)
	else:
	  result["Labels"] = result['Labels']

 	#remove outliers
	result = result[np.abs(result.x_embeddings-result.x_embeddings.mean()) <= (sigma[0]*result.x_embeddings.std())]
	result = result[np.abs(result.y_embeddings-result.y_embeddings.mean()) <= (sigma[1]*result.y_embeddings.std())]
	result = result[np.abs(result.z_embeddings-result.z_embeddings.mean()) <= (sigma[2]*result.z_embeddings.std())]
	return result