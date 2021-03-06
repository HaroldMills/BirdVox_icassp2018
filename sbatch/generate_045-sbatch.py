import numpy as np
import os
import sys

sys.path.append("../src")
import localmodule


# Define constants.
aug_kinds = ["all", "all-but-noise", "none"]
units = localmodule.get_units()
script_name = "045_evaluate-add-convnet-full-audio.py"
script_path = os.path.join("..", "..", "..", "src", script_name)
n_trials = 10


# Define thresholds.
icassp_thresholds = 1.0 - np.linspace(0.0, 1.0, 201)[:-1]
n_thresholds = len(icassp_thresholds)


# Create folder.
script_dir = script_name[:-3]
os.makedirs(script_dir, exist_ok=True)
sbatch_dir = os.path.join(script_dir, "sbatch")
os.makedirs(sbatch_dir, exist_ok=True)
slurm_dir = os.path.join(script_dir, "slurm")
os.makedirs(slurm_dir, exist_ok=True)


# Loop over kinds of data augmentation.
for aug_kind_str in aug_kinds:

    # Loop over test units.
    for test_unit_str in units:

        # Retrieve fold such that unit_str is in the test set.
        folds = localmodule.fold_units()
        fold = [f for f in folds if test_unit_str in f[0]][0]
        test_units = fold[0]
        training_units = fold[1]
        validation_units = fold[2]
        predict_units = test_units + validation_units

        # Loop over prediction units.
        for predict_unit_str in predict_units:

            # Loop over trials.
            for trial_id in range(n_trials):

                # Define job name.
                job_name = "_".join([
                    script_name[:3],
                    "aug-" + aug_kind_str,
                    "test-" + test_unit_str,
                    "predict-" + predict_unit_str,
                    "trial-" + str(trial_id)])

                # Define file path.
                file_name = job_name + ".sbatch"
                file_path = os.path.join(sbatch_dir, file_name)

                # Define script path with arguments.
                script_list = [
                    script_path, aug_kind_str,
                    test_unit_str, predict_unit_str,
                    str(trial_id)]
                script_path_with_args = " ".join(script_list)

                # Define slurm path.
                slurm_path = os.path.join("..", "slurm",
                    "slurm_" + job_name + "_%j.out")

                # Write sbatch file.
                with open(file_path, "w") as f:
                    f.write("#!/bin/bash\n")
                    f.write("\n")
                    f.write("#BATCH --job-name=" + job_name + "\n")
                    f.write("#SBATCH --nodes=1\n")
                    f.write("#SBATCH --tasks-per-node=1\n")
                    f.write("#SBATCH --cpus-per-task=1\n")
                    f.write("#SBATCH --time=24:00:00\n")
                    f.write("#SBATCH --mem=1GB\n")
                    f.write("#SBATCH --output=" + slurm_path + "\n")
                    f.write("\n")
                    f.write("module purge\n")
                    f.write("\n")
                    f.write("# The first argument is the kind of data augmentation.\n")
                    f.write("# The second argument is the test unit.\n")
                    f.write("# The third argument is the prediction unit.\n")
                    f.write("# The fourth argument is the trial index.\n")
                    f.write("python " + script_path_with_args)
