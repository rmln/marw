"""
Affix classes.

This file contains data affix classes for each part of speech. The classes
inherit from the meta classes from meta.py - to acquire methods and attributes.

0 Nom
1 Gen
2 Dat
3 Acc
4 Voc
5 Loc
6 Ins

Affix classes follow strict naming rules that fit a line of doc string
formatting:

Name: 'Aff' + <Pos> + <Process> + <optional unique id>.
Doc: <Type of affix>. 'Example:' ''example1''. 'Ref.' + <reference id> + <page>.

Class attributes:

- altform
  Alternative affixes for a given POS.

- blendswith
  Defines base properties. For example, noun stem ending in a fricative.

- condition
  Describes semantical property of a given POS, i.e. does a noun describes a
  person, job etc.

- ending
  Endings for a given pos. This is a generic attribute, more specific is
  plural/singular/person/etc.

- gender
  Grammatical gender.

- gender_forms
  In adjectives, a dictionary with endings for m, f and n forms in the
  nominative case.

- persons
  Conjugation endings. There must be six items in this attribute, if needed
  empy ones (3 for singular, 3 for plural).

- place
  States where the affix goes in reference to the base: start, end, middle
  (prefix, infix, suffix).

- plural
  In adjectives and nouns, suffuxes for plural. There must be 7 items.

- pos
  Metaclass for a resulting word.

- process
  Grammatical 'process', i.e. derivation, conjugation etc.

- requires
  Metaclass of the stem. For example, for a derivation the word must originate
  from MNoun or MAdjective class.

- singular
  In adjectives and nouns, suffuxes for singular. There must be 7 items (at
  least in Serbian, on which the code is based).

- subtype
  Closer defines the type attribute. If a type is gradation, subtype can be
  comparaton.

- maintype
  Part of speech ID for a resulting word.

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


from .meta import MAffix

__author__ = 'Romeo Mlinar'
__mail__ = "mlinar [a] languagebits.com"
__language__ = 'serbian'

#TODO: Can pos anything alse than one item only? No.

class AffNounDeclension0(MAffix):
    """Suffix. Example: 'доктор'. Ref. Klajn:51."""
    pos = 'MNoun'
    place = 'end'
    process = ('inflection', 'declension')
    subtype = 1
    gender = 'm'
    suffix = {0:'', 1:'а', 2:'у', 3:'а', 4:'е', 5:'ом', 6:'у'}
    blendswith = ('nonpalatal',)

class AffNounDeclension1(MAffix):
    """Suffix. Example: 'пријатељ'. Ref. Klajn:51"""
    pos = 'MNoun'
    place = 'end'
    process = ('inflection', 'declension')
    subtype = 1
    gender = 'm'
    suffix = {0:'', 1:'а', 2:'у', 3:'', 4:'е', 5:'ом', 6:'у'}
    blendswith = ('palatal',)

class AffNounDeclension2(MAffix):
    """Suffix. Example: 'завод'. Ref. Klajn:51"""
    pos = 'MNoun'
    place = 'end'
    process = ('inflection', 'declension')
    subtype = 1
    gender = 'm'
    suffix = {0:'', 1:'а', 2:'у', 3:'', 4:'е', 5:'ом', 6:'у'}
    blendswith = ('nonpalatal',)

class AffNounDeclension3(MAffix):
    """Suffix. Example: 'чекић'. Ref. Klajn:51"""
    pos = 'MNoun'
    place = 'end'
    process = ('inflection', 'declension')
    subtype = 1
    gender = 'm'
    suffix = {0:'', 1:'а', 2:'у', 3:'', 4:'у', 5:'ем', 6:'у'}
    blendswith = ('palatal',)

class AffNounDeclension4(MAffix):
    """Suffix. Ref. Klajn:51"""
    pos = 'MNoun'
    place = 'end'
    process = ('inflection', 'declension')
    subtype = 1
    gender = 'm'
    suffix = {7:'и', 8:'а', 9:'има', 10:'е', 11:'и', 12:'има', 13:'има'}

class AffNounDeclension5(MAffix):
    """Suffix. Example: 'станови', 'мужеви'. Ref. Klajn:51-52"""
    pos = 'MNoun' # TODO: Check rules for this in Klajn.
    place = 'end'
    process = ('inflection', 'declension')
    subtype = 1
    gender = 'm'
    suffix = {7:'и', 8:'а', 9:'има', 10:'е', 11:'и', 12:'има', 13:'има'}
    infix = ('ов','ев')

class AffNounDeclension6(MAffix):
    """Suffix. Example: 'село'. Ref. Klajn:58"""
    pos = 'MNoun'
    place = 'end'
    process = ('inflection', 'declension')
    subtype = 1
    gender = 'n'
    suffix = {0:'о', 1:'а', 2:'у', 3:'о', 4:'о', 5:'ом', 6:'у'}

class AffNounDeclension7(MAffix):
    """Suffix. Example: 'поље'. Ref. Klajn:58"""
    pos = 'MNoun'
    place = 'end'
    process = ('inflection', 'declension')
    subtype = 1
    gender = 'n'
    suffix = {0:'е', 1:'а', 2:'у', 3:'о', 4:'о', 5:'ем', 6:'у'}

class AffNounDeclension8(MAffix):
    """Suffix. Example: 'поље', 'село'. Ref. Klajn:58"""
    pos = 'MNoun'
    place = 'end'
    process = ('inflection', 'declension')
    subtype = 1
    gender = 'n'
    suffix = {7:'а', 8:'а', 9:'има', 10:'а', 11:'а', 12:'има', 13:'има'}
    #TODO: Nepostojano """a""". str. 59.

class AffNounDeclension9(MAffix):
    """Suffix. Example: 'очи', 'уши'. Ref. Klajn:59-60"""
    pos = 'MNoun'
    place = 'end'
    process = ('inflection', 'declension')
    subtype = 1
    gender = 'n'
    suffix = {7:'и', 8:'ију', 9:'има', 10:'и', 11:'и', 12:'има', 13:'има'}
    #blendswith = ('exception') TODO

class AffNounDeclension10(MAffix):
    """Suffix. Example: 'име'. Ref. Klajn:59-60"""
    pos = 'MNoun'
    place = 'end'
    process = ('inflection', 'declension')
    subtype = 1
    gender = 'n'
    suffix = {0:'е', 1:'а', 2:'у', 3:'е', 4:'е', 5:'ом', 6:'у'}
    infix = ('н',)
    # TODO: Solve problem of multiple infixes.

class AffNounDeclension11(MAffix):
    """Suffix. Example: 'име', 'уже'. Ref. Klajn:60-61"""
    pos = 'MNoun'
    place = 'end'
    process = ('inflection', 'declension')
    subtype = 1
    gender = 'n'
    suffix = {7:'а', 8:'а', 9:'има', 10:'а', 11:'а', 12:'има', 13:'има'}
    infix = ('н', 'т')
    # TODO: Is this a doublet?

class AffNounDeclension12(MAffix):
    """Suffix. Example: 'риба'. Ref. Klajn:62"""
    pos = 'MNoun'
    place = 'end'
    process = ('inflection', 'declension')
    subtype = 2
    gender = 'f', 'm'
    suffix = {0:'а', 1:'е', 2:'и', 3:'у', 4:'о', 5:'ом', 6:'и'}
    #TODO: Many exceptions.

class AffNounDeclension13(MAffix):
    """Suffix. Example: 'риба'. Ref. Klajn:62"""
    pos = 'MNoun'
    place = 'end'
    process = ('inflection', 'declension')
    subtype = 2
    gender = 'f', 'm'
    suffix = {7:'е', 8:'а', 9:'ама', 10:'е', 11:'е', 12:'ама', 13:'ама'}
    #TODO: Many exceptions.

class AffNounDeclension14(MAffix):
    """Suffix. Example: 'реч'. Ref. Klajn:66"""
    pos = 'MNoun'
    place = 'end'
    process = ('inflection', 'declension')
    subtype = 3
    gender = 'f'
    suffix = {0:'', 1:'и', 2:'и', 3:'', 4:'и', 5:'ју', 6:'и'}
    blendswith = ('ends_in_consonant',)
    altform = ((5, 'и', 'doublet'),) # (case, ending, rule)
    #TODO: Devise altform schemata.

class AffNounDeclension15(MAffix):
    """Suffix. Example: 'реч'. Ref. Klajn:66"""
    pos = 'MNoun'
    place = 'end'
    process = ('inflection', 'declension')
    subtype = 3
    gender = 'f'
    suffix = {7:'и', 8:'и', 9:'има', 10:'и', 11:'и', 12:'има', 13:'има'}
    blendswith = ('ends_in_consonant',)

# Adjectives

class AffAdjectiveDeclension0(MAffix):
    """Suffix. Example: 'леп', 'бео'. Ref. Stevanović:85"""
    pos = 'MAdjective'
    place = 'end'
    process = ('inflection', 'declension')
    gender = 'm'
    suffix = {0:'', 1:'а', 2:'у', 3:'', 4:'и', 5:'им', 6:'у'}
    condition = ('descriptive', 'material', 'nondefinite')
    altform = ((3, 'a', 'doublet'),)

class AffAdjectiveDeclension1(MAffix):
    """Suffix. Example: 'леп', 'беo'. Ref. Stevanović:85"""
    pos = 'MAdjective'
    place = 'end'
    process = ('inflection', 'declension')
    gender = 'm'
    suffix = {7:'и', 8:'их', 9:'им', 10:'е', 11:'и', 12:'им', 13:'им'}
    condition = ('descriptive', 'material', 'nondefinite')
    altform = ((2, 'има', 'doublet'), (5, 'има', 'doublet'))

class AffAdjectiveDeclension2(MAffix):
    """Suffix. Example: 'лепи', 'бели'. Ref. Stevanović:85"""
    pos = 'MAdjective'
    place = 'end'
    process = ('inflection', 'declension')
    gender = 'm'
    suffix = {0:'и', 1:'ог', 2:'ом', 3:'и', 4:'и', 5:'им', 6:'ом'}
    condition = ('descriptive', 'material', 'definite')
    altform = ((2, 'оме', 'doublet'), (3, 'ог', 'doublet'),
               (5, 'оме', 'doublet'))

class AffAdjectiveDeclension3(MAffix):
    """Suffix. Example: 'лепи', 'бели'. Ref. Stevanović:85"""
    pos = 'MAdjective'
    place = 'end'
    process = ('inflection', 'declension')
    gender = 'm'
    suffix = {7:'и', 8:'ох', 9:'има', 10:'е', 11:'и', 12:'им', 13:'им'}
    condition = ('descriptive', 'material', 'definite')
    altform = ((2, 'има', 'doublet'), (5, 'има', 'doublet'),
               (6, 'има', 'doublet'))

class AffAdjectiveDeclension4(MAffix):
    """Suffix. Example: 'широко'. Ref. Stevanović:85"""
    pos = 'MAdjective'
    place = 'end'
    process = ('inflection', 'declension')
    gender = 'n'
    suffix = {0:'о', 1:'а', 2:'у', 3:'о', 4:'о', 5:'им', 6:'у'}
    condition = ('nondefinite',)

class AffAdjectiveDeclension5(MAffix):
    """Suffix. Example: 'широко'. Ref. Stevanović:85"""
    pos = 'MAdjective'
    place = 'end'
    process = ('inflection', 'declension')
    gender = 'n'
    suffix = {0:'а', 1:'их', 2:'им', 3:'а', 4:'а', 5:'им', 6:'им'}
    condition = ('nondefinite',)
    altform = ((5, 'има', 'doublet'), (6, 'има', 'doublet'))

class AffAdjectiveDeclension6(MAffix):
    """Suffix. Example: 'широко'. Ref. Stevanović:85"""
    pos = 'MAdjective'
    place = 'end'
    process = ('inflection', 'declension')
    gender = 'n'
    suffix = {0:'о', 1:'ог', 2:'ом', 3:'о', 4:'о', 5:'им', 6:'им'}
    condition = ('definite',)
    altform = ((1, 'ога', 'doublet'), (2, 'оме', 'doublet'),
               (6, 'оме', 'doublet'))

class AffAdjectiveDeclension7(MAffix):
    """Suffix. Example: 'широко'. Ref. Stevanović:85"""
    pos = 'MAdjective'
    place = 'end'
    process = ('inflection', 'declension')
    gender = 'n'
    suffix = {7:'а', 8:'их', 9:'им', 10:'а', 11:'а', 12:'им', 13:'им'}
    condition = ('definite',)
    altform = ((2, 'има', 'doublet'), (5, 'има', 'doublet'),
               (6, 'има', 'doublet'))

class AffAdjectiveDeclension8(MAffix):
    """Suffix. Example: 'широка'. Ref. Stevanović:86"""
    pos = 'MAdjective'
    place = 'end'
    process = ('inflection', 'declension')
    gender = 'f'
    suffix = {0:'а', 1:'е', 2:'ој', 3:'у', 4:'а', 5:'ом', 6:'ој'}

class AffAdjectiveDeclension9(MAffix):
    """Suffix. Example: 'широко'. Ref. Stevanović:86"""
    pos = 'MAdjective'
    place = 'end'
    process = ('inflection', 'declension')
    gender = 'n'
    suffix = {7:'е', 8:'их', 9:'им', 10:'е', 11:'е', 12:'им', 13:'им'}
    condition = ('definite',)
    altform = ((2, 'има', 'doublet'), (5, 'има', 'doublet'),
               (6, 'има', 'doublet'))

class AffAdjectiveComparative0(MAffix):
    """Suffix. Example: 'храбрији'. Ref. Stevanović:87"""
    pos = 'MAdjective'
    place = 'end'
    process = ('inflection', 'gradation')
    subtype = 'comparative'
    condition = ('comparative', 'multisyllabic') #TODO: How does this fit in 'condition'?
    infix = ('иј',)
    gender_forms = {'m':'и', 'f':'а', 'n':'е'}
    # TODO Comparation needs work.

class AffAdjectiveComparative1(MAffix):
    """Suffix. Example: 'млађи', 'живљи'. Ref. Stevanović:88"""
    pos = 'MAdjective'
    place = 'end'
    process = ('inflection', 'gradation')
    subtype = 'comparative'
    condition = ('comparative', 'iotation')
    infix = ('ј',)
    gender_forms = {'m':'и', 'f':'а', 'n':'е'}

class AffAdjectiveSuperlative0(MAffix):
    """Suffix. Example: 'најхрабрији'. Ref. Stevanović:88"""
    pos = 'MAdjective'
    place = 'end'
    process = ('inflection', 'gradation')
    subtype = 'superlative'
    place = 'start'
    condition = ('superlative',)
    prefix = ('нај',)

# Verbs

class AffVerbInf(MAffix):
    """Suffix. Example: 'певати', 'читати'. Ref. http://sr.wikipedia.org/sr-el/infinitiv/"""
    pos = 'MVerb'
    place = 'end'
    process = ('inflection',)
    blendswith = ('infinitive_base')
    maintype = 'infinitive'
    suffix = ('ти', 'ћи')

