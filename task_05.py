#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Optional and required things."""

def flip_keys(to_flip):
    """Flips what is provided by the user

    There would be paragraphs upon paragraphs of text here, should they
    be required, but they aren't so this will simply have two lines.

    Args:
        to_flip (list): user-provided list to be worked on

    Returns:
        tuple: flipped arguments

    Examples:
        >>> LIST = [(1, 2, 3), 'abc']
        >>> NEW = flip_keys(LIST)
        >>> LIST is NEW
        True
        >>> print LIST
        [(3, 2, 1), 'cba']
    """
    for x in range(len(to_flip)):
        to_flip[x] = to_flip[x][::-1]
    return (to_flip)
