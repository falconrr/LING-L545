import nltk
import sys
import re
idx = 1

infile = sys.stdin.readline()
while infile != '':
    infile = infile.strip()
    period = infile.replace('.', ' .')
    coma = period.replace(',', ' , ')
    par_in = coma.replace('(', ' ( ')
    par_out = par_in.replace(')', ' ) ')
    no_spaces = re.sub('  *', ' ', par_out)

    #tokenizer = no_spaces.replace(' ', '\n'). #(Without numbers, underscores and titles)
# Title
    if no_spaces.strip() == '':
        infile = sys.stdin.readline()
        continue
    print('# Sentence ID:', idx)
    idx +=1
    print('# Sentence =', no_spaces)
    text = nltk.word_tokenize(no_spaces)
    upos = nltk.pos_tag(text)

    # numbers and underscores
    sentence = no_spaces.split(' ')
    index = 1
    cnt = 0

    for i in sentence: # i = each item in that list
        #print(index, i, cnt, upos[cnt], file = sys.stderr)
        if i.strip() == '':
            continue
        print('%d\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s' % (index, i, '_', upos[cnt][1], '_', '_', '_', '_', '_', '_'))
        index +=1
        cnt += 1
    print()
    infile = sys.stdin.readline ()

"""
# no_spaces =
# import re
#x = '     ergerg     '
#re.sub('    *', '', x)
#'     ergerg     '
# post processing on Unix if we dont want blank lines and orthographical characers=== tr -sc 'a-zA-Z' '\n' < hmw01b.txt > hmw1.txt
sentence = tokenizer.split
enumerate(tokenizer.split)
"""