class AffVerbInfNonf(MAffix):
    """Suffix. Example: 'обећавати', 'приморавати', 'досађивати' Ref. Klajn:108"""
    pos = 'MVerb'
    place = 'end'
    process = ('inflection',)
    blendswith = ('infinitive_base',)
    maintype = 'infinitive'
    subtype = 'nonfinite'
    suffix = ('авати',)
    altform = (('ending', 'ивати'), ('ending', 'евати'))

class AffVerbImperative0(MAffix):
    """Suffix. Example: 'чекати' Ref. Klajn:110"""
    pos = 'MVerb'
    place = 'end'
    process = ('inflection', 'conjugation')
    blendswith = ('infinitive_base',) #TODO: Check this.
    maintype = 'mood'
    subtype = 'imperative'
    person = {0:'', 1:'ј', 2:'', 3:'јмо', 4:'', 5:'јте'}

class AffVerbImperative1(MAffix):
    """Suffix. Example: 'кренути' Ref. Klajn:111"""
    pos = 'MVerb'
    place = 'end'
    process = ('inflection', 'conjugation')
    blendswith = ('infinitive_base',) #TODO: Check this.
    maintype = 'mood'
    subtype = 'imperative'
    person = {0:'', 1:'и', 2:'', 3:'имо', 4:'', 5:'ите'}

