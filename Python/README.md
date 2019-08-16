## Jupyter Notebooks

### Create Environment
```
conda env create -f environment.yml
```
### (Optional) Configure Environment 
E.g. to start in the current directory
1. set the environment variable `CLASSIFICATION_ROOT` to point to this repository's root location
2. copy the folder `config/etc` to the Anaconda environment, i.e. `<Anaconda home>\envs\sklearn`

### Run Jupyter Notebook
```
conda activate sklearn
jupyter notebook
```
