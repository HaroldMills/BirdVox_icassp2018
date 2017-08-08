import datetime
import h5py
import numpy as np
import os
import sys
import time

import localmodule


# Define constants.
n_thresholds = 100
# The array of upward thresholds is equal to
# f(t) = 1 + threshold_multiplier * (t**threshold_exponent)
# when the parameters threshold_multiplier and threshold_exponent
# are chosen such that:
# (1)    f(threshold_range_alpha*n_thresholds) = ad_hoc_threshold
# (2)    f(n_threshold) = ad_hoc_threshold**2
# In Old Bird, ad_hoc_threshold is equal to 2.0 for Thrush and 1.2 for Tseep.
threshold_range_alpha = 0.1
data_dir = localmodule.get_data_dir()
dataset_name = localmodule.get_dataset_name()
models_dir = localmodule.get_models_dir()
sample_rate = localmodule.get_sample_rate()
hop_duration = 0.02 # in seconds
hop_length = int(np.round(sample_rate * hop_duration))
args = sys.argv[1:]
unit_str = args[0]
odf_str = args[1]
threshold_id_start = int(args[2][:2])
threshold_id_stop = int(args[2][-2:])
threshold_id_range = range(threshold_id_start, threshold_id_stop)


# Print header.
start_time = int(time.time())
print(str(datetime.datetime.now()) + " Start.")
print("Running Old Bird onset detection functions (Thrush and Tseep) on " +
    dataset_name + ", " + unit_str + ".")
print('h5py version: {:s}.'.format(h5py.__version__))
print('numpy version: {:s}'.format(np.__version__))
print("")


# Load onset detection function.
oldbird_name = "_".join([dataset_name, "oldbird"])
oldbird_dir = os.path.join(data_dir, oldbird_name)
odf_path = os.path.join(oldbird_dir, unit_str + ".hdf5")
odf_file = h5py.File(odf_path, "r")
odf_dataset_key = "_".join([odf_str, "odf"])
odf = odf_file[odf_dataset_key]
odf_length = len(odf)


# Define arrays of thresholds.
odf_settings_key = "_".join([odf_str, "settings"])
odf_settings = odf_file[odf_settings_key]
ad_hoc_threshold = odf_settings["ratio_threshold"].value
ad_hoc_threshold = 1.2
threshold_multiplier = ad_hoc_threshold**2 - 1
threshold_exponent = \
    (np.log(ad_hoc_threshold-1) - np.log(threshold_multiplier)) /\
    np.log(threshold_range_alpha)
up_threshold_abcissa = np.arange(1, 1+n_thresholds) / n_thresholds
up_thresholds = 1 +\
    threshold_multiplier * up_threshold_abcissa**threshold_exponent
down_thresholds = 1.0 / up_thresholds


# Create directory for Old Bird in models_dir.
model_dir = os.path.join(models_dir, "Old Bird")
os.makedirs(model_dir, exist_ok=True)
out_unit_dir = os.path.join(model_dir, unit_str)
os.makedirs(out_unit_dir, exist_ok=True)
predictions_dir = os.path.join(out_unit_dir, "predictions")
os.makedirs(predictions_dir, exist_ok=True)


# Compute minimum and maximum clip length according to Old Bird heuristics.
min_clip_duration = odf_settings["min_duration"].value
min_clip_length = int(np.round(min_clip_duration * sample_rate))
max_clip_duration = odf_settings["max_duration"].value
max_clip_length = int(np.round(max_clip_duration * sample_rate))



# Print elapsed time.
print(str(datetime.datetime.now()) + " Finish.")
elapsed_time = time.time() - int(start_time)
elapsed_hours = int(elapsed_time / (60 * 60))
elapsed_minutes = int((elapsed_time % (60 * 60)) / 60)
elapsed_seconds = elapsed_time % 60.
elapsed_str = "{:>02}:{:>02}:{:>05.2f}".format(elapsed_hours,
                                               elapsed_minutes,
                                               elapsed_seconds)
print("Total elapsed time: " + elapsed_str + ".")