class AffVerbPresent(MAffix):
    """Suffix. Example: 'кренем' Ref. Klajn:111"""
    pos = 'MVerb'
    place = 'end'
    process = ('inflection', 'conjugation')
    blendswith = 'okrnjena_osnova' #TODO: What's the name in English?
    maintype = 'tense'
    subtype = 'present'
    person = {0:'м', 1:'ш', 2:'', 3:'мо', 4:'те', 5:'е'}
    altform = ((5,'и'),(5,'ију'))

class AffVerbAorist0(MAffix):
    """Suffix. Example: 'кренух' Ref. Klajn:116"""
    pos = 'MVerb'
    place = 'end'
    process = ('inflection', 'conjugation')
    blendswith = ('infinitive_base', 'infinitive_ends_in_ti')
    maintype = 'tense'
    subtype = 'aorist'
    person = {0:'х', 1:'', 2:'', 3:'смо', 4:'сте', 5:'ше'}

class AffVerbAorist1(MAffix):
    """Suffix. Example: 'поједох' Ref. Klajn:116"""
    pos = 'MVerb'
    place = 'end'
    process = ('inflection', 'conjugation')
    blendswith = ('infinitive_base', 'infinitive_ends_in_ti',
                'infinitive_ends_in_chyi')
    maintype = 'tense'
    subtype = 'aorist'
    person = {0:'ох', 1:'е', 2:'е', 3:'осмо', 4:'осте', 5:'оше'}

