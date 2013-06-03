"""
Module that deals with listings.

Used at: http://srmorph.languagebits.com/process
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



from grammar import affix

affixclasses = [getattr(affix, c) for c in affix.affixclasses_names]

def _get_participle_suffixes(ac):
    """
    In:
    suffix_singular = {'m':('н', 'ен', 'вен'), 
                       'f':('на','ена', 'вена'),
                       'n':('но', 'ено', 'вено')}
    Out: ('н', 'ен', 'вен' ... )
    """
    endings = []
    sufs = ('suffix_singular', 'suffix_plural')
    gn = ('m', 'n', 'f')
    for s in sufs:
        if s in dir(ac):
            for gender in gn:
                if gender in getattr(ac, s).keys():
                    endings = endings + list(getattr(ac, s)[gender])
    return endings

def get_all_affixes(remove_asterisk=False):
    """
    Get all affixes.
    """
    _suffix = []
    _infix = []
    _prefix = []

    for ac in affixclasses:
        class_attribs = dir(ac)
        found = False
        if 'infix' in class_attribs:
            _infix = _infix + list(ac.infix)
            found = True
        if 'gender_forms' in class_attribs:
            _suffix = _suffix + list(ac.gender_forms.values())
            found = True
        if 'person' in class_attribs:
            _suffix = _suffix + list(ac.person.values())
            found = True
        if 'prefix' in class_attribs:
            _prefix = _prefix + list(ac.prefix)
            found = True
        if 'suffix' in class_attribs:
            if isinstance(ac.suffix, dict):
                _suffix = _suffix + list(ac.suffix.values())
            else:
                _suffix = _suffix + list(ac.suffix)
            found = True

        if not found:
            if ac.__name__ in ('AffParticipleAdjectivalActive',
                               'AffParticipleAdjectivalPassive'):
                endings = _get_participle_suffixes(ac)
                if len(endings) == 0:
                    found = False
                else:
                    _suffix = _suffix + endings
                    found = True

        if not found:
            pass
            # print("Nothing found for", ac.__name__)
           
    acombined = {'prefix':set(_prefix),
                 'infix':set(_infix),
                 'suffix':set(_suffix)}
    # Cleanup
    if remove_asterisk:
        acombined = {'prefix':[i.replace('*', '') for i  in acombined['prefix']],
                     'infix':[i.replace('*', '') for i  in acombined['infix']],
                     'suffix':[i.replace('*', '') for i  in acombined['suffix']]}
    return acombined



def get_classes_by_affix(affix_searched):
    """
    Get all classes that contain affix_searched.
    """
    _classes = []

    for ac in affixclasses:
        class_attribs = dir(ac)
        found = False
        if 'infix' in class_attribs:
            if affix_searched in ac.infix:
                _classes.append(ac.__name__)
                found = True
        if 'gender_forms' in class_attribs:
            if affix_searched in ac.gender_forms.values():
                _classes.append(ac.__name__)
                found = True
        if 'person' in class_attribs:
            if affix_searched in ac.person.values():
                _classes.append(ac.__name__)
                found = True
        if 'prefix' in class_attribs:
            if affix_searched in ac.prefix:
                _classes.append(ac.__name__)
                found = True
        if 'suffix' in class_attribs:
            if isinstance(ac.suffix, dict):
                if affix_searched in ac.suffix.values():
                    _classes.append(ac.__name__)
                    found = True
            else:
                if affix_searched in ac.suffix:
                    _classes.append(ac.__name__)
                    found = True
        
        if not found:
            if ac.__name__ in ('AffParticipleAdjectivalActive',
                               'AffParticipleAdjectivalPassive'):
                endings = _get_participle_suffixes(ac)
                if affix_searched in endings:
                    _classes.append(ac.__name__)
                    found = True
  
    return _classes


def get_classes_by_process():
    """
    Get all processes that are listed in the classes.
    """
    _process = {'noprocessfound':[]}

    for ac in affixclasses:
        try:
            if ac.process not in _process.keys():
                _process[ac.process] = []
            else:
                _process[ac.process].append(ac.__name__)
        except AttributeError:
            _process['noprocessfound'].append(ac.__name__)
            #print ("No process for", ac.__name__)

    return _process
