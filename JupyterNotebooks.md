# Jupyter Notebooks
The easiest and recommended way to install Jupyter is using an [Anaconda Distribution](https://www.anaconda.com/distribution/). This project is using Anaconda 2019.07 - Python 3.7 version.

Anaconda comes with the [Conda Package Manager](https://docs.conda.io/en/latest/) to install kernels for other languages like R. On Windows all Anaconda/Conda commands should be run from the _Anaconda Prompt_ that comes with the Anaconda installation.

It is recommended to set up a separate environment for each kernel (see [Managing Conda Environments](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#)):

### Create Environment
```
conda env create -f environment.yml
```
### Configure Environment (Optional) 
E.g. to start in the current directory
1. copy the folder `config/etc` to the Anaconda environment, i.e. `<Anaconda home>\envs\classification`
2. update the path in etc/conda/activate.d/profile.bat

### Run Jupyter Notebook
```
conda activate classification
jupyter notebook
```

## Tips and Tricks

### Setting PATH variables in Conda environments
See [Conda Documentation](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#windows). 

In envs\classification\etc\conda\activate.d\env_vars.bat
```
set OLD_PATH=%PATH%
set PATH=%PATH%;C:\Octave\Octave-5.1.0.0\mingw64\bin
```
In envs\classification\etc\conda\deactivate.d\env_vars.bat
```
set PATH=%OLD_PATH%
set OLD_PATH=
```

### Setting working directory in Conda environments
In envs\classification\etc\conda\activate.d\profile.bat
```
C:
cd \GitHub\ml4economics\classification
```