class AffVerbImperfect(MAffix):
    """Suffix. Example: 'певах', 'ношах'. Ref. Klajn:117"""
    pos = 'MVerb'
    place = 'end'
    process = ('inflection', 'conjugation')
    blendswith = ('infinitive_base')
    maintype = 'tense'
    subtype = 'imperfect'
    # TODO: See less common form as well, p. 117
    person = {0:'ах', 1:'аше', 2:'аше', 3:'асмо', 4:'асте', 5:'аху'}

class AffVerbFuture0(MAffix):
    """Suffix. Example: 'певаћу'. Ref. Klajn:119
       This is just a shot form of the tense.
    """
    pos = 'MVerb'
    place = 'end'
    process = ('inflection', 'conjugation')
    blendswith = ('okrnjena_osnova',) # TODO: Check this.
    maintype = 'tense'
    subtype = 'future-1'
    # TODO: See complex form as well. p. 117
    person = {0:'ћу', 1:'ћеш', 2:'ће', 3:'ћемо', 4:'ћете', 5:'ће'}

# http://www.serbian-corpus.edu.rs/ie/tagging/new/elementsnew.htm

# .ending_singular means a nominal form of the word in m/f/n,
# while .singular denotes endings in changes.

# Serbian: radni pridjev.
class AffParticipleAdjectivalActive(MAffix):
    """Suffix. Example: 'изабрао'. Ref. Klajn:125-127"""
    pos = 'MParticiple'
    place = 'end'
    process = ('inflection',)
    maintype = 'participle'
    subtype = 'adjectivial'
    voice = 'active'
    suffix_singular = {'m':('о', 'ао', 'шао'), 'f':('ла', 'шла'), 
                       'n':('ло', 'шло')}
    suffix_plural = {'m':('ли', ), 'f':('ле',), 'n':('ла',)}
    blendswith = ('inifinitive_base')

