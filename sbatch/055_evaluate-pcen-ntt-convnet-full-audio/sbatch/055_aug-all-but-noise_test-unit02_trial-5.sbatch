#!/bin/bash

#BATCH --job-name=055_aug-all-but-noise_test-unit02_trial-5
#SBATCH --nodes=1
#SBATCH --tasks-per-node=1
#SBATCH --cpus-per-task=1
#SBATCH --time=24:00:00
#SBATCH --mem=1GB
#SBATCH --output=../slurm/slurm_055_aug-all-but-noise_test-unit02_trial-5_%j.out

module purge

# The argument is the kind of data augmentation.
python ../../../src/055_evaluate-pcen-ntt-convnet-full-audio.py all-but-noise unit02 5