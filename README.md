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

```sh
python3 ./2_sprectrum_of_ALPS_analysis.py
```
## Results
All subjects' 1000 ALPS values would be recorded in the results.csv

## References
* Tatekawa H, Matsushita S, Ueda D, et al. Improved reproducibility of diffusion tensor image analysis along the perivascular space (DTI-ALPS) index: an analysis of reorientation technique of the OASIS-3 dataset. Japanese Journal of Radiology. 2023;41(4):393-400.
