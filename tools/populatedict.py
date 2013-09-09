"""

The purpose of this script is to populate (expand) Goran Igaly's Dictionary
of Croatian Languages with Serbian equivalents.

This is to be achieved by the following:

1. Load Croatian dictionary.
2. Iterate of each element in the first column, convert to
   Cyrillic and see if the same word exist in hunspell-sr.
   If yes, add the word into new column.

"""

import os
import sys

sys.path.append("../")

import conf
import helpers
from text import makewords
from labels import POS_CRO

dpos = {}

def populate_serbian():
    """
    Populate HR dictionary with Serbian equivalents.
    """
    parsed = []
    serbian = []
    print("Loading dictionaries...")
    dic_croatian = open(conf.PATH_CROD).readlines()
    dic_serbian =  [w.strip() for w in open(conf.HUNSPELL_PATH).readlines()]
    # Converting it to set makes 'in' operation
    # much, much faster.
    dic_serbian = set(dic_serbian)
    print("Lines in Croatian dictionary:\t%s" % len(dic_croatian))
    print("Unique lines in Serbian dictionary:\t%s" % len(dic_serbian))
    f_parse = open(conf.PATH_TMPPARSE, 'w')
    f_serbian = open(conf.PATH_SERBIAN, 'w')
    print("Started parsing...")
    perc_ten = int(len(dic_croatian) / 10)
    counter = 0
    perc = 1
    for line in dic_croatian:
        if counter == 0:
            print("0% done...")
        if counter > perc_ten*perc:
            print("%s0%% done..." % perc)
            perc = perc + 1
        cro_line_split = croline_rebuild(line)
        head_cyr_from_cro = helpers.cyrrilic_check_convert(cro_line_split[0])
        if head_cyr_from_cro != False:
            # Now, check if this word is found in hunspell:
            if head_cyr_from_cro in dic_serbian:
                # Save it to new dictionary
                srline = croline_to_serbian(head_cyr_from_cro, cro_line_split)
                serbian.append('\t'.join(srline))
        counter = counter + 1
    f_serbian.write('\n'.join(serbian))
    f_serbian.write('\n')
    print("Done parsing.")
    print("POS distribution:")
    for i in dpos:
        print('%s\t%s' % (i, dpos[i]))
        

def croline_to_serbian(head_cyr_from_cro, line):
    """
    Convert a line from Croatian dictionary to
    Serbian version of the same line.
    """
    head = head_cyr_from_cro
    form = str(helpers.cyrrilic_check_convert(line[1]))
    codes = line[2]
    pos = POS_CRO[line[3].strip()]
    try:
        dpos[pos] += 1
    except KeyError:
        dpos[pos] = 0
    return (head, form, codes, pos)
             

def croline_rebuild(line):
    """
    Change the data format in Croatian dictionary.
    In:
    čobančicu/tčobančica/t32 25/timenica
    
    Out:
    čobančicu/tčobančica/tnoun/32,25
    """
    items = line.split('\t')
    form = items[0].strip()
    head = items[1].strip() if len(items) > 1 else ''
    pos = items[2].strip() if len(items) > 2 else ''
    markers = ','.join(items[3].strip().split(" ")) if len(items) > 3 else ''
    return (form, head, pos, markers)
    
populate_serbian()

