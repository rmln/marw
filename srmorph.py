"""

Command line interface to misc functions.

Switches:

-h     --help              This text.   

-p     --parse             Parse all files in data/text and store them in 
                           data/parsed. Update only.

-P     --parseclean        Parse as above, but overwrite already parsed
                           files.

-c     --crostats          Return stats about the Croatian dictionary. 

-b     --parsecrobase      Parse the base (first column) in the Croatian
                           dictionary.

-e     --exportcorpus      Generate corpus (makes tar.gz of all sources).

-E     --exportcorpusns    Generate corpus (makes tar.gz of all sources,
                           but uses only find parsed files).

"""

import os
import sys
import getopt

sys.path.append("../")

from tools import croparser
from tools import createcorpus
from text import makewords


args_short = 'hpPcbeE'
args_long = ['help',
             'parse',
             'parseclean',
             'crostats',
             'parsecrobase',
             'exportcorpus',
             'exportcorpusnp']

if __name__ == "__main__":
    args = sys.argv[1:]
    try:
        cmd, r = getopt.getopt(args, args_short, args_long)
    except:
         print("Error in command args: %s" % str(args))

    for o, a in cmd:
        if o in ('-h', '--help'):
            print(__doc__)
        if o in ('-p', '--parse'):
            makewords.parse_all_files(overwrite=False)
        if o in ('-P', '--parseclean'):
            makewords.parse_all_files(overwrite=True)
        if o in ('-c', '--crostats'):
            croparser.calculate_stats()
        if o in ('-b', '--parsecrobase'):
            croparser.parse_crobase()
        if o in ('-e', '--exportcorpus'):
            createcorpus.generate_corpus()
        if o in ('-E', '--exportcorpusnp'):
            createcorpus.generate_corpus(overwrite=False)
            createcorpus.pack_corpus()
