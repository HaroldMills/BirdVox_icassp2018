# This shell script executes Slurm jobs for training
# add-NTT convolutional neural network
# on BirdVox-70k with PCEN input.
# Trial ID: 0.
# Augmentation kind: all.

sbatch 054_aug-all_unit01_trial-0.sbatch
sbatch 054_aug-all_unit02_trial-0.sbatch
sbatch 054_aug-all_unit03_trial-0.sbatch
sbatch 054_aug-all_unit05_trial-0.sbatch
sbatch 054_aug-all_unit07_trial-0.sbatch
sbatch 054_aug-all_unit10_trial-0.sbatch
