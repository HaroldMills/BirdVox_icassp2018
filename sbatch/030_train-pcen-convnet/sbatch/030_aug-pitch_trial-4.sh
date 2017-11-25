# This shell script executes Slurm jobs for training
# Justin Salamon's ICASSP 2017 convolutional neural network
# on BirdVox-70k with PCEN input instead of
# log-mel-spectrogram (logmelspec) input.
# Trial ID: 4.
# Augmentation kind: pitch.

sbatch 030_aug-pitch_unit01_trial-4.sbatch
sbatch 030_aug-pitch_unit02_trial-4.sbatch
sbatch 030_aug-pitch_unit03_trial-4.sbatch
sbatch 030_aug-pitch_unit05_trial-4.sbatch
sbatch 030_aug-pitch_unit07_trial-4.sbatch
sbatch 030_aug-pitch_unit10_trial-4.sbatch