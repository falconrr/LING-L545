# this is the Assignment 00 for initial consonant sequences

$ sed 's/[^a-zA-Z]\+/\n/g' < wiki.txt > practice.txt
$ grep '^[bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ]' practice.txt > consonants.txt
$ sed 's/[aeiouAEIUO].*//' consonants.txt > test.txt
$ sort -d test.txt | uniq -c > output1.txt
$ sort -nr < output1.txt > output1-2.txt
$ head output1-2.txt
