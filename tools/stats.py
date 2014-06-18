"""
Calculate project-wide stats.
"""

import sys
sys.path.append("../")

import text

def stats():
    """
    Calculate stats.
    """
    text.makewords.load_dictionaries()
    
