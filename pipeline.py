#!/usr/bin/env python3

import numpy


def load_data(filename):
    """
    Loads tab separated matrix data.
    Assumes first colum is ID, skips it.
    Converts NA to np.nan
    """
    data = numpy.genfromtxt(filename, delimiter="\t", skip_header=1, dtype=float, 
    missing_values="NA", filling_values=numpy.nan)
    return data