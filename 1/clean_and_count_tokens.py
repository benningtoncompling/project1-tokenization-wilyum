#!/usr/bin/env python3
"""
    William Bowers
    Cleaning and counting words in a file
    03/11/2019
"""

import sys
import re

file_name = sys.argv[1] #input('Enter name of text file: ')
output_file_name = sys.argv[2] #input('Enter name of output file: ')

# Read and write file
with open(file_name, 'r') as new_file:
    with open(output_file_name, 'w') as updated_file:
        text = new_file.read().lower()

# Regex operation to clean text
# Get rid of tags
        text = re.sub(r'<[^>]+>|[^\w\s\']|_|\'{2,3}', r' ', text) # <[^<.+>]+>|<.+> also works but the unnecessary '.' in the brackets forces the or statement
# Get rid of unwanted characters       
        text = re.sub(r'\b\w*(?:\d+\w*?\d*)\b', r'', text) # strings with numbers. Butwhat about words like "2nd"
        text = re.sub(r'\s+', r' ', text) # condensing spaces
# write updated file
        new_file.close()
        updated_file.write(text)
        updated_file.close()

#Word counter

def word_counter():
    word_count = dict()
    with open(output_file_name, 'r') as updated_file:
        lines = updated_file.read()
        updated_file.close()

        

    words = lines.split(' ') # space is dilimeter 
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    
    #sort by alphabet the sort by number, automatic, sort by keys first

    sortedDict = sorted(word_count, key=lambda x: x)
    sortedDict_2 = sorted(sortedDict, key=lambda x: word_count[x], reverse=True)

    with open(output_file_name, 'w') as output_file:
        for word in sortedDict_2:
            output_file.write(word + ':    ' + str(word_count[word]) + '\n') 
        output_file.close()

word_counter()

#internal dot 

       

        




