[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
# Spectrum-of-DTI-ALPS
This repo accompanies the manuscript "Subtle Glymphatic Dysfunction as a Novel Biomarker for Staging and Predicting Cognitive Impairment".

## Requirements
For DTI preprocessing in Shell
* MRtrix3
* FSL
* AFNI
* CUDA

For Auto ALPS Calculation and QC in Python
* nibabel
* numpy
* PIL
* csv

## How to use
DTI preprocessing for each subject (about 10-30 minutes for single subject, parallel run is reconmmeded)
```sh
./1_DTI_preprocessing.sh
```
Calculating 1000 ALPS values for each subject (about 5 minutes for single subject)
```sh
python3 ./2_sprectrum_of_ALPS_analysis.py
```
## Results
The ALPS values for all 1000 subjects will be recorded in the results.csv file, from which features such as the mean and variance can be extracted from the spectrum.
