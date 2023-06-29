# Workload Classification using FBCSP on STEW Dataset

This repository contains a Python project that applies Filter Bank Common Spatial Pattern (FBCSP) and Support vector machine(SVM) to classify Electroencephalography (EEG) workload data. The EEG data comes from the Simultaneous Task EEG Workload (STEW) dataset. The code completes two-class classification with an accuracy rate of approximately 70%.

After installing the prerequisites and obtaining the dataset. First run stew.m to change the format of the raw stew file (from txt to mat).

Then, you can use the following command to run the main pipeline:
```
python mainPipeline.py
```

stew dataset link <a href="https://ieee-dataport.org/open-access/stew-simultaneous-task-eeg-workload-dataset">stew-simultaneous-task-eeg-workload-dataset</a>.