#Serbian: trpni pridjev (pasivni particip).
class AffParticipleAdjectivalPassive(MAffix):
    """Suffix. Example: 'изабран'. Ref. Klajn:127-130
       This is a participle. It has nominal change of
       AffAdjective2 and AffAdjective3 adjectives."""
    pos = 'MParticiple'
    place = 'end'
    process = ('inflection',)
    singular = AffAdjectiveDeclension2.suffix
    plural = AffAdjectiveDeclension3.suffix
    maintype = 'participle'
    subtype = 'adjectivial'
    voice = 'passive'
    suffix_singular = {'m':('н', 'ен', 'вен'), 
                       'f':('на','ена', 'вена'),
                       'n':('но', 'ено', 'вено')}
    blendswith = ('inifinitive_base', 'present_base')

# Serbian: glagolski prilog sadašnji, gerund.
class AffParticipleAdverbialPresent(MAffix):
    """Suffix. Example: 'читајући'. Ref. Klajn:130"""
    pos = 'MParticiple'
    place = 'end'
    process = ('inflection',)
    maintype = 'participle'
    subtype = 'adverbial'
    tense = 'present'
    suffix = ('ћи',)
    blendswith = ('present_3_s')

# Serbian: glagolski prilog prošli.
class AffParticipleAdverbialPast(MAffix):
    """Suffix. Example: 'изабрабши'. Ref. Klajn:131"""
    pos = 'MParticiple'
    place = 'end'
    process = ('inflection',)
    maintype = 'participle'
    subtype = 'adverbial'
    tense = 'past'
    suffix = ('вши', 'авши', 'в')
    # TODO: How to distinguish between an alternative and """conditional""" form?
    blendswith = ('inifinitive_base',)

