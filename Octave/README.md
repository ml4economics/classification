## GNU Octave
See [GNU Octave](https://www.gnu.org/software/octave/)

## Installation
Download and install from [GNU Octave Download](https://www.gnu.org/software/octave/download.html). 

This project is using version 5.1.0

## Octave in Jupyter Notebooks
An Octave kernel for Jupyter is provided by https://github.com/Calysto/octave_kernel

Create environment and install kernel
```
conda create --name octave python=3.7
conda activate octave
conda install jupyter
conda install -c conda-forge octave_kernel
```
Make sure the Octave CLI is on your path
```
set PATH=%PATH%;C:\Octave\Octave-5.1.0.0\mingw64\bin
```

Run Jupyter notebook
```
conda activate octave
jupyter notebook
```
