#!/usr/bin/env python3

import numpy as np
import argparse

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
        usecols=range(1, 4),  #NOTE: skip probe_id, use only columns 1-3
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

#NOTE: added max_row = None as a default
def compute_rmse(original, imputed, missing_indices, max_row=None):
    """
    Compute RMSE only on values that have been removed.
    If max_row specified, compute only for rows < max_row
    """
    errors = []

    for i, j in zip(*missing_indices):
        
        #skip if past processed rows
        if max_row is not None and i >= max_row:
            continue
        
        errors.append((original[i, j] - imputed[i, j]) ** 2)
    
    #if no errors
    if len(errors) == 0:
        return np.nan
    
    return np.sqrt(np.mean(errors))


def pipeline():
    #load data
    data = load_data("data.txt")

    #introduce missing vAluees (10%)
    corrupted, missing_idx = introduce_missing(data, 0.1)

    #NOTE: debug lines, missing values beyond 300
    print(f"Missing indices range: rows {min(missing_idx[0])}-{max(missing_idx[0])}, cols {min(missing_idx[1])}-{max(missing_idx[1])}")
    print(f"Total missing values: {len(missing_idx[0])}")

    #takes a bit of time, print to confirm its running
    print("Starting KNN.....")

    #impute using k-NN
    imputed = knn_impute(corrupted, k=10)

    #evaluAte
    error = compute_rmse(data, imputed, missing_idx,  max_row=300)

    print("RMSE:", error)


#NOTE: added the entire argparse block below so can be run from command line with custom parameters instead of hard-coded
if __name__ == "__main__":

    #create parser object
    parser = argparse.ArgumentParser(description='k-NN imputation')

    parser.add_argument('-file', default='data.txt', help='Input file')   #take input file
    parser.add_argument('-k', type=int, default=10, help='Number of neighbors')   #take k value
    parser.add_argument('-missing', type=float, default=0.1, help='Missing percentage (0-1)')   #take missing percentage
    
    args = parser.parse_args()
    
    data = load_data(args.file)
    corrupted, missing_idx = introduce_missing(data, args.missing)   #call the introduce missing function
    
    print(f"Missing indices range: rows {min(missing_idx[0])}-{max(missing_idx[0])}")
    print(f"Total missing values: {len(missing_idx[0])}")
    print("Starting KNN...")
    
    imputed = knn_impute(corrupted, k=args.k)   #call impute function
    error = compute_rmse(data, imputed, missing_idx, max_row=300)   #call function to calculate RMSE
    
    print(f"RMSE: {error}")