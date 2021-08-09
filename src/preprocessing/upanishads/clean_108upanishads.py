# -*- coding: utf-8 -*-
"""
Created on Sat July 23 16:01:36 2021

@author: Mukul(https://github.com/mukul54)
"""
#Basic Python and Machine learning libraries
import os, sys, warnings, random, time, re, math, string, copy
from collections import defaultdict
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from utils.preprocess_utils import map_old_new, contraction_mapping
#read the file
fname = '../../../assets/upanishads_texts/108upanishads'

with open("{}.txt".format(fname), 'r', encoding='utf-8-sig') as f:
    data = f.read()
    f.close()


def get_upanishads_names(raw_data):
  '''
  get the names of all 108 upanishads from raw data
  Args:
    raw_data: unprocessed data
  Return:
    all_upanishads: list of all 108 upanishads
  '''
  raw_data = raw_data.replace('\x0c', '')#remove unicode
  raw_data = raw_data.replace('*', '')#
  data_split_newline = raw_data.split('\n')
  
  all_upanishads = []
  all_upanishads_ = [x for x in data_split_newline[16:128]]

  for i, name in enumerate(all_upanishads_):
    if len(name) > 0 and "Followed by" not in name:
      name = name.strip().split(' ')[1] 
      all_upanishads.append(name)

  return all_upanishads


def veda_to_upanishads(raw_data):
  '''
  get the names of all 108 upanishads from raw data
  Args:
    raw_data: unprocessed data
  Return:
    all_upanishads: dictioanry with vedas name as key and upanishads list as values
  '''
  raw_data = raw_data.replace('\x0c', '')#remove unicode
  raw_data = raw_data.replace('*', '')#remove asterics
  data_split_newline = raw_data.split('\n')
  
  veda_to_upanishads = defaultdict(list)

  
  all_upanishads_rig_ = [x for x in data_split_newline[33880:33891]]
  all_upanishads_syv_ = [x for x in data_split_newline[33893:33912]]
  all_upanishads_kyv_ = [x for x in data_split_newline[33914:33947]]
  all_upanishads_sam_ = [x for x in data_split_newline[33949:33965]]
  all_upanishads_ath_ = [x for x in data_split_newline[33967:33999]]


  #Rig Veda
  for i, name in enumerate(all_upanishads_rig_):
    if len(name) > 0:
      name = name.strip().split(' ')[1] 
      veda_to_upanishads["Rig-Veda"].append(name)
  #Sukla_yajur_veda

  for i, name in enumerate(all_upanishads_syv_):
    if len(name) > 0:
      name = name.strip().split(' ')[1] 
      veda_to_upanishads["Sukla-Yajur-Veda"].append(name)
  # Krishna-Yajur-Veda

  for i, name in enumerate(all_upanishads_kyv_):
    if len(name) > 0:
      name = name.strip().split(' ')[1] 
      veda_to_upanishads["Krishna-Yajur-Veda"].append(name)
  # Sama-Veda

  for i, name in enumerate(all_upanishads_sam_):
    if len(name) > 0:
      name = name.strip().split(' ')[1] 
      veda_to_upanishads["Sama-Veda"].append(name)

  # Atharva-Veda
  for i, name in enumerate(all_upanishads_ath_):
    if len(name) > 0:
      name = name.strip().split(' ')[1] 
      veda_to_upanishads["Atharva-Veda"].append(name)
  return veda_to_upanishads


def create_upanishads_dict(raw_data):
  '''
  Create a dictionary for each Upanished contained with texts 
  '''
  all_upanishads = get_upanishads_names(raw_data)
  # for upanishands_name in all_upanishads
  raw_data = data.replace('\x0c', '')
  all_match = re.findall(r"(Here ends the .*panishad.*Veda\.)", raw_data)
  #some text contains commentry by Swami Nirmalananda Giri

  commentary_list = re.findall(r"End of .*Commentary", raw_data)

  upan_dict = {}
  start_idx = raw_data.find("Isavasya Upanishad");

  for idx , match in enumerate(all_match):
    #upan = match.strip().split(" ")[3]
    upan = all_upanishads[idx]
    # print(upan, ":", match)
    if upan.endswith(","):
      upan = upan[:-1]#remove comma in the end
    
    end_idx = raw_data.find(all_match[idx])

    #first 10 upanishads contains commentary
    if idx < 10:
      end_idx = raw_data.find(commentary_list[idx])
      upan_dict[upan] = r"{}".format(raw_data[start_idx:end_idx+len(commentary_list[idx])])
      start_idx = end_idx+len(commentary_list[idx])+1
    else:
      upan_dict[upan] = r"{}".format(raw_data[start_idx:end_idx+len(match)])
      start_idx = end_idx+len(match)+1

  return upan_dict

