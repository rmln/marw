"""
Create corpus.

The resulting file can be downloaded at:

http://srmorph.languagebits.com/database
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

from text import  makewords
import similarity
import conf
import subprocess

def generate_corpus():
    """
    Save corpus.
    """
    makewords.parse_all_files(overwrite=True)
    makewords.save_corpus()

def pack_corpus():
    """
    Create, save and gzip the corpus for distribution.
    """
    print("Will be saved to", conf.PATH_EXPORT_TAR)
    print("Creating readme...")
    readme = open(conf.PATH_EXPORT_README, "w")
    text = conf.corpus_readme % {
        'sources':conf.corpus_sources,
        'log':open(conf.PATH_PARSE_LOG, 'r').read()
        }
    readme.write(text)
    readme.close()
    print("Compressing...")
    subprocess.check_call(["tar",
                           "-C", # Change dir
                           conf.PATH_TEMP,
                           "-zcvf",
                           conf.PATH_EXPORT_TAR,
                           "srmorph-corpus.txt",
                           "readme.txt"])
    
generate_corpus()    
pack_corpus()
