"""

Command line interface to misc functions.

Switches:

-h     --help        This text.   

-p     --parse       Parse all files in data/text and store them in 
                     data/parsed. Update only.

-P     --parseclean  Parse as above, but overwrite already parsed
                     files.

"""

import os
import sys
import getopt

sys.path.append("../")

# srpmorph stuff
from text import makewords

args_short = 'hpP'
args_long = ['help', 'parse', 'parseclean']

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
