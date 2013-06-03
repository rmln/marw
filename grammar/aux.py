"""

Auxiliary verbs.

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


from .meta import MVerb

class AuxVerbToBeFullPresentAffirmative(MVerb):
    """
    Auxiliary verb 'to be', full form ('наглашени облик'), affirmative.
    Ref. Klajn 118
    """
    pos = 'MVerb'
    meaning = 'to be'
    infinitive = 'бити'
    tense = 'present'
    form = 'full'
    person = ('јесам', 'јеси', 'јесте', 'јесмо', 'јесте', 'јесу')


class AuxVerbToBeFullPresentNegative(MVerb):
    """
    Auxiliary verb 'to be', full form ('наглашени облик'), negative.
    """
    pos = 'MVerb'
    meaning = 'not to be'
    infinitive = 'бити'
    tense = 'present'
    form = 'full'
    negative = True
    person = ('нисам', 'ниси', 'није', 'нисмо', 'нисте', 'нису')


class AuxVerbToBeShortPresentAffirmative(MVerb):
    """
    Auxiliary verb 'to be', short form ('енклитички облик'), affirmative.
    Ref. Klajn 118
    """
    pos = 'MVerb'
    meaning = 'be'
    infinitive = 'бити'
    tense = 'present'
    form = 'full'
    person = ('сам', 'си', 'је', 'смо', 'сте', 'су')


class AuxVerbWillFullPresentAffirmative(MVerb):
    """
    Auxiliary verb 'will', full form ('наглашени облик'), affirmative.
    Ref. Klajn 118
    """
    pos = 'MVerb'
    meaning = 'will'
    infinitive = 'хоћу'
    tense = 'present'
    form = 'full'
    person = ('хоћу', 'хоћеш', 'хоће', 'хоћемо', 'хоћете', 'хоће')


class AuxVerbWillShortPresentAffirmative(MVerb):
    """
    Auxiliary verb 'will', short form ('енклитички облик'), affirmative.
    Ref. Klajn 118
    """
    pos = 'MVerb'
    meaning = 'will'
    infinitive = 'хоћу'
    tense = 'present'
    form = 'short'
    person = ('ћу', 'ћеш', 'ће', 'ћемо', 'ћете', 'ће')



class AuxVerbWillShortPresentNegative(MVerb):
    """
    Auxiliary verb 'will', short form ('енклитички облик'), affirmative.
    Ref. Klajn 118
    """
    pos = 'MVerb'
    meaning = 'will not'
    infinitive = 'хоћу'
    tense = 'present'
    form = 'short'
    negative = True
    person = ('нећу', 'нећеш', 'неће', 'нећемо', 'нећете', 'неће')