# Suffixes for making nouns

class AffNounDerivatonAgent(MAffix):
    """Suffix. Example: 'преводилац', 'праља'. Ref. Klajn:179-180"""
    pos = 'MNoun'
    place = 'end'
    suffix = ('*ац', 'л*ац', 'ач', 'тељ', 'ник', 'ар', 'ља', 'ара' )
    maintype = 'noun'
    subtype = 'agent'
    process = ('derivation',)

class AffNounDerivatonProfession(MAffix):
    """Suffix. Example: 'књижар', 'шеширџија'. Ref. Klajn:180"""
    pos = 'MNoun'
    place = 'end'
    suffix = ('ар', 'ник', 'аш', 'џија', 'ист*а')
    maintype = 'noun'
    subtype = 'profession'
    process = ('derivation',)

class AffNounDerivatonPeople(MAffix):
    """Suffix. Example: 'старац', 'тврдица'. Ref. Klajn:180"""
    pos = 'MNoun'
    place = 'end'
    suffix = ('*ац', 'ак', 'ар', 'ник', 'џија', 'оња', 'ица',
              'лица', 'ло')
    maintype = 'noun'
    subtype = 'describing_people'
    process = ('derivation',)

class AffNounDerivatonAffiliation(MAffix):
    """Suffix. Example: 'омладинац', 'толстојевац'. Ref. Klajn:180"""
    pos = 'MNoun'
    place = 'end'
    suffix = ('*ац', 'ов*ац', 'ев*ац', 'аш')
    maintype = 'noun'
    subtype = 'affiliation'
    process = ('derivation',)

class AffNounDerivatonEthnicity(MAffix):
    """Suffix. Example: 'Београђанин', 'странац'. Ref. Klajn:181"""
    pos = 'MNoun'
    place = 'end'
    suffix = ('*јанин', '*ац', 'ан*ац', 'лија', '*јанин')
    maintype = 'noun'
    subtype = 'ethnicity'
    process = ('derivation',)

class AffNounDerivatonGender(MAffix):
    """Suffix. Example: 'фризерка', 'муслиманка'. Ref. Klajn:181"""
    pos = 'MNoun'
    place = 'end'
    suffix = ('ица', 'ика', 'иња', 'киња', 'уша')
    maintype = 'noun'
    subtype = 'gender'
    process = ('derivation',)
    gender = 'f'

class AffNounDerivatonDeminutive(MAffix):
    """Suffix. Example: 'прозорче', 'црвић'. Ref. Klajn:182"""
    pos = 'MNoun'
    place = 'end'
    suffix = ('ић', 'чић', 'ица', 'чица', '*ац', '*ак', 'це', 'енце', 'че')
    maintype = 'noun'
    subtype = 'deminutive'
    process = ('derivation',)

class AffNounDerivatonAugmentative(MAffix):
    """Suffix. Example: 'војничина', 'лажовчина'. Ref. Klajn:182"""
    pos = 'MNoun'
    place = 'end'
    suffix = ('ина', 'чина', 'етина', 'ура', 'урда')
    maintype = 'noun'
    subtype = 'augmentative'
    process = ('derivation',)

class AffNounDerivatonTool(MAffix):
    """Suffix. Example: 'прекидач', 'штипаљка'. Ref. Klajn:182"""
    pos = 'MNoun'
    place = 'end'
    suffix = ('ач', 'лица', 'ло', 'аљка', 'иљка')
    maintype = 'noun'
    subtype = 'tool'
    process = ('derivation',)

