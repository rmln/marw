"""
Deals with Cyrillic conversion of words.
"""

import os
import sys

sys.path.append("../")

import cyrconv

def append_cyrillic(data):
    """
    Append a Cyrillic version of the word into
    each element of data that comes from database.

    IN:
    [{'base': 'test', 
      'wform': 'test',
      'pos': 'n',
      '_id': ObjectId('53543f1c54cf0d241de4aee5'),
      'detid': ''}, ... ]

    OUT:
    [{'base': 'test', 
      'wform': 'test',
      'base_c': 'тест', 
      'wform_c': 'тест',
      'pos': 'n',
      '_id': ObjectId('53543f1c54cf0d241de4aee5'),
      'detid': ''}, ... ]
    """
    #Instantiate the conversion class
    cnv = cyrconv.CirConv()
    # Count them, so dictionaries can be
    # located by position, and modofied.
    elems = len(data)
    for i in range(elems):
        try:
            data[i]['base_c'] = cnv.convert(data[i]['base'])
            data[i]['wform_c'] = cnv.convert(data[i]['wform'])
        except ValueError:
            data[i]['base_c'] = 'E'
            data[i]['wform_c'] = 'E'
    return data
        

        
