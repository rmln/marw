"""

The purpose of this script is to create a Serbian version of Goran Igaly's
Dictionary of Croatian Languages.

This is achieved by the following:

1. Load Croatian dictionary.
2. Iterate over each element in the first column.
3. Check if the item is valid Serbian entry (can be
   converted to Cyrillic-only form).
4. If the item is valid, convert the second item in
   the entry ('base' of the word). Also, convert
   POS identifier to an English version (via labels.POS_CRO).
"""

import os
import sys

sys.path.append("../")

import conf
import helpers
from text import makewords
from labels import POS_CRO

# Cunter por POS (now many nouns, verbs etc.)
dpos = {}

def populate_serbian():
    """
    Create SR dictionary based on HR.
    """
    parsed = []
    serbian = []
    print("Loading dictionaries...")
    dic_croatian = open(conf.PATH_CROD).readlines()
    dic_serbian_full =  [w.strip() for w in open(conf.HUNSPELL_PATH).readlines()]
    # Converting it to set makes 'in' operation
    # much, much faster.
    dic_serbian = set(dic_serbian_full)
    print("BASIC INFO")
    print("Items in Croatian dictionary:\t%s" % len(dic_croatian))
    print("Items Serbian dictionary:\t%s" % len(dic_serbian_full))
    print("Uniques in Serbian dictionary:\t%s" % len(dic_serbian))
    print("PATHS")
    print("Serbian version will be saved to %s" % conf.PATH_SERBIAN)
    print("Parsed version will be saved to %s" % conf.PATH_TMPPARSE)
    f_parse = open(conf.PATH_TMPPARSE, 'w')
    f_serbian = open(conf.PATH_SERBIAN, 'w')
    print("Parsing started...")
    # Just counters
    perc_ten = int(len(dic_croatian) / 10)
    counter = 0
    perc = 1
    for line in dic_croatian:
        if counter == 0:
            print("Done 0%...")
        if counter > perc_ten*perc:
            print("Done %s0%% (~%s items)..." % (perc, counter))
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
    print("Done parsing. Stats follow.")
    print("")
    print("POS DISTRIBUTION:")
    for i in dpos:
        print('%s\t%s' % (i, dpos[i]))
    print("")
    print("COUNT & PERCENTAGES")
    print("Items in newly created Serbian dictionary: %s" % len(serbian))
    print("Serbian dictionary contains %s%% of Croatian dictionary." \
              % helpers.perc(len(serbian), len(dic_croatian)))
    print("Serbian dictionary contains %s%% of original hunspell dictionary." \
              % helpers.perc(len(serbian), len(dic_serbian_full)))
    print("And for the record, hunspell-sr contains %s%% of original items." \
              % helpers.perc(len(dic_serbian), len(dic_serbian_full)))
        

def croline_to_serbian(head_cyr_from_cro, line):
    """
    Convert a line from Croatian dictionary to
    Serbian version of the same line.

    Example:
    
    IN
    head:  летење
    line:  ('letenje', 'letenje', '53', 'imenica')

    OUT
    летење летење 53 n
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

