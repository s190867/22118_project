#!/usr/bin/env python3

import numpy as np

def load_data(filename):
    """
    Loads tab-separated matrix data.
    Assumes first colum is ID, skips it.
    Converts NA to np.nan.
    """
    data = np.genfromtxt(
        filename,
        delimiter="\t",
        skip_header=1,
        dtype=float,
        missing_values="NA",
        filling_values=np.nan
    )

    return data


def introduce_missing(data, percent):
    """
    Randomly replace a percentage of values with np.nan.
    Returns modified data and indices of removed values.
    """
    if not (0 < percent < 1):
        raise ValueError("percent must be between 0 and 1")

    #NOTE: hard-coded
    np.random.seed(42)

    data_copy = data.copy()
    rows, cols = data.shape
    total = rows * cols
    n_missing = int(total * percent)

    #selected positions at random
    flat_indices = np.random.choice(total, n_missing, replace=False)
    row_indices = flat_indices // cols
    col_indices = flat_indices % cols
    
    data_copy[row_indices, col_indices] = np.nan

    return data_copy, (row_indices, col_indices)

#NOTE: new function, distance, 
def distance(a, b):
    """
    Euclidean distance ignores NAN values
    """
    
    sum_sq = 0
    count = 0
    
    for i in range(len(a)):
        if not np.isnan(a[i]) and not np.isnan(b[i]):
            sum_sq += (a[i] - b[i]) ** 2
            count += 1
    
    if count == 0:
        return np.inf
    
    return np.sqrt(sum_sq)




def knn_impute(data, k):
    """
    Imputes missing values using k-nearest neighbors,
    """
    if not isinstance(k, int) or k <= 0:
        raise ValueError("k must be a positive integer")

    imputed = data.copy()
    rows, cols = data.shape

    for i in range(rows):

        if i == 300:
            break

        #progress print every 50 rows
        #process is quadratic, takes a long time
        if i % 50 == 0:
            print(f"Row {i}/{rows}")

        for j in range(cols):

            if np.isnan(data[i, j]):

                distances = []

                #find all valid rows for this column
                for r in range(rows):
                    if r != i:  #skip self
                        if not np.isnan(data[r, j]):  #this row has a value in column j
                            d = distance(data[i], data[r])
                            distances.append((d, data[r, j]))
    
                #sort by distance (smallest first)
                distances.sort(key=lambda x: x[0])
                
                #take k nearest
                neighbors = distances[:k]
                
                ##impute value
                if len(neighbors) == 0:

                    #fallback: use column average
                    col_sum = 0
                    col_count = 0
                    for row in range(rows):
                        if not np.isnan(data[row, j]):
                            col_sum += data[row, j]
                            col_count += 1
                    if col_count > 0:
                        imputed[i, j] = col_sum / col_count
                    else:
                        imputed[i, j] = 0  #or keep as nan

                else:
                    #average the neighbor values
                    total = 0
                    for dist, val in neighbors:
                        total += val
                    imputed[i, j] = total / len(neighbors)

    return imputed