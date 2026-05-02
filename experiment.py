
def run_experiment(data, missing_percentages, k_values):
    """
    Runs experiments with different k values and missing percentages
    """

    results = {}
    for percent in missing_percentages:
        percent_results = []

        #generate 1 corrupted dataset per %
        corrupted, missing_idx = introduce_missing(data, percent)

        for k in k_values:
            imputed = knn_impute(corrupted, k)   #NOTE: same corrupted dataset, change?
            error = compute_rmse(data, imputed, missing_idx)
            percent_results.append(error)

        results[percent] = percent_results
    return results