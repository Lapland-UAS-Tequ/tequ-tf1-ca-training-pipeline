import os
import re
import sys

OUTPUT_PATH = sys.argv[1]
#OUTPUT_PATH     = basepath+'\\content\\output'
regex = re.compile(r"model\.ckpt-([0-9]+)\.index")
numbers = [int(regex.search(f).group(1)) for f in os.listdir(OUTPUT_PATH) if regex.search(f)]
TRAINED_CHECKPOINT_PREFIX = os.path.join(OUTPUT_PATH, 'model.ckpt-{}'.format(max(numbers)))
f = open("temp.txt", "w")
f.write(TRAINED_CHECKPOINT_PREFIX)
f.close()
