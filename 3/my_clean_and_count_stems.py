#!/usr/bin/env python3
"""
    William Bowers
    (working alongside Paulina Valdivieso)
    Cleaning and Counting Stems using own stemmer based on https://tartarus.org/martin/PorterStemmer/def.txt
    03/11/2019
"""
import sys
import re

file_name = sys.argv[1] 
output_file_name = sys.argv[2]

# Read file
with open(file_name, 'r') as new_file:
    with open(output_file_name, 'w') as updated_file:
        text = new_file.read().lower()

# Clean based definiton of a word
        text = re.sub(r'<[^>]+>|[^\w\s\'\.]|_|\'{2,3}|\b\w*(?:\d+\w*.\d*)\b', r' ', text)
        text = re.sub(r'\s+', r' ', text)

# write updated file
        new_file.close()
        updated_file.write(text)
        updated_file.close()

# reopen to define delimiter 
with open(output_file_name, 'r') as updated_file:
    lines = updated_file.read()
    updated_file.close()
    words = lines.split(' ')

def step_1(words):
    #SSES -> SS  
    if re.search(r'sses$', str(words), re.M):
        words = re.sub(r'sses',r'ss', words, re.M)

    #IES  -> I 
    if re.search(r'ies$', str(words), re.M):
        words = re.sub(r'ies',r'i', words, re.M)    
    
    #SS   -> SS  
    if re.search(r'ss$', str(words), re.M):
        words = re.sub(r'ss',r'ss', words, re.M)

    #S    -> 
    if re.search(r's$', str(words), re.M):
        words = re.sub(r's',r'', words, re.M)

    #EED -> EE 
    if re.search(r'^[^aeiou\W]*([aeiou]+[^aeiou\W]+)+[aeiou]*eed$', str(words), re.M):
        words = re.sub(r'eed',r'ee', words, re.M)

    #ED  -> 
    if re.search(r'\w*[aeiou]+\w+ed$', str(words), re.M):
        words = re.sub(r'ed',r'', words, re.M)
        step_1b(words)

    #ING  -> 
    if re.search(r'\w*[aeiou]+\w+ing$', str(words), re.M):
        words = re.sub(r'ing',r'', words, re.M)
        step_1b(words)

    #Y  ->  I 
    if re.search(r'\w*[aeiou]+\w+y$', str(words), re.M):
        words = re.sub(r'y',r'i', words, re.M)
    
    return words     

def step_1b(words):
    #AT -> ATE
    if re.search(r'at$', str(words), re.M):
        words = re.sub(r'at',r'ate', words, re.M)

    #BL -> BLE 
    if re.search(r'bl$', str(words), re.M):
        words = re.sub(r'bl',r'ble', words, re.M)

    #IZ -> IZE  
    if re.search(r'iz$', str(words), re.M):
        words = re.sub(r'iz',r'ize', words, re.M)

    #Double letter and not l,s, or z -> single letter 
    if re.search(r'([^aeioulsz])\1$', str(words), re.M):
        words = re.sub(r'([^aeioulsz])\1',r'\w$', words, re.M)

    #(m=1 and *o) -> E    the stem ends cvc, where the second c is not W, X or Y
    if re.search(r'^[^aeiou\W]+([aeiou][^aeiouwxy\W]){1}$', str(words), re.M):
        words = re.sub(r'\w$',r'e$', words, re.M)
    print(words)
    return words 

