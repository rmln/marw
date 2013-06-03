"""

Finds affixes in words.

Used at:

http://srmorph.languagebits.com/word
http://srmorph.languagebits.com/affixes

"""


    # srmorph - Pythonic Experiments in Serbian Morphology
    # Copyright (C) <year>  <name of author>

    # This program is free software: you can redistribute it and/or modify
    # it under the terms of the GNU General Public License as published by
    # the Free Software Foundation, either version 3 of the License, or
    # (at your option) any later version.

    # This program is distributed in the hope that it will be useful,
    # but WITHOUT ANY WARRANTY; without even the implied warranty of
    # MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    # GNU General Public License for more details.

    # You should have received a copy of the GNU General Public License
    # along with this program.  If not, see <http://www.gnu.org/licenses/>.



import lister

def search_dictionary(affixlist, word):
    """
    Return found words for word/affixlist.
    """
    pass


def analyze_word(word):
    """
    Find affixes in word.

    Returns:

    {'startswith': {'prefix': ['AffClassName' ... ]},
     'endswith': {'suffix': ['AffClassName' ... ]}
     }

    """
    # Hold the results in these.
    _d_search_results = {'startswith':{}, 'endswith':{}}
    _search_results = {'startswith':[], 'endswith':[]}
    # Iterate over these:
    title_affixes = ('prefix', 'suffix')
    # AFFS = {'prefix':[], 'infix'... 'suffix':..}
    AFFS = lister.get_all_affixes()
    # Normalize word
    word = word.strip().lower()
    # Go thought the affixes.
    for affix_type in title_affixes:
        #print("Searching through %s" % affix_type)
        for _aff in AFFS[affix_type]:
            
            if affix_type == 'prefix':
                funct = 'startswith'
            if affix_type == 'suffix':
                funct = 'endswith'

            if getattr(word, funct)(_aff):
                _search_results[funct] += lister.get_classes_by_affix(_aff)
                try:
                    _d_search_results[funct][_aff] += \
                        lister.get_classes_by_affix(_aff)
                except KeyError:
                    _d_search_results[funct][_aff] = \
                        lister.get_classes_by_affix(_aff)
                    
    return _d_search_results

#print(analyze_word('учење'))
    
