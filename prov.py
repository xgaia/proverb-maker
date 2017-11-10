# -*- coding: utf-8 -*-
import random
import locale
import os
import re, json, sys
from urllib2 import Request, urlopen, URLError
from bs4 import BeautifulSoup

import polyglot
from polyglot.text import Text, Word

adress_dict={"fr":"https://fr.wiktionary.org/w/api.php?titles=Annexe:Liste_de_proverbes_fran%C3%A7ais"
,"en":"https://en.wiktionary.org/w/api.php?titles=Appendix:English_proverbs"}

def get_list(lang="fr"):
    if not lang == "fr" and not lang == "en":
        print "Only support fr & en languages"
        sys.exit(1)
    request = Request(adress_dict[lang]+"&action=query&prop=extracts&format=json")
    response = urlopen(request)
    body = json.loads(response.read())["query"]["pages"]
    for key in body.keys():
    	return body[key]["extract"]

def parse_list(lang="fr"):
    if not lang == "fr" and not lang == "en":
        print "Only support fr & en languages"
        sys.exit(1)
    html_string = get_list(lang)
    parsed_html = BeautifulSoup(html_string,"lxml")
    proverb_list = []
    if lang == "fr":
        references = parsed_html.find("h3")
        for elm in references.find_next_siblings():
            elm.extract()
        references.extract()
        for pro in parsed_html.find_all('li'):
            proverb_list.append(pro.get_text().rstrip("."))
    elif lang == "en":
        for pro in parsed_html.find_all('dd'):
            proverb_list.append(pro.get_text().rstrip("."))
    return proverb_list

def build_proverbs_file(lang):
    """Build a file with proverbs and cut them with a @"""

    # Get uncut proverbs file
    uncut_provs = parse_list(lang)

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