def step_2(words):
    #ATIONAL ->  ATE 
    if re.search(r'[^aeiou\W]*([aeiou]+[^aeiou\W]+)+[aeiou]*ational', str(words), re.M):
        words = re.sub(r'ational',r'ate', str(words), re.M)
    
    #TIONAL  ->  TION   
    if re.search(r'[^aeiou\W]*([aeiou]+[^aeiou\W]+)+[aeiou]*[^a]tional', str(words), re.M):
        words = re.sub(r'tional',r'tion', str(words), re.M)
        
    #ENCI    ->  ENCE
    if re.search(r'[^aeiou\W]*([aeiou]+[^aeiou\W]+)+[aeiou]*enci', str(words), re.M):
        words = re.sub(r'enci',r'ence', str(words), re.M)    

    #ANCI    ->  ANCE 
    if re.search(r'[^aeiou\W]*([aeiou]+[^aeiou\W]+)+[aeiou]*anci', str(words), re.M):
        words = re.sub(r'anci',r'ance', str(words), re.M) 

    #IZER    ->  IZE
    if re.search(r'[^aeiou\W]*([aeiou]+[^aeiou\W]+)+[aeiou]*izer', str(words), re.M):
        words = re.sub(r'izer',r'ize', str(words), re.M) 

    #ABLI    ->  ABLE  
    if re.search(r'[^aeiou\W]*([aeiou]+[^aeiou\W]+)+[aeiou]*abli', str(words), re.M):
        words = re.sub(r'abli',r'able', str(words), re.M) 

    #ALLI    ->  AL 
    if re.search(r'[^aeiou\W]*([aeiou]+[^aeiou\W]+)+[aeiou]*alli', str(words), re.M):
        words = re.sub(r'alli',r'al', str(words), re.M) 
   
    #ENTLI   ->  ENT
    if re.search(r'[^aeiou\W]*([aeiou]+[^aeiou\W]+)+[aeiou]*entli', str(words), re.M):
        words = re.sub(r'entli',r'ent', str(words), re.M) 

    #ELI     ->  E 
    if re.search(r'[^aeiou\W]*([aeiou]+[^aeiou\W]+)+[aeiou]*eli', str(words), re.M):
        words = re.sub(r'eli',r'e', str(words), re.M)

    #OUSLI   ->  OUS  
    if re.search(r'[^aeiou\W]*([aeiou]+[^aeiou\W]+)+[aeiou]*ousli$', str(words), re.M):
        words = re.sub(r'ousli',r'ous', str(words), re.M)

    #IZATION ->  IZE 
    if re.search(r'[^aeiou\W]*([aeiou]+[^aeiou\W]+)+[aeiou]*ization$', str(words), re.M):
        words = re.sub(r'ization',r'ize', str(words), re.M)

    #ATION   ->  ATE 
    if re.search(r'[^aeiou\W]*([aeiou]+[^aeiou\W]+)+[aeiou]*[^iz]ation$', str(words), re.M):
        words = re.sub(r'ation',r'ate', str(words), re.M)

    #ATOR    ->  ATE
    if re.search(r'[^aeiou\W]*([aeiou]+[^aeiou\W]+)+[aeiou]*ator$', str(words), re.M):
        words = re.sub(r'ator',r'ate', str(words), re.M)   

    #ALISM   ->  AL 
    if re.search(r'[^aeiou\W]*([aeiou]+[^aeiou\W]+)+[aeiou]*alism$', str(words), re.M):
        words = re.sub(r'alism',r'al', str(words), re.M)  

    #IVENESS ->  IVE
    if re.search(r'[^aeiou\W]*([aeiou]+[^aeiou\W]+)+[aeiou]*iveness$', str(words), re.M):
        words = re.sub(r'iveness',r'ive', str(words), re.M)    

    #FULNESS ->  FUL 
    if re.search(r'[^aeiou\W]*([aeiou]+[^aeiou\W]+)+[aeiou]*fulness$', str(words), re.M):
        words = re.sub(r'fulness',r'ful', str(words), re.M)  

    #OUSNESS ->  OUS
    if re.search(r'[^aeiou\W]*([aeiou]+[^aeiou\W]+)+[aeiou]*ousness$', str(words), re.M):
        words = re.sub(r'ousness',r'ous', str(words), re.M) 

    #ALITI   ->  AL
    if re.search(r'[^aeiou\W]*([aeiou]+[^aeiou\W]+)+[aeiou]*aliti$', str(words), re.M):
        words = re.sub(r'aliti',r'al', str(words), re.M) 

    #IVITI   ->  IVE   
    if re.search(r'[^aeiou\W]*([aeiou]+[^aeiou\W]+)+[aeiou]*iviti$', str(words), re.M):
        words = re.sub(r'iviti',r'ive', str(words), re.M) 

    #BILITI  ->  BLE   
    if re.search(r'[^aeiou\W]*([aeiou]+[^aeiou\W]+)+[aeiou]*biliti$', str(words), re.M):
        words = re.sub(r'biliti',r'ble', str(words), re.M)
    
    return words 