class AffNounDerivatonSites(MAffix):
    """Suffix. Example: 'ловиште', 'шећерана'. Ref. Klajn:182-183"""
    pos = 'MNoun'
    place = 'end'
    suffix = ('иште', 'лиште', 'ана', 'ара',
              'ница', 'оница', 'ионица', 'арница',
              'ињак', 'ик')
    maintype = 'noun'
    subtype = 'site'
    process = ('derivation',)

class AffNounDerivatonNonliving(MAffix):
    """Suffix. Example: 'ловиште', 'шећерана'. Ref. Klajn:183"""
    pos = 'MNoun'
    place = 'end'
    suffix = ('ница', 'ка', 'ина', 'етина',
              'овина', 'арина', 'овача', 'евача')
    maintype = 'noun'
    subtype = 'nonliving'
    process = ('derivation',)

class AffNounDerivatonAbstGeneral(MAffix):
    """Suffix. Example: 'јунаштво', 'старост'. Ref. Klajn:183"""
    pos = 'MNoun'
    place = 'end'
    # TODO: Split them into those made from
    # nouns and those of verbs.
    suffix = ('ство', 'ост', 'ота', 'оћа',
              'ина', 'ило', 'а', 'ња',
              'ба', 'идба', '*јава', 'њава',
              '*јај', '*ак', 'еж', '',)
    maintype = 'noun'
    subtype = 'abstract_general'
    process = ('derivation',)

class AffNounDerivatonVerbal(MAffix):
    """Suffix. Example: 'чишћење', 'увенуће'. Ref. Klajn:183"""
    pos = 'MNoun'
    place = 'end'
    suffix = ('ње', 'ће')
    maintype = 'noun'
    subtype = 'verbal'
    process = ('derivation',)
    blendswith = AffParticipleAdjectivalPassive().blendswith

# Adjectivial derivation
# TODO: Blending is very complex and each base has precise
# meaning. Most of the endings can function separate.

class AffAdjectiveDerivatonRelational(MAffix):
    """Suffix. Example: 'поштански', 'мачји'. Ref. Klajn:187-191"""
    pos = 'MAdjective'
    place = 'end'
    suffix = ('ски', 'ји', 'ни', 'они', 'иони', 'овни', 'евни',
              'ан', 'ани', 'ен', 'ени', 'њи', 'ећи', 'аћи',
              'ћи', 'ов', 'ев', 'љев', 'ин')
    maintype = 'adjective'
    subtype = 'relational'
    process = ('derivation',)


class AffAdjectiveDerivatonDescriptive(MAffix):
    """Suffix. Example: 'лековит', 'запаљив'. Ref. Klajn:191-192"""
    pos = 'MAdjective'
    place = 'end'
    suffix = ('*ан', 'ни', 'ав', 'ат', 'аст', 'ит', 'ив', 'љив',
              'ушан', 'ушкаст', 'каст', 'ичаст', 'цат', 'цит')
    maintype = 'adjective'
    subtype = 'descriptive'
    process = ('derivation',)

# Derivation: Suffixes for verbs

class AffVerbDerivatonNoun0(MAffix):
    """Suffix. Example: 'цветати', 'мекшати'. Ref. Klajn:193"""
    pos = 'MVerb'
    place = 'end'
    suffix = ('ати',)
    maintype = 'verb'
    process = ('derivation',)
    requires = ('MNoun', 'MAdjective')

class AffVerbDerivatonNoun1(MAffix):
    """Suffix. Example: 'просјачити', 'блатити'. Ref. Klajn:193"""
    pos = 'MVerb'
    place = 'end'
    suffix = ('ити',)
    maintype = 'verb'
    process = ('derivation',)
    requires = ('MNoun', 'MAdjective')

class AffVerbDerivatonNoun2(MAffix):
    """Suffix. Example: 'робовати', 'лудовати'. Ref. Klajn:193-194"""
    pos = 'MVerb'
    place = 'end'
    suffix = ('овати', 'евати')
    maintype = 'verb'
    process = ('derivation',)
    requires = ('MNoun', 'MAdjective')

