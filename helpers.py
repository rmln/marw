"""
Miscellaneous helper functins. 
"""

import os

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
