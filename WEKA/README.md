# WEKA Models for Bank Dataset

This folder contains classifications models for [Weka (Waikato Environment for Knowledge Analysis)](https://www.cs.waikato.ac.nz/ml/index.html) created for the [Bank Marketing Data Set from UCI](https://archive.ics.uci.edu/ml/datasets/bank+marketing).

Weka is an easy-to-use tool for Machine Learning. To get started on Weka, I recommend to join the free [Data Mining with Weka Online Course](https://www.futurelearn.com/courses/data-mining-with-weka). It's quite compact and easy to follow.

To apply these models on the bank dataset
* Download and install Weka
* Start Weka and select `Workbench`
* Go to the `Preprocessing` view and load the data with `Open File`. The complete dataset is `bank-full.arff`. For LDA you should use `bank-full.dummy-encoded.arff`
* Go to the `Classify` view and load a model (right-click in the `Result list` window)
* Set the `Test options` to `Use training set` and apply the model with `Start`. If you select `Percentage split`, the model will be recreated using 80% of the data and evaluated on the remaining 20%.
