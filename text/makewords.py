"""

Module for work with texts.

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



import sys
sys.path.append("../")

import os
import string
import random

import conf
import helpers

from tools import croparser

extrachar = '“„—®’”»«–…' 

def extract_words(text, f_errors, fname):
    """
    Extract words from text, stripping it from any interpunction.
    Returns: tuple.
    """
    words = []
    tsplit = []
    if isinstance(text, str):
        # Split text by space
        _temp = text.split(" ")
        for word in _temp:
            if '\n' in word:
                tsplit = tsplit + word.split('\n')
            else:
                tsplit.append(word)
    else:
        # The text is list/tuple, so just remove spaces/breaks
        tsplit = [t.strip() for t in text]
    # Go over each "word"
    exclude = set(string.punctuation + string.digits + '\ufeff' + extrachar)
    for s in tsplit: 
        s = s.replace('\t', ' ')
        s = s.strip()
        s = s.lower()
        s = ''.join(c for c in s if c not in exclude)
        wconverted = helpers.cyrilic_check_convert(s)
        if wconverted == False:
            f_errors.write("noallcyr in %s: '%s'\n" % (fname, wconverted))
        else:
            if (wconverted not in ('', '\n', '\r')):
                words.append(wconverted)
    #print('73 is %s' %  words[73])
    #sys.exit(0)
    return words
    

def parse_all_files(overwrite=False, usecroatian=conf.SETUSECRO):
    """
    Process all files and extract words.
    If overwrite is False, skip files that are already
    processed.
    """
    logfile = open(conf.PATH_PARSE_LOG, "w")
    f_errors = open(conf.PATH_PARSE_ERRORLOG, mode='w')
    filelist = []
    wordcount = 0
    print("Accepted extensions: %s" % ''.join(conf.PARSE_EXTENSIONS))
    print("Source:", conf.PATH_TEXTS)
    print("Saving parsed into:", conf.PATH_PARSED)
    if overwrite:
        print("Parsing all files: use overwrite=False if you wish" + \
                  " to update only.")
    else:
        print("Parsing only new files: use overwrite=True if you wish" + \
                  " to rebuild completely.")
    # Croatian dictionary check
    if usecroatian:
        print("Checking if Croatian dictionary is present...")
        if os.path.exists(os.path.join(conf.PATH_TEXTS, conf.NAME_PARSED_CRO)):
            print("Croatian dictionary is prepared for parsing, skipping...")
        else:
            print("Croatian dictionary is not prepared, extracting...")
            croparser.parse_crobase()
            print("Continuing with parsing.")
    for files in os.listdir(conf.PATH_TEXTS):
        if files.lower().endswith(conf.PARSE_EXTENSIONS):
            if not overwrite:
                parsed = os.path.join(conf.PATH_PARSED, files)
                if not os.path.exists(parsed):
                    filelist.append(files)
                else:
                    print("Skipping %s." % files)
            else:
                filelist.append(files)
    # Check for Croatian file exclusion:
    if usecroatian:
        print("Croatian dictionary will be used.")    
    else:
        if conf.NAME_PARSED_CRO in filelist:
            filelist.remove(conf.NAME_PARSED_CRO)
            print("Croatian dictionary removed from the parsing list.")
        else:
            print("Croatian dictionary not in the list.")
    print("Indexed", len(filelist), "files.")
    for f in filelist:
        path = os.path.join(conf.PATH_TEXTS, f)
        print("Processing %s..." % f)
        fp = os.path.join(conf.PATH_TEXTS, f)
        text = open(fp, mode='r').read()
        ptext = extract_words(text, f_errors, f)
        # Lengths
        wordsall = len(ptext)
        wordsunique = len(set(ptext))
        percentage = get_perc(wordsunique, wordsall)
        print("\twords %s\tunique %s\tunique %s%% " % \
                  (wordsall, wordsunique, percentage))
        print("words %s\tunique %s\tunique %s%%\t%s" % \
                  (wordsall, wordsunique, percentage, f),
              file=logfile)
        wordcount = wordcount + len(ptext)
        open(os.path.join(conf.PATH_PARSED, f), 
             mode='w').write('\n'.join(ptext))
    f_errors.close()
    print("\ntotal (with repeats) %s" % wordcount, file=logfile)
    print("Total word count is", wordcount)
    f = open(conf.PATH_PARSE_ERRORLOG, mode="r").readlines()
    print("Rejected 'words':", len(f))
    
        

def load_dictionaries(fromclass=False):
    """
    Load available dictionaries.
    """
    corpus = []
    print("Loading dictionaries and removing line breaks...")
    for f in get_parsedlist(show=False):
        pf = os.path.join(conf.PATH_PARSED, f)
        content = open(pf, mode='r').readlines()
        content = [c.strip('\n') for c in content]
        corpus = corpus + content
    # Assert that there are no spaces/endlines in
    # randomly selected word.
    #assert (' ' and '\n') not in random.choice(corpus)
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


def get_parsedlist(show=False):
    """
    Return the list of the parsed files that will be used in
    corpus creation.
    """
    flist = []
    for f in os.listdir(conf.PATH_PARSED):
        if f.lower().endswith(conf.PARSE_EXTENSIONS):
            flist.append(f)
    if show:
        print("Files will be loaded from %s" % conf.PATH_PARSED)
        print('\n\t'.join(flist))
        print("Total", len(flist), "files.")
    else:
        return flist
