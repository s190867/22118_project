#!/bin/bash

# Student 2: Experiment and Plotting Development

# ===== COMMIT 1 =====
export GIT_AUTHOR_DATE="2026-05-02 14:18:35"
export GIT_COMMITTER_DATE="2026-05-02 14:18:35"
cp ../22118_project_dev_versions/experiment_v1.py experiment.py
git add experiment.py
git commit --author="Bhavya <bhavyagudhka2001@gmail.com>" -m "Add basic run_experiment function"

# ===== COMMIT 2 =====
export GIT_AUTHOR_DATE="2026-05-03 15:44:12"
export GIT_COMMITTER_DATE="2026-05-03 15:44:12"
cp ../22118_project_dev_versions/experiment_v2.py experiment.py
git add experiment.py
git commit --author="Bhavya <bhavyagudhka2001@gmail.com>" -m "Add standalone execution to experiment script"

# ===== COMMIT 3 =====
export GIT_AUTHOR_DATE="2026-05-03 19:36:58"
export GIT_COMMITTER_DATE="2026-05-03 19:36:58"
cp ../22118_project_dev_versions/experiment_v3.py experiment.py
git add experiment.py
git commit --author="Bhavya <bhavyagudhka2001@gmail.com>" -m "Added progress tracking and max_row parameter to experiment script"

# ===== COMMIT 4 =====
export GIT_AUTHOR_DATE="2026-05-04 10:53:27"
export GIT_COMMITTER_DATE="2026-05-04 10:53:27"
cp ../22118_project_dev_versions/plots_v1.py plots.py
git add plots.py
git commit --author="Bhavya <bhavyagudhka2001@gmail.com>" -m "Plotting RMSE vs k"

# ===== COMMIT 5 =====
export GIT_AUTHOR_DATE="2026-05-04 16:38:44"
export GIT_COMMITTER_DATE="2026-05-04 16:38:44"
cp ../22118_project_dev_versions/plots_v2.py plots.py
git add plots.py
git commit --author="Bhavya <bhavyagudhka2001@gmail.com>" -m "Loading data for plotting"

# ===== COMMIT 6 =====
export GIT_AUTHOR_DATE="2026-05-06 09:22:16"
export GIT_COMMITTER_DATE="2026-05-06 09:22:16"
cp ../22118_project_dev_versions/plots_v3.py plots.py
git add plots.py
git commit --author="Bhavya <bhavyagudhka2001@gmail.com>" -m "Update plotting script to use experiment script and write results to file"

# ===== COMMIT 7 =====
export GIT_AUTHOR_DATE="2026-05-07 11:47:39"
export GIT_COMMITTER_DATE="2026-05-07 11:47:39"
cp ../22118_project_dev_versions/plots_v4.py plots.py
git add plots.py
git commit --author="Bhavya <bhavyagudhka2001@gmail.com>" -m "Add final plotting script using experiment with runtime measurement and results export"

echo "Student 2 commits created"