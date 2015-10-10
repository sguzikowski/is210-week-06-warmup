#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Optional and required things."""


def process_data(data):
    """Does some math to provided data.

    Here, there would be paragraphs worth of text.
    Just this one time, there will be two lines worth of it.

    Args:
        data (int): Arg to be worked on.

    Returns:
        tuple: arguments' sum and average.

    Examples:

        >>> process_data([1, 2, 3])
        (6, 2.0)
    """
    RESULT = [0, 0]
    for x in data:
        RESULT[0] = RESULT[0] + x
    RESULT[1] = float(RESULT[0]/len(data))
    return tuple(RESULT)
