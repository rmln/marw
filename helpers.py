"""
Miscellaneous helper functins. 
"""

import os
import conf
import copy

import cyrconv
crconv = cyrconv.CirConv()

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

def cyrilic_check_convert(word):
    """
    Check/convert the word to Cyrillic script.
    
    Returns False is word cannot be converted to
    Cyrillic script, otherwise returns the converted
    form of the word.
    """
    # Is all text in this word Cyrillic?
    # If yes, just return the word.
    allcyr = crconv.is_all_cyrillic(word)
    if allcyr:
        return word
    # What to do if not?
    else:
        # First, check if the word contains only letters
        # of the Serbian alphabet (no x, y, q)
        if crconv.is_all_latin(word):
            # It's safe to convert it to Cyrilic.
            return crconv.convert(word)
        else:
            return False

def perc(x, y, r=2):
    """
    Return percentage of x in y.
    """
    return round(100 * float(x)/float(y), r)
