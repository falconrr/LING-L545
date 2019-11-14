import sys

infile = sys.stdin.readline ()
while infile != '':
    if infile.strip() == '': # .strip removes all the spaces before and after the string
        infile = sys.stdin.readline ()
        continue
    line_break = infile.strip().replace('. ', '.\n').strip()
    if line_break != '':
        sys.stdout.write(line_break)
    infile = sys.stdin.readline ()

# print(line_break, end='')
