# This is the Segmenter.py for Practical 01b
import sys

infile = sys.stdin.readline ()
while infile != '':
    if infile.strip() == '':
        infile = sys.stdin.readline ()
        continue
    line_break = infile.strip().replace('. ', '.\n').strip()
    if line_brak != '':
        sys.stdout.write(line_break)
    infile = sys.stdin.readline ()
  
# This is the Tokenizer.py for Practical 01b
import sys
import re
idx = 1

infile = sys.stdin.readline ()
while infile != '':
    period = infile.replace('.', ' .')
    coma = period.replace(',', ' , ')
    par_in = coma.replace('(', ' ( ')
    par_out = par_in.replace(')', ' ) ')
    no_spaces = re.sub('  *', ' ', par_out)
    print('Sentence ID:', idx)
    idx +=1
    print('Sentence =', no_spaces)
    sentence = no_spaces.split(' ')
    index = 1
    for i in sentence: # i = each item in that list
        print(index, i, '_', '_', '_', '_', '_', '_', '_', '_')
	index +=1
    infile = sys.stdin.readline ()

    
