# Implementations of Classification Algorithms

This repository demonstrates the application of different Machine Learning tools on a real world classification problem. The data being used is the [Bank Marketing Data Set](https://archive.ics.uci.edu/ml/datasets/bank+marketing) from the [UC Irvine Machine Learning Repository](https://archive.ics.uci.edu/ml/index.php).

The tools that were applied to the data are
* [Weka](WEKA)
* [KNIME](KNIME)
* [R](R)
* [Python with scikit-learn](python)
* [TensorFlow](tensorflow)

If you want to run the algorithms with Weka or KNIME, you will need a local installation of the software. For the other tools, several example implementations are available as [Jupyter Notebooks](https://jupyter.org/). 

You can run the notebooks in your browser **without any installation** if you use the links below. They will access a Jupyter environment on the [![Binder](/binder.png)](https://mybinder.org) cloud service. If this repository has changed recently, *mybinder.org* will have to rebuild a Docker image for this environment which might take a while. Once the Docker image is available, the environment will be up in less than a minute.

If you insist on running Jupyter locally, you'll need to install a few things. [Run Jupyter Notebooks locally](JupyterNotebooks.md) has more information on that.

## Example Notebooks

### R
* Data Exploration : [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/ml4economics/classification/master?filepath=R%2FDataExplorationWithR.ipynb)
* Logistic Regression : [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/ml4economics/classification/master?filepath=R%2FLogisticRegressionWithR.ipynb)
* Decision Trees : [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/ml4economics/classification/master?filepath=R%2FDecisionTreeWithR.ipynb)
* Random Forest : [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/ml4economics/classification/master?filepath=R%2FRandomForestWithR.ipynb)

### Python (Scikit-Learn)
* Data Exploration : [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/ml4economics/classification/master?filepath=python%2FDataExplorationWithPython.ipynb)
* Classification Algorithms : [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/ml4economics/classification/master?filepath=python%2FClassificationWithPython.ipynb)

### Tensorflow
* Logistic Regression with TensorFlow : [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/ml4economics/classification/master?filepath=tensorflow%2FLogisticRegression.ipynb)
* Classification by a Neural Network implemented with Keras : [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/ml4economics/classification/master?filepath=tensorflow%2FNeuralNetwork.ipynb)
* Logistic Regression on a standard benchmark, the MNIST dataset : [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/ml4economics/classification/master?filepath=tensorflow%2FLogisticRegressionMNIST.ipynb)

### GNU Octave
Here's one final example that shows how an implementation of logistic regression would look like in [GNU Octave](https://www.gnu.org/software/octave/). Octave is the tool being used in the highly popular [Stanford Machine Learning Course](https://www.coursera.org/learn/machine-learning)
* Logistic Regression : [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/ml4economics/classification/master?filepath=octave%2FLogisticRegression.ipynb)

## Binder Configuration Files

This repository uses the following [Binder Configuration Files](https://mybinder.readthedocs.io/en/latest/using/config_files.html)
1. environment.yml : the Conda environment for the notebooks
2. runtime.txt : defines the R runtime version
3. install.R : specifies the required R packages
4. apt.txt : specifies Linux packages for Octave (see also https://github.com/binder-examples/octave)
5. postBuild : activate Jupyter TOC extension

Testing webhook
