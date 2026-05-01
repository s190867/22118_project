#!/usr/bin/env python3

def load_file(filename):
    data = {}
    with open(filename) as f:
        next(f)  #skip header
        for line in f:
            parts = line.strip().split("\t")
            probe = parts[0]
            value = parts[7]  #Assay_Normalized_Signal is last column
            try:
                data[probe] = float(value)
            except:
                continue
    return data

