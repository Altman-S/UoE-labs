import string
import math
import re
import numpy as np
import collections
import matplotlib.pyplot as plt
from stemming.porter2 import stem

# open txt file
# with open('bible.txt', 'r') as f:
with open('abstracts_wiki.txt', 'r') as f:
    f_str = f.read()

# delete punctuation
# re.sub(pattern, repl, string, count=0, flags=0)
r = "[0-9!#$%&'()*+,-./:;<=>?@[\]^_`{|}~\n]"
no_punct = re.sub(r, ' ', f_str)

# transform to lower_case
no_punct = no_punct.lower()

# string to words list
no_list = no_punct.split()

# put words in englishST into a list
with open('englishST.txt', 'r') as eng:
    eng_str = eng.read()
eng_list = eng_str.split()

# delete words in no_list
stop_list = []
for i in no_list:
    if (i not in eng_list):
        stop_list.extend([i])

# substitution
norm_list = []
for i in stop_list:
    norm_list.append(stem(i))

# write to file
# ATTENTION: change file name
output_file = open('pre_abstracts_wiki.txt', 'w')
for i in range(len(norm_list)):
    s = str(norm_list[i]) + ' '
    output_file.write(s)
output_file.close()
