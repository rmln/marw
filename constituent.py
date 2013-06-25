"""
Calculate all words from the constituent letters.

Used at: http://srmorph.languagebits.com/constituent
"""

    # srmorph - Pythonic Experiments in Serbian Morphology
    # Copyright (C) 2013 Romeo Mlinar

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



import helpers
from text.makewords import load_dictionaries

def find_words_from_letters(word, lenmin=3, lenmax=False, corpus=False):
    """
    Find all words that can be created from letters in 'word'.
    """
    words = {}
    words['w'] = {}
    # If max len is not provided, them max len is
    # the length of the word provided.
    if lenmax == False:
        lenmax = len(word)
        words['lenmax_correction_type'] = 'set_as_word_lenth_by_def'
    if lenmax > len(word):
        lenmax = len(word)
        words['lenmax_correction_type'] = 'set_as_word_lenth'
    else:
        words['lenmax_correction_type'] = 'none'
    words['lenmax'] = lenmax
    # If not called from class, load the corpus.
    if not corpus:
        corpus = load_dictionaries(fromclass=False)
    # Iterate over words in corpus.
    cmain = get_letters(word)
    for w in corpus:
        wl = len(w)
        if (wl >= lenmin) and (wl <= lenmax):
        #if True:
            if can_be_made(cmain, w):
                try:
                    words['w'][wl].append(w)
                except KeyError:
                    words['w'][wl] = [w, ]
    return words
    #return helpers.sort_dictionary(words)


def can_be_made(cmain, sub):
    """
    Return true is sub word can be made from letters in the main word. 
    
    cmain already has calculated letters to save time. 
    """
    # Get constituent letters of the sub word.
    csub = get_letters(sub)
    # condition: must have all letters.
    if not set(cmain.keys()).issuperset(set(csub.keys())):
        return False
    else:
        for i in csub:
            if not (csub[i] <= cmain[i]):
                return False
    return True
            
def get_letters(word):
    """
    Return a dictionary with counted letters
    from the word.
    """
    letters = {}
    for i in word:
        try:
            letters[i] = letters[i] + 1
        except KeyError:
            letters[i] = 0
    return letters
