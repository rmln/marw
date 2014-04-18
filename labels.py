"""
Labels for misc elements.
"""

import conf

LB = {'cases_full':{0:'nominative',
                    1:'genitive',
                    2:'dative',
                    3:'accusative',
                    4:'vocative',
                    5:'locative',
                    6:'instrumental',
                    7:'nominative',
                    8:'genitive',
                    9:'dative',
                    10:'accusative',
                    11:'vocative',
                    12:'instrumental',
                    13:'locative',
               },
      'cases_short':{0:'nom',
                    1:'gen',
                    2:'dat',
                    3:'acc',
                    4:'voc',
                    5:'loc',
                    6:'inst',
                    7:'nom',
                    8:'gen',
                    9:'dat',
                    10:'acc',
                    11:'voc',
                    12:'inst',
                    13:'loc',
               },
      'persons_full':{0: '1st person singular',
                     1: '2nd person singular',
                     2: '3rd person singular',
                     3: '1st person plural',
                     4: '2nd person plural',
                     5: '3rd person plural'},

      'persons_short':{0: '1st sg.',
                     1: '2nd sg.',
                     2: '3rd sg.',
                     3: '1st pl.',
                     4: '2nd pl.',
                     5: '3rd pl.'},

      'nounc_classes_desc': {1:"Masculine nouns ending in vowel or neuter nouns ending in -о or -е.",
                             2:'Nouns ending in -а (mostly feminine, but also some masculine).',
                             3:'Feminine nouns ending in consonant, with -и in genitive and almost all other cases.'
                             }
      
}

POS_CRO = {'broj': 'number',
           'prijedlog': 'prep', 
           'imenica': 'n', 
           'prilog': 'adv',
           'zamjenica': 'pron',
           'čestica': 'part', 
           'kratica': 'abbr',
           'veznik': 'conj', 
           'uzvik': 'int',
           'pridjev': 'adj',
           'glagol':'v',
           '':'NA'}


def generate_labels():
    """
    Return a dictionary with labels.
    """
    dlab = {}
    for line in open(conf.PATH_TABLABELS).readlines():
        items = [i.strip() for i in line.split('\t')]
        dlab[items[0]] = [i for i in items[1:]]
    return dlab

codes = generate_labels()
