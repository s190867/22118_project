#!/usr/bin/env python3

import numpy as np
from pipeline import load_data, introduce_missing, knn_impute, compute_rmse

def run_experiment(data, missing_percentages, k_values):
    """
    Runs experiments with different k values and missing percentages    
    """

    results = {}

    for percent in missing_percentages:
        percent_results = []

        #Generate 1 corrupted dataset per percentage
        corrupted, missing_idx = introduce_missing(data, percent)

        #now call the functions from the pipeline script
        for k in k_values:

            print(f"  k={k}...", end=" ", flush=True)

            imputed = knn_impute(corrupted, k)   #NOTE: same corrupted dataset, change?
            error = compute_rmse(data, imputed, missing_idx, max_row=1500)
            percent_results.append(error)

            print(f"RMSE={error:.3f}")

        results[percent] = percent_results

    return results

#now call the functions with the set parameters, use only when running the experiment script stand-alon
if __name__ == "__main__":

    print("Loading data...")
    data = load_data("data.txt")
    print(f"Data shape: {data.shape}")
    
    #define test parameters
    missing_percentages = [0.05, 0.10, 0.15, 0.20, 0.25]
    k_values = [3, 5, 10, 15, 20]
    
    print("\nStarting experiments...")
    
    #run experiment
    results = run_experiment(data, missing_percentages, k_values)
    
    #print results
    print("\n" + "="*50)
    print("RESULTS")
    print("="*50)

    for percent in missing_percentages:
        print(f"\n{int(percent*100)}% missing:")
        error_list = results[percent]
        
        for i in range(len(k_values)):
            k = k_values[i]
            error = error_list[i]
            print(f"  k={k}: RMSE={error:.3f}")
