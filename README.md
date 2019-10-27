# Implementations of Classification Algorithms

This repository demonstrates the application of different Machine Learning tools on a real world classification problem. The data being used the [Bank Marketing Data Set](https://archive.ics.uci.edu/ml/datasets/bank+marketing) from the [UC Irvine Machine Learning Repository](https://archive.ics.uci.edu/ml/index.php).

The tools that were applied to the data are
* [Weka](WEKA)
* [KNIME](KNIME)
* [R](R)
* [Python with scikit-learn](python)
* [TensorFlow](tensorflow)

If you want to run the algorithms with Weka or KNIME, you will need a local installation of the software. For the other tools, several example implementations are available as [Jupyter Notebooks](https://jupyter.org/). You **do not need any installation** if you use the links below. They will create a Jupyter environment on the [![Binder](/binder.svg)](https://mybinder.org) [Binder](https://mybinder.org) cloud service and you can access the notebooks through your browser. 
If you insist on running Jupyter locally, you'll need to install a few things. [Run Jupyter Notebooks locally](JupyterNotebooks.md) has more information on that.

## Example Notebooks

### Python (Scikit-Learn)
* Data Exploration : [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/ml4economics/classification/master?filepath=python%2FDataExploration.ipynb)
* Logistic Regression : [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/ml4economics/classification/master?filepath=python%2FLogisticRegression.ipynb)

### R
* Logistic Regression : [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/ml4economics/classification/master?filepath=R%2FLogisticRegression.ipynb)

### Tensorflow
* Logistic Regression TF : [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/ml4economics/classification/master?filepath=tensorflow%2FLogisticRegression.ipynb)
* Logistic Regression MNIST : [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/ml4economics/classification/master?filepath=tensorflow%2FLogisticRegressionMNIST.ipynb)
* Neural Network (Keras) : [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/ml4economics/classification/master?filepath=tensorflow%2FNeuralNetwork.ipynb)

### GNU Octave
Here's one final example that shows how an implementation of logistic regression would look like in [GNU Octave](https://www.gnu.org/software/octave/). Octave is the tool being used highly popular [Stanford Machine Learning Course](https://www.coursera.org/learn/machine-learning)
* Logistic Regression : [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/ml4economics/classification/master?filepath=octave%2FLogisticRegression.ipynb)
