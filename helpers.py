"""
Miscellaneous helper functins. 
"""

def sort_dictionary(d):
    """
    Sort items in dictiounary.
    """
    print("SORTING", d)
    for i in d:
        d[i] = d[i].sort()
    return d