def step_3(words):
    #ICATE ->  IC  
    if re.search(r'[^aeiou\W]*([aeiou]+[^aeiou\W]+)+[aeiou]*icate$', str(words), re.M):
        words = re.sub(r'icate',r'ic', str(words), re.M)
                
    #ATIVE ->  
    if re.search(r'[^aeiou\W]*([aeiou]+[^aeiou\W]+)+[aeiou]*ative$', str(words), re.M):
        words = re.sub(r'ative',r'', str(words), re.M) 

    #ALIZE ->  AL
    if re.search(r'[^aeiou\W]*([aeiou]+[^aeiou\W]+)+[aeiou]*alize$', str(words), re.M):
        words = re.sub(r'alize',r'al', str(words), re.M) 
                  
    #ICITI ->  IC     
    if re.search(r'[^aeiou\W]*([aeiou]+[^aeiou\W]+)+[aeiou]*iciti$', str(words), re.M):
        words = re.sub(r'iciti',r'ic', str(words), re.M) 

    #ICAL  ->  IC     
    if re.search(r'[^aeiou\W]*([aeiou]+[^aeiou\W]+)+[aeiou]*ical$', str(words), re.M):
        words = re.sub(r'ical',r'ic', str(words), re.M) 
             
    #FUL   ->   
    if re.search(r'[^aeiou\W]*([aeiou]+[^aeiou\W]+)+[aeiou]*ful$', str(words), re.M):
        words = re.sub(r'ful',r'', str(words), re.M) 
                    
    #NESS  ->    
    if re.search(r'[^aeiou\W]*([aeiou]+[^aeiou\W]+)+[aeiou]*ness$', str(words), re.M):
        words = re.sub(r'ness',r'', str(words), re.M) 
    
    return words     

