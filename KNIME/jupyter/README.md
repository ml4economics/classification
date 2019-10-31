
## KNIME and Jupyter Notebooks

You can also embed KNIME workflows in Jupyter notebooks. However, the functionality is a bit limited and 
requires a local KNIME installation. Also there's currently no https://mybinder.org/ support.

To run the notebook
* 
```
conda env create -f  py36_knime.yml
conda activate  py36_knime
pip install knime  # unfortunately, there's no conda package yet
jupyter notebook
```

For more information checkout
* https://www.knime.com/blog/knime-and-jupyter
* https://pypi.org/project/knime/
