# Classification with KNIME

[KNIME (Konstanz Information Miner)](https://www.knime.com/) is a comprehensive and free data mining tool. It's the perfect tool if you want to run through a full data mining process including exploration of data, preprocessing and building a classification model.

This folder contains several workflows that demonstrate the usage of different classification algorithms on the [Bank Marketing Data Set from UCI](https://archive.ics.uci.edu/ml/datasets/bank+marketing).

To use these models
* download and install the `KNIME Analytics Platform for Windows` from the [KNIME Download Site](https://www.knime.com/downloads/download-knime)
* start KNIME and import a workflow (`File` -> `Import Workflow`, select `Root Directory`)
* activate the workflow and execute it
* to see the results of a workflow node, right click and select one of the results option. For instance, there's an *Accuracy Statistics* in the context menu of the *Score* node or an *Image* in the *ROC Curve* node.

The workflows as stored here are not executed. That means the model will be built when you first execute the entire workflow.

## KNIME and Jupyter Notebooks

You can also embed KNIME workflows in Jupyter notebooks. Check out https://www.knime.com/blog/knime-and-jupyter.
