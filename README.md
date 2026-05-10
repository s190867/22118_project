# 22118 Project README

The goal of the project is to evaluate how accurately any missing values can be reconstructed
under different conditions, such as the proportion of missing data. The performance of the
method is assessed by removing known values from a complete dataset, estimating them via the
k-NN algorithm, and then comparing these estimates to the original values in the dataset. 
This project implements the python, unix and GitHub concepts learned throughout the 22118 course. 

# k-NN Imputation for Microarray Data

Implementation of k-nearest neighbor algorithm for imputing missing values in gene expression data (scripts were written for microarrays particularly).

# Requirements

The below versions were used to run the scripts during development but earlier versions will likely support functionality as well:

- Python 3.13.9
- NumPy 2.3.5
- Matplotlib 3.10.6

# Installation

pip install numpy matplotlib

# Usage

1. Preprocess Data

python preprocess.py

Converts raw microarray files to data.txt.

2. Run Single Test

python pipeline.py -file data.txt -k 10 -missing 0.1

Arguments:
- -k: Number of neighbors (default: 10)
- -missing: Percentage missing 0-1 (default: 0.1)

3. Run Full Experiment

python experiment.py

Tests multiple k values and missing percentages. Edit parameters in script.

4. Generate Plots

python plots.py

Runs experiments and creates knn_results.png and results.txt

5. Run Tests

python test.py

Validates core functions.

# Output Files

- data.txt - Preprocessed data
- knn_results.png - RMSE plot
- results.txt - Numerical results

# Project Structure

preprocessing.py  # Data preparation
pipeline.py       # Core k-NN functions
experiment.py     # Parameter sweep
plot.py           # Visualization
test.py           # Unit tests
data.txt          # Input data