def step_4(words):
    #AL    -> 
    if re.search(r'[^aeiou\W]*([aeiou]+[^aeiou\W]+){2,}[aeiou]*al$', str(words), re.M):
        words = re.sub(r'al',r'', str(words), re.M) 

    #ANCE  -> 
    if re.search(r'[^aeiou\W]*([aeiou]+[^aeiou\W]+){2,}[aeiou]*ance$', str(words), re.M):
        words = re.sub(r'ance',r'', str(words), re.M) 

    #ENCE  ->
    if re.search(r'[^aeiou\W]*([aeiou]+[^aeiou\W]+){2,}[aeiou]*ence$', str(words), re.M):
        words = re.sub(r'ence',r'', str(words), re.M) 

    #ER    ->
    if re.search(r'[^aeiou\W]*([aeiou]+[^aeiou\W]+){2,}[aeiou]*er$', str(words), re.M):
        words = re.sub(r'er',r'', str(words), re.M) 

    #IC    ->
    if re.search(r'[^aeiou\W]*([aeiou]+[^aeiou\W]+){2,}[aeiou]*ic$', str(words), re.M):
        words = re.sub(r'ic',r'', str(words), re.M) 

    #ABLE  ->
    if re.search(r'[^aeiou\W]*([aeiou]+[^aeiou\W]+){2,}[aeiou]*able$', str(words), re.M):
        words = re.sub(r'able',r'', str(words), re.M) 

    #IBLE  ->
    if re.search(r'[^aeiou\W]*([aeiou]+[^aeiou\W]+){2,}[aeiou]*ible$', str(words), re.M):
        words = re.sub(r'ible',r'', str(words), re.M) 

    #ANT   -> 
    if re.search(r'[^aeiou\W]*([aeiou]+[^aeiou\W]+){2,}[aeiou]*ant$', str(words), re.M):
        words = re.sub(r'ant',r'', str(words), re.M) 

    #EMENT -> 
    if re.search(r'[^aeiou\W]*([aeiou]+[^aeiou\W]+){2,}[aeiou]*ement$', str(words), re.M):
        words = re.sub(r'ement',r'', str(words), re.M) 

    #MENT  -> 
    if re.search(r'[^aeiou\W]*([aeiou]+[^aeiou\W]+){2,}[aeiou]*[^e]ment$', str(words), re.M):
        words = re.sub(r'ment',r'', str(words), re.M) 

    #ENT   ->  
    if re.search(r'[^aeiou\W]*([aeiou]+[^aeiou\W]+){2,}[aeiou]*[^m]ent$', str(words), re.M):
        words = re.sub(r'ent',r'', str(words), re.M) 

    #ION   -> 
    if re.search(r'^[^aeiou\W]*([aeiou]+[^aeiou\W]+){2,}[aeiou]*(tion|sion)$', str(words), re.M):
        words = re.sub(r'ion',r'', str(words), re.M) 

    #OU    ->        
    if re.search(r'[^aeiou\W]*([aeiou]+[^aeiou\W]+){2,}[aeiou]*ou$', str(words), re.M):
        words = re.sub(r'ou',r'', str(words), re.M) 

    #ISM   ->  
    if re.search(r'[^aeiou\W]*([aeiou]+[^aeiou\W]+){2,}[aeiou]*ism$', str(words), re.M):
        words = re.sub(r'ism',r'', str(words), re.M) 

    #ATE   ->  
    if re.search(r'[^aeiou\W]*([aeiou]+[^aeiou\W]+){2,}[aeiou]*ate$', str(words), re.M):
        words = re.sub(r'ate',r'', str(words), re.M) 

    #ITI   ->   
    if re.search(r'[^aeiou\W]*([aeiou]+[^aeiou\W]+){2,}[aeiou]*iti$', str(words), re.M):
        words = re.sub(r'iti',r'', str(words), re.M) 

    #OUS   -> 
    if re.search(r'[^aeiou\W]*([aeiou]+[^aeiou\W]+){2,}[aeiou]*ous$', str(words), re.M):
        words = re.sub(r'ous',r'', str(words), re.M) 
                    
    #IVE   ->  
    if re.search(r'[^aeiou\W]*([aeiou]+[^aeiou\W]+){2,}[aeiou]*ive$', str(words), re.M):
        words = re.sub(r'ive',r'', str(words), re.M) 

    #IZE   ->                   
    if re.search(r'[^aeiou\W]*([aeiou]+[^aeiou\W]+){2,}[aeiou]*ize$', str(words), re.M):
        words = re.sub(r'ize',r'', str(words), re.M) 

    return words 

def step_5(words):
    #E     ->
    if re.search(r'^[^aeiou\W]*([aeiou]+[^aeiou\W]+){2,}[aeiou]*e$', str(words), re.M):
        words = re.sub(r'e$',r'', str(words), re.M) 

    #E     ->  
    if re.search(r'^[^aeiou\W]*([aeiou]+[^aeiou\W]+){1}e$', str(words), re.M):
        words = re.sub(r'e$',r'', str(words), re.M)

    #LL -> single letter   
    if re.search(r'^[^aeiou\W]*([aeiou]+[^aeiou\W]+){2,}[aeiou]*l$', str(words), re.M):
        words = re.sub(r'([^aeiou])\1',r'l$', words, re.M) 

    return words 

def stemmer(words):
    words = step_1(words)
    words = step_2(words)
    words = step_3(words)
    words = step_4(words)
    words = step_5(words)
    return words  


# New list of stems
stems = []
for i in words:
    i = stemmer(i) 
    stems.append(i)


def stem_counter(stems):
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


stem_counter(stems)