"""

Return the percentare of word similarity.

In: aaaa, aaaa
Out: 100

In: aaab, aaaa
Out: 75%

In: aaaa, bbbb
Out: 0%

Used at: http://srmorph.languagebits.com/words

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



import os
import conf

PATH = conf.PATH

def calculate_word_percentage_similarity(word1, word2):
    """
    Return the percentage of word similarity.
    """
    # Select the longer word to iterrate over
    if len(word2) > len(word1):
        word_iterate = word2
        word_compare = word1.ljust(len(word2))
    else:
        word_iterate = word1
        word_compare = word2.ljust(len(word1))
    # Compare the letters
    i = 0
    same_letter = 0
    for wi in word_iterate:
        wc = word_compare[i]
        if wc == wi:
            same_letter = same_letter + 1
        i = i + 1
    # Calcuate the percentage
    m = len(word_compare)
    perc = round((same_letter/m)*100)
    return perc

def search_similar_words(word, perc, corpus=False):
    """
    Return all words similar to word, filtered
    by the percentage.
    """
    results = []
    # If hunspellsr is not provided, that
    # means this function is called from a class.
    if not corpus:
        corpus = load_dictionaries()
    for hword in corpus:
        #hword = hword.strip()
        if not calculate_word_percentage_similarity(word, hword) < perc:
            results.append(hword)
    return results    
