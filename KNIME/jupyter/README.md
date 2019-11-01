
## KNIME and Jupyter Notebooks

Here's an example Jupyter notebook with an embedded KNIME workflow. However, the functionality for KNIME in Jupyter is a bit limited and 
requires a local KNIME installation. Also there's currently no https://mybinder.org/ support.

To run the notebook (unfortunately, there's no conda package for `knime` yet)

```
conda env create -f  py36_knime.yml
conda activate  py36_knime
pip install knime  
jupyter notebook
```

For more information checkout
* https://www.knime.com/blog/knime-and-jupyter
* https://pypi.org/project/knime/
