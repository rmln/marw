"""

Return words that are not found in hunspell.

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
import sys
sys.path.append("../")

import conf
from text import  makewords

corpus = set(makewords.load_dictionaries())
hunspell = open(conf.HUNSPELL_PATH, mode='r').readlines()

hcorpus = set(hunspell)


print("Hunspell counts %s words, of wich unique %s is used." % \
          (len(hunspell), len(hcorpus)))


diff = corpus.difference(hcorpus)
diff = list(diff)
diff.sort()

print("There is %s words that are not wound in hunspell." % len(diff))
open(conf.HUNSPELL_DIFF_PATH, mode='w').write(''.join(diff))
print("Saved to %s" % conf.HUNSPELL_DIFF_PATH)