def remove_beginning_lines(data):
  """
  Remove the beginning lines, like translated by, published by, and upanishads name
  """
  data_list = data.split('\n')
  
  data_list = [x for x in data_list if len(x)> 0]
  
  data_list = data_list[1:]#remove name of the upanishads
  
  if "Translated by" in data_list[0]:
    data_list = data_list[1:]
  if "Published by" in data_list[0]:
    data_list = data_list[1:]

  data = "\n".join(data_list)
  
  return data

def replace_words_contraction(data, map_old_new, contraction_map):
  """
  Replace old and archaic words
  """
  for new_old, word in zip(map_old_new.keys(), contraction_map.keys()):
    data = data.replace(new_old, map_old_new[new_old])
    data = data.replace(word, contraction_map[word])
  return data

def clean_text(data):
  '''
  clean the raw text of each of the 108 upanishads
  '''
  #remove unicode
  data = data.replace('\x0c', '')

  #removes beginning line eg. Upanishad's name, translated by and published by
  data = remove_beginning_lines(data)

  #remove sloka's numbering eg. 2-III-11.,I-3:,10.etc
  data = re.sub('(.*[-][\d]+[.:])|(^[\d]+[.])', '', data)

  #remove the numbering of upanishads eg. (Atharvashikha Upanishad 1:10)
  data = re.sub('[(](?<=\()(.*? Upanishad .*?)(?=\))[)]', '', data)

  #remove the numbering of upanishads eg. (2:10)
  data = re.sub('[(](?<=\()([0-9]+:[0-9]+)(?=\))[)]', '', data)

  #remove the numberings eg. II-ii-51-56., II-21.
  data = re.sub("(.*[-][\d]+[.:])|(^[\d]+[.])|(.*[-][\d]+([a-z()]{3})[.:])", '', data)

  #remove and replace different symbols and repetitive characters
  data = data.replace('…………………', '')
  data = data.replace('………..', '')
  data = data.replace('……', '')
  data = data.replace('....', '')
  data = data.replace('...', '')
  data = data.replace('..', '')

  #replace texts
  data = data.replace('Om!', 'Om ')
  data = data.replace('Om !', 'Om')
  data = data.replace('Om! Peace! Peace! Peace!', 'Om Peace Peace Peace!')

  #remove extra texts like commentary by ...
  data = re.sub('.*by Swami Nirmalananda Giri.', '', data)
  data = re.sub(r"End of .*Commentary", '', data)
  
  #eg. Isha Upanishad commentary
  data = re.sub(".*panishad Commentary", '', data)

  #remove archaic words like thy thou etc
  data = replace_words_contraction(data, map_old_new, contraction_mapping)

  # remove all other symbols numbers and white spaces
  data = "".join([character if (character.isalpha() or character == "." or character ==" " or character == "\n") else " " for character in data])
  
  # remove line break and break based on full stops to make documents
  data = data.replace("\n", " ")

  data_list = data.split(".")
  data_list = [x for x in data_list if (len(x.strip().split(" ")) > 3)]

  data = "\n".join(data_list)

  #remove extra spaces 
  data = re.sub(" +", " ", data)

  #lower case
  data = data.lower()

  return data

def get_cleaned_data_dict(data):
  """
  dict of Cleaned data
  """
  all_upanishads = get_upanishads_names(data)
  upan_dict = create_upanishads_dict(data)
  new_upan_dict = rename_keys_upanishad_dict(all_upanishads, upan_dict)

  cleaned_upanishads_dict = {}
  for upanishads_name in new_upan_dict.keys():
    cleaned_upanishads_dict[upanishads_name] = clean_text(new_upan_dict[upanishads_name])
  
  return cleaned_upanishads_dict

def save_cleaned_data_as_json(data):
  """
  Save as json
  """
  cleaned_upanishads = get_cleaned_data_dict(data)
  with open('all_upanishads_cleaned.json', 'w') as fp:
    json.dump(cleaned_upanishads_dict, fp, indent=4)

def join_upanishads(data, num):

  """
  join first num upanishads to form a larger corpse
  """
  cleaned_upanishads = get_cleaned_data_dict(data)
  top_num_upanishads = []
  for idx, name in enumerate(cleaned_upanishads.keys()):
    if idx < num:
      top_num_upanishads.append(cleaned_upanishads[name])
  
  top_num_upanishads_ = "\n".join(top_num_upanishads)
  return top_num_upanishads_

