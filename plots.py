import matplotlib.pyplot as plt


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

    plt.show()