class AffVerbDerivatonNoun3(MAffix):
    """Suffix. Example: 'програмирати', 'фотографисати'. Ref. Klajn:194"""
    pos = 'MVerb'
    place = 'end'
    suffix = ('ирати', 'исати')
    maintype = 'verb'
    process = ('derivation',)
    requires = ('MNoun', 'MAdjective')

class AffVerbDerivatonIterative(MAffix):
    """Suffix. Example: 'куцкати', 'лупкати'. Ref. Klajn:194"""
    pos = 'MVerb'
    place = 'end'
    suffix = ('кати', 'ицати', 'уцкати', 'ицати', 'карати',
              'акати', 'утати', 'цати')
    maintype = 'verb'
    subtype= 'iterative'
    process = ('derivation',)
    requires = ('MVerb',)

#preffix-suffixation

class AffNounDerivatonPrefSuffixation(MAffix):
    """Suffix. Example: 'беспуће', 'начелник'. Ref. Klajn:195"""
    pos = 'MNoun'
    place = 'end'
    suffix = ('је', 'ица', 'ник', 'ина', '*ак',
              '*ац')
    maintype = 'noun'
    process = ('derivation',)
    # TODO: There is also zero suffix for
    # ne- prefix (ie. 'nemar')

class AffAdjectiveDerivatonPrefSuffixation(MAffix):
    """Suffix. Example: 'бескрајан', 'неуништив'. Ref. Klajn:195-196"""
    pos = 'MAdjective'
    place = 'end'
    suffix = ('*ан', 'ни', 'ски', 'љив')
    maintype = 'adjective'
    process = ('derivation',)

class AffVerbDerivatonPrefSuffixation(MAffix):
    """Prefix. Example: 'настанити', 'исправити'. Ref. Klajn:196-197"""
    pos = 'MVerb'
    place = 'start' # This is prefix.
    prefix = ('у', 'по', 'из', 'об', 'с',
              'раз', 'при', 'за',
              'на')
    maintype = 'verb'
    process = ('derivation',)
    requires = ('MNoun', 'MAdjective')

# Prefixation

class AffNounPrefixation(MAffix):
    """Prefix. Example: 'подсвест', 'нараменица'. Ref. Klajn:199-201"""
    pos = 'MNoun'
    place = 'start'
    prefix = ('без', 'за', 'међу', 'на', 'над',
              'не', 'нуз', 'о', 'по', 'под',
              'пра', 'пред', 'при', 'против', 'раз',
              'са', 'су', 'у', 'уз')
    maintype = 'noun'
    process = ('derivation', 'prefixation')
    requires = ('MNoun',)

class AffAdjectivePrefixation(MAffix):
    """Prefix. Example: 'прекоморски', 'бешуман'. Ref. Klajn:201-203"""
    pos = 'MAdjective'
    place = 'start'
    prefix = ('без', 'ван', 'до', 'за', 'међу',
              'на', 'над', 'не', 'о', 'по',
              'под', 'пра', 'пре', 'пред', 'преко',
              'при', 'про', 'против')
    maintype = 'adjective'
    process = ('derivation', 'prefixation')
    requires = ('MAdjective',)
    # TODO: how to implement sound changes in derivaton,
    # like in без?

class AffVerbPrefixation(MAffix):
    """Prefix. Example: 'додирнути', 'изићи'. Ref. Klajn:203-210"""
    pos = 'MVerb'
    place = 'start'
    prefix = ('до', 'за', 'из', 'на', 'над',
              'о', 'об', 'од', 'по', 'под',
              'пре', 'пред', 'пре', 'пред', 'при',
              'про', 'раз', 'с*а', 'у', 'уз')
    maintype = 'verb'
    process = ('derivation', 'prefixation')
    requires = ('MVerb',)

class AffAdverbPrefixation(MAffix):
    """Prefix. Example: 'неретко', 'накосутра'. Ref. Klajn:210"""
    pos = 'MAdverb'
    place = 'start'
    prefix = ('не', 'по', 'пре', 'прек*о', 'нак*о')
    maintype = 'adverb'
    process = ('derivation', 'prefixation')
    requires = ('MAdverb',)

#Filter only affix classes
affixclasses_names = [k for k in dir() if k.startswith('Aff')]
