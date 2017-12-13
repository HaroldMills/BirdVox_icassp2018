# This shell script executes Slurm jobs for thresholding
# Justin Salamon's ICASSP 2017 predictions of convolutional
# neural network on BirdVox-70k full audio
# with PCEN input.
# Augmentation kind: all-but-noise.
# Test unit: unit05.
# Trial ID: 5.

sbatch 034_aug-all-but-noise_test-unit05_predict-unit05_trial-5.sbatch
sbatch 034_aug-all-but-noise_test-unit05_predict-unit02_trial-5.sbatch
sbatch 034_aug-all-but-noise_test-unit05_predict-unit03_trial-5.sbatch