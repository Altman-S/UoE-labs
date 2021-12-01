import re
import json
import collections
import xml.dom.minidom
from stemming.porter2 import stem

# Term -> (Document -> Position)
file = open('index_ts.txt', 'r')
js = file.read()
term_doc_pos_dict = json.loads(js)
file.close()

# Term -> Position
file = open('index_ts_pos.txt', 'r')
js = file.read()
term_position_dict = json.loads(js)
file.close()

# input from term_position_dict
# {'Term1': [[doc1, pos1], [doc2, pos2], [doc3, pos3]
#  'Term2': [[doc1, pos1], [doc2, pos2], [doc3, pos3]}
# output to output_index.txt

# input term_doc_pos_dict
# {'Term1': {doc1: [position1, position2], doc2: [position1, position2]}
#  'Term2': {doc1: [position1, position2, position3], doc2: [position1, position2]}}

doc = open('output_index.txt', 'w')
for key, value in term_position_dict.items():
    print(key + ":" + str(len(term_doc_pos_dict[key])), file=doc)
    print("\t" + str(value[0][0]) + ": " + str(value[0][1]), end="", file=doc)  # do not wrap
    for i in range(len(value) - 1):
        if (value[i + 1][0] == value[i][0]):
            print(", " + str(value[i + 1][1]), end="", file=doc)
        else:
            print("", file=doc)
            print("\t" + str(value[i + 1][0]) + ": " + str(value[i + 1][1]), end="", file=doc)

    print("", file=doc)
doc.close()