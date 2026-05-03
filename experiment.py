
#!/usr/bin/env python3

from pipeline_v6 import load_data, introduce_missing, knn_impute, compute_rmse
import numpy as np

def run_experiment(data, missing_percentages, k_values):
    """
    Runs experiments with different k values and missing percentages
    """

    results = {}
    for percent in missing_percentages:
        percent_results = []

        #generate 1 corrupted dataset per percentage
        corrupted, missing_idx = introduce_missing(data, percent)

        for k in k_values:
            imputed = knn_impute(corrupted, k)   #NOTE: same corrupted dataset, change?
            error = compute_rmse(data, imputed, missing_idx)
            percent_results.append(error)

        results[percent] = percent_results
    return results


#NOTE: now call the functions with the set parameters, use only when running the script as stand-alone
if __name__ == "__main__":

    print("Loading data...")
    data = load_data("data.txt")
    print(f"Data shape: {data.shape}")
    
    #define test parameters
    missing_percentages = [0.05, 0.10]  #just 2 for a quick test
    k_values = [5, 10]  #2 for quick test
    
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