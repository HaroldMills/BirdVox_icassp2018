#!/bin/bash

#BATCH --job-name=028_T-0060_unit07
#SBATCH --nodes=1
#SBATCH --tasks-per-node=1
#SBATCH --cpus-per-task=1
#SBATCH --time=4:00:00
#SBATCH --mem=8GB
#SBATCH --gres=gpu:1
#SBATCH --output=../slurm/slurm_028_T-0060_unit07_%j.out

module purge

# The first argument is the name of the recording unit.
# The second argument is the duration of background.
python ../../../src/028_train-median-ntt-convnet.py 0060 unit07