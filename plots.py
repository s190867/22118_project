#!/usr/bin/env python3

import matplotlib.pyplot as plt
import time

#importing from pipeline and experiment scripts to run the plot script
from pipeline import load_data
from experiment import run_experiment

def plot_results(results, k_values):
    """
    Plot RMSE vs k for different missing percentages.
    """

    for percent, errors in results.items():
        plt.plot(k_values, errors, marker='o', label=f"{int(percent*100)}% missing")

    plt.xlabel("k (number of neighbors)")
    plt.ylabel("RMSE")
    plt.title("k-NN Imputation Error")
    plt.legend()
    plt.grid()
    plt.savefig("knn_results.png", dpi=300, bbox_inches='tight')   #NOTE: added to save the resultant plots

    plt.show()

#call to run the plot function via the pipeline and experiment scripts
if __name__ == "__main__":

    print("Loading data and running experiment...")
    
    #setting parameters
    data = load_data("data.txt")
    missing_percentages = [0.05, 0.10, 0.15, 0.25, 0.30]
    k_values = [5, 6, 7, 8, 9, 10]

    start_time = time.time()   #NOTE: timing the experiment
    results = run_experiment(data, missing_percentages, k_values)
    end_time = time.time()   #NOTE: timing the experiment
    total_time = end_time - start_time   #NOTE: timing the experiment

    #NOTE: print timing info
    print(f"\nTotal runtime: {total_time:.1f} seconds ({total_time/60:.1f} minutes)")
    print(f"Rows processed: 1500")
    print(f"Average per configuration: {total_time/30:.1f} seconds")

    #NOTE: write results to file so can easily view them
    with open("results.txt", "w") as f:
        for percent, errors in results.items():
            f.write(f"{percent}: {errors}\n")
            
    #NOTE: plot with matplotlib and view in its default viewer when running from terminal
    print("\nGenerating plot...")
    plot_results(results, k_values)
    print("Plot saved as 'knn_results.png'")
