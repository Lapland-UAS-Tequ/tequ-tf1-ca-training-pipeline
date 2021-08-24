import json
import os
import sys
from object_detection.utils.label_map_util import get_label_map_dict

basepath = os.getcwd()
labels_path = sys.argv[1]

DATA_PATH       = basepath+'\\content\\data'
LABEL_MAP_PATH    = os.path.join(DATA_PATH, 'label_map.pbtxt')

label_map = get_label_map_dict(LABEL_MAP_PATH)
label_array = [k for k in sorted(label_map, key=label_map.get)]

with open(os.path.join(labels_path, 'labels.json'), 'w') as f:
  json.dump(label_array, f)
