#!/usr/bin/env python3
"""
    William Bowers
    Natural Language Toolkit Cleaning and Counting Stems
    03/11/2019
"""

import sys
import re
import nltk
from nltk.stem.porter import *


file_name = sys.argv[1] 
output_file_name = sys.argv[2]

# Read file
with open(file_name, 'r') as new_file:
    with open(output_file_name, 'w') as updated_file:
        text = new_file.read().lower()

# Clean based definiton of a word
        text = re.sub(r'<[^>]+>|[^\w\s\']|_|\'{2,3}', r' ', text)
        text = re.sub(r'\b\w*(?:\d+\w*?\d*)\b', r'', text)
        text = re.sub(r'\s+', r' ', text)

# write updated file
        new_file.close()
        updated_file.write(text)
        updated_file.close()

# Tokenize text
tokens = nltk.word_tokenize(text)
print(tokens)
# Stem words
stems = [PorterStemmer().stem(word) for word in tokens]

def stem_counter():
    stem_count = dict() 

    for stem in stems:
        if stem in stem_count:
            stem_count[stem] += 1
        else:
            stem_count[stem] = 1

    # Sort Stem Dictionary first alphabetically then by stem count
    sortedDict = sorted(stem_count, key=lambda x: x)
    sortedDict_2 = sorted(sortedDict, key=lambda x: stem_count[x], reverse=True)

    with open(output_file_name, 'w') as output_file:
        for stem in sortedDict_2:
            output_file.write(stem + '    ' + str(stem_count[stem]) + '\n') 
        output_file.close()

stem_counter()