# -*- coding: utf-8 -*-
import random
import locale
import os

import polyglot
from polyglot.text import Text, Word


def build_proverbs_file(lang):
    """Build a file with proverbs and cut them with a @"""

    # Get uncut proverbs file
    #TODO: parse wikipedia page to get uncut proverbs
    file_path = 'prov_%s_uncut.txt' % lang
    file = open(file_path)
    uncut_provs = file.readlines()

    # Open results file (delete if exist)
    resfile_path = 'prov_%s.txt' % lang
    resfile = open(resfile_path, 'w')
    
    for prov in uncut_provs:
        text = Text(prov, hint_language_code=lang)
        tags = text.pos_tags

        #  list: word and tag
        tag_list = []
        word_list = []
        for tag in tags:
            tag_list.append(tag[1])
            word_list.append(tag[0])

        # If PUNCT on the tag_list, cut here
        if 'PUNCT' in tag_list:
            # Get the position of the PUNCT
            position = tag_list.index('PUNCT')
            if position == 0:
                continue
            # Add a '@' after the position
            word_list.insert(position+1, '@')

            # print(' '.join(word_list))
            resfile.write(' '.join(word_list) + '\n')
            continue

        # If ADP on the tag_list, cut here
        if 'ADP' in tag_list:
            # Get the position of the ADP
            position = tag_list.index('ADP')
            if position == 0:
                continue
            # Add a '@' before the position
            word_list.insert(position, '@')

            # print(' '.join(word_list))
            resfile.write(' '.join(word_list) + '\n')
            continue

        # If VERB on the tag_list, cut here
        if 'VERB' in tag_list:
            # Get the position of the VERB
            position = tag_list.index('VERB')
            if position == 0:
                continue
            # Add a '@' before the position
            word_list.insert(position, '@')

            # print(' '.join(word_list))
            resfile.write(' '.join(word_list) + '\n')
            continue

        # If ADV on the tag_list, cut here
        if 'ADV' in tag_list:
            # Get the position of the ADV
            position = tag_list.index('ADV')
            if position == 0:
                continue
            # Add a '@' before the position
            word_list.insert(position, '@')

            # print(' '.join(word_list))
            resfile.write(' '.join(word_list) + '\n')
            continue

def main():
    # get system language
    lang = locale.getdefaultlocale()[0].split('_')[0]
    #lang = 'en' # uncoment this to force language

    file_path = 'prov_%s.txt' % lang

    # Make the prov file if not exist
    if not os.path.isfile(file_path):
        build_proverbs_file(lang) 

    # Get proverbs
    file = open(file_path)
    prov = file.readlines()

    # random choose 2
    prov1 = random.choice(prov)
    prov2 = random.choice(prov)
    # Split them
    begin = prov1.split('@')[0].strip()
    end = prov2.split('@')[1].strip()

    # Print the new one
    print('%s %s' % (begin, end))

if __name__ == '__main__':
    main()
