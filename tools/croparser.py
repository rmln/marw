"""
A code to convert "Rječnik hrvatskih jezika" into other formats.

"A Dictionary of Croatian Languages" (http://www.igaly.org/rjecnik-hrvatskih-jezika)
consists of a tab delimited text file. This code does two things with the file:


1. Parses the dictionary and extracts the first column, containing the words which may
   or may not be the part of overall "Serbian" corpus used to create the output file
   (where only the unique are used). Please see config file and SETUSECRO switch.

2. To convert the dictionary into JSON/MongoDB data base, for further use and plans.
   The aim of this is to have a solid platform (via web interface) for editing the
   dictionary and eventually compiling one big Serbo-Croatian/BSH dictionary. The
   new dictionary would be based on Igaly's dictionary (and its extensive POS data)
   and Serbian Hunspell. MongoDB and JSON were chosen because the author of this
   code already had installed all needed software and reference material.  

"""
import os
import sys

sys.path.append("../")

import conf
import helpers
import labels

def calculate_stats():
    """
    Calculate basic stats about the file.
    """
    print("CROATIAN DICTIONARY STATS")
    fsize = helpers.fsize(conf.PATH_CROD)
    print("Size of the Croatian dictionary file is %s MB" % fsize)
    fcontent = open(conf.PATH_CROD).readlines()
    print("It contains %s lines of text." % len(fcontent))
    print("Parsing, please wait...")
    stats = []
    for line in fcontent:
        tab_count = len(line.split('\t'))
        if tab_count not in stats:
            stats.append(tab_count)
    stats.sort()
    print("Column lengths in files: %s" % ', '.join([str(s) for s in stats]))


def crobase_to_jsondb():
    """
    Create JSON database and populate it with Croatian
    dictionary.
    """
    import pymongo
    # Database stuff
    from pymongo import MongoClient
    client = MongoClient() 
    client = MongoClient('localhost', 27017)
    # words.db
    dbwords = client.words
    colwords = dbwords.words
    # Parse the words
    print("Parsing begins...")
    fcontent = open(conf.PATH_CROD).readlines()
    j = 0
    for line in fcontent:
        j += 1
        try:
            todb = create_line_for_db(line)
        except:
            print("Error for", line, " on line", j)
        # Check if this is a duplicate. This is *very* slow, and
        # therefore commented out.
        #dsearch = colwords.find_one({'wform':todb['wform']})
        #if dsearch == todb:
        #    print("Duplicate for", todb['wform'])
        #else:
        #    colwords.insert(todb)
        colwords.insert(todb) #slow!
    print("Lines parsed:", j)


def create_line_for_db(line):
    """
    Create/check dictionary line that goes to JSON database.
    """
    parsed = [w.strip() for w in line.split('\t')]
    parsed_for_db = {'wform':parsed[0],
                     'base':parsed[1],
                     'detid':parsed[2],
                     'pos':labels.POS_CRO[parsed[3]]}
    return parsed_for_db


def parse_crobase(lowcap=True, first_column_only=True, sep="\n"):
    """
    Parse only the first column in the dictionary and save the result.
    This needs to be done so the Croatian data is available for further
    parsing.
    
    sep - separator. If this file is to be insterted to parsing
    directory, then it must be treated as a block of text.
    """
    print("Parsing begins...")
    parsed = []
    fcontent = open(conf.PATH_CROD).readlines()
    for line in fcontent:
        if first_column_only:
            parsed.append(line.split('\t')[0].strip())
        else:
            # We are rebulding the dictionary
            pass
    path_out = os.path.join(conf.PATH_TEXTS, 'croatian.txt')
    fout = open(path_out, 'w')
    if lowcap:
        print("Lowercasing is ON...")
        parsed = sep.join([p.lower() for p in parsed])
    else:
        print("Lowercasing is OFF...")
        parsed = sep.join(parsed)
    fout.writelines(parsed)
    fout.close()
    print("Saved %s items into %s" % (len(parsed), path_out))
    print("File size of Croatian dictionary is %s MB" % helpers.fsize(path_out))
