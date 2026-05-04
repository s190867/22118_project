#!/usr/bin/env python3

import matplotlib.pyplot as plt

#importing from pipeline and experiment scripts to run the plot script
from pipeline_v2 import load_data
from experiment_v1 import run_experiment

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
    
    data = load_data("data.txt")
    missing_percents = [0.05, 0.10, 0.15, 0.25, 0.30]
    k_values = [5, 6, 7, 8, 9, 10]
    
    results = run_experiment(data, missing_percents, k_values)
    
    #plot with matplotlib and view in its default viewer when running from terminal
    print("\nGenerating plot...")
    plot_results(results, k_values)
    print("Plot saved as 'knn_results.png'")