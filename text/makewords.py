"""

Module for work with texts.

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



import sys
sys.path.append("../")

import os
import string

import conf
import cyrconv
crconv = cyrconv.CirConv()

extrachar = '“„—®’”'

def extract_words(text):
    """
    Extract words from text, stripping it from any interpunction.
    Returns: tuple.
    """
    words = []
    tsplit = []
    # Split them
    _temp = text.split(" ")
    for word in _temp:
        if '\n' in word:
            tsplit = tsplit + word.split('\n')
        else:
            tsplit.append(word)
    # Go over each "word"
    exclude = set(string.punctuation + string.digits + '\ufeff' + extrachar)
    for s in tsplit:
        s = s.strip().lower()
        s = ''.join(c for c in s if c not in exclude)
        allcyr = crconv.is_all_cyrillic(s)
        if (s not in ('', '\n', '\r')) and allcyr:
            words.append(s)
    return words


def parse_all_files(overwrite=False):
    """
    Process all files and extract words.
    If overwrite is False, skip files that are already
    processed.
    """
    logfile = open(conf.PATH_PARSE_LOG, "w")
    filelist = []
    wordcount = 0
    print("Loading from", conf.PATH_TEXTS)
    print("Saving to", conf.PATH_PARSED)
    for files in os.listdir(conf.PATH_TEXTS):
        if files.lower().endswith(".txt"):
            if not overwrite:
                parsed = os.path.join(conf.PATH_PARSED, files)
                if not os.path.exists(parsed):
                    filelist.append(files)
                else:
                    print("Skipping %s." % files)
            else:
                filelist.append(files)

    print("Indexed", len(filelist), "files.")
    for f in filelist:
        path = os.path.join(conf.PATH_TEXTS, f)
        print("Processing %s..." % f)
        fp = os.path.join(conf.PATH_TEXTS, f)
        text = open(fp, mode='r').read()
        ptext = extract_words(text)
        # Lengths
        wordsall = len(ptext)
        wordsunique = len(set(ptext))
        percentage = get_perc(wordsunique, wordsall)
        print("\twords %s\tunique %s\tunique %s%% " % \
                  (wordsunique, wordsall, percentage))
        print("words %s\tunique %s\tunique %s%%\t%s" % \
                  (wordsunique, wordsall, percentage, f),
              file=logfile)
        wordcount = wordcount + len(ptext)
        open(os.path.join(conf.PATH_PARSED, f), 
             mode='w').write('\n'.join(ptext))
    print("\ntotal (with repeats) %s" % wordcount, file=logfile)
    print("Total word count is", wordcount)
        

def load_dictionaries(fromclass=False):
    """
    Load available dictionaries.
    """
    corpus = []
    for f in os.listdir(conf.PATH_PARSED):
        if f.lower().endswith(".txt"):
            pf = os.path.join(conf.PATH_PARSED, f)
            content = open(pf, mode='r').readlines()
            corpus = corpus + content
    # Strip all words:
    corpus = [i.strip() for i in corpus]
    lenall = len(corpus)
    ucorpus = set(corpus)
    lenunique = len(ucorpus)
    uniqueperc = get_perc(lenunique, lenall)
    print("Words in parsed corpus:", lenall)
    print("Returning %s unique words." % lenunique)
    print("Percentage of unique words is %s%%" % uniqueperc)
    if not fromclass:
        logfile = open(conf.PATH_PARSE_LOG, "a")
        print("\ntotal %s\tunique %s\tunique %s%%:" % \
                  (lenall, lenunique, uniqueperc),
              file=logfile)
    return(ucorpus)

def save_corpus():
    """
    Save corpus to PATH_EXPORT_CORPUS.
    """
    corpus = load_dictionaries()
    corpus = list(corpus)
    corpus.sort()
    open(conf.PATH_EXPORT_CORPUS, mode='w').write(''.join(corpus))
    print("Written to", conf.PATH_EXPORT_CORPUS)

def get_perc(x, y):
    """
    Returns percentage of x in y.
    """
    if x == 0 or y == 0:
        return 0
    return round((x/y)*100)
