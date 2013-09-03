"""
Miscellaneous helper functins. 
"""

import os
import conf
import copy

def fsize(path):
    """
    Return file size in MB.
    """
    return round(os.path.getsize(path) / (1024*1000),2)


def sort_dictionary(d):
    """
    Sort items in dictiounary.
    """
    print("SORTING", d)
    for i in d:
        d[i] = d[i].sort()
    return d

def compile_sources():
    """
    Compile sources for corpus.
    """
    template = "\n\nSource id:%s\n\n%s"
    text = []
    src = copy.deepcopy(conf.corpus_sources)
    if not conf.SETUSECRO:
        # Croatian dictionary not used
        del src['HR.Txt']
    for s in src:
        #print(s)
        #print(src[s])
        text.append(template % (s, src[s]))
    return ''.join(text)
