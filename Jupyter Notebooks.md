# Implementations of Classification Algorithms

Here are the tools being used
* [KNIME](https://www.knime.com/)
* [Weka (Waikato Environment for Knowledge Analysis)](https://www.cs.waikato.ac.nz/ml/index.html)
* [R](https://cran.r-project.org/)
* [Python with scikit-learn](https://scikit-learn.org)
* [GNU Octave](Octave)

## Jupyter Notebooks
Most examples are available as [Jupyter Notebooks](https://jupyter.org/). The easiest and recommended way to install Jupyter is using an [Anaconda Distribution](https://www.anaconda.com/distribution/). This project is using Anaconda 2019.07 - Python 3.7 version.

Anaconda comes with the [Conda Package Manager](https://docs.conda.io/en/latest/) to install kernels for other languages like R. On Windows all Anaconda/Conda commands should be run from the _Anaconda Prompt_ that comes with Anaconda installation.

It is recommended to set up a separate environment for each kernel (see [Managing Conda Environments](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#)):
```
conda create --name my_env python=3.7
conda activate my_env
conda install jupyter
```
You can then switch between environments by
```
conda activate my_env
conda deactivate
```
## Tips and Tricks
### Setting PATH variables in Conda environments
See [Conda Documentation](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#windows). 

In activate.d\env_vars.bat
```
set OLD_PATH=%PATH%
set PATH=%PATH%;C:\Octave\Octave-5.1.0.0\mingw64\bin
```
In deactivate.d\env_vars.bat
```
set PATH=%OLD_PATH%
set OLD_PATH=
```
