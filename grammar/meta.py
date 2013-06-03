"""
Meta classes.
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


import warnings

class MAffix:
    """
    Meta object for affixes.
    Each class from grammar.affix inherits from this meta
    class.
    """
   
    ATTRIBUTES = [
    'altform', 'blendswith', 'condition',
    'declension', 'ending', 'exception',
    'gender', 'infix', 'place', 'plural',
    'singular', 'subtype', 'type', 'voice',
    'process', 'person']
    

    def __init__(self):
        """
        Make instance of MAffix() class.
        """
        pass
        

    def _elements(self):
        """
        Attribute True/False for each element.
        """
        class_items = dir(self)
        for i in self.ATTRIBUTES:
            if i in class_items:
                truefalse = True
            else:
                truefalse = False
            self.__dict__['has_%s' % i] = truefalse


    def has_affix(self, item):
        """
        Return true if class has item.
        """
        # Variable proper_affixes and other chacks in this
        # part are done so all base classes could be
        # checked properly.
        proper_affixes = None
        affix_type = False
        # NOUNS AND ADJECTIVES / DECLENSION ===================
        if self.pos in ('MNoun', 'MAdjective'):
                if self.process == 'declension':
                    warnings.warn("Nominal check doesn't include infixes in derivation.")
                    if 'singular' in dir(self):
                        proper_affixes = self.singular
                    else:
                        proper_affixes = self.plural
                        affix_type = 'suffix'
        # DERIVATION ===================
                if self.process == 'derivation':
                    if self.place == 'end':
                        proper_affixes = self.ending
                        affix_type = 'suffix'
                    if self.place == 'start':
                        proper_affixes = self.beginning
                        affix_type = 'prexif'
        # COMPARATION ===================
                if self.process == 'gradation':
                    pass
        # Variable proper_affixes always must have
        # some value.
        if not proper_affixes:
            raise ValueError("proper_affixes must have value.")
        # Finally, return True if the item is in proper_affixes
        # The second item is affix type.
        has_affix = item in proper_affixes
        return(has_affix, affix_type)
                
            

class MVerb:
    """
    Meta class for verbs.
    """
    def __init__(self):
        pass
