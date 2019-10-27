# Classification with Weka

This folder contains classifications models for [Weka (Waikato Environment for Knowledge Analysis)](https://www.cs.waikato.ac.nz/ml/index.html) created for the [Bank Marketing Data Set from UCI](https://archive.ics.uci.edu/ml/datasets/bank+marketing).

Weka is an easy-to-use tool for Machine Learning. To get started on Weka, I recommend to join the free [Data Mining with Weka Online Course](https://www.futurelearn.com/courses/data-mining-with-weka). It's quite compact and easy to follow.

To apply these models on the bank dataset
* download and install Weka
* start Weka and select `Workbench`
* go to the `Preprocessing` view and load the data with `Open File`. The complete dataset is *bank-full.arff*. For LDA you should use *bank-full.dummy-encoded.arff*.
* go to the `Classify` view and load a model (right-click in the `Result list` window)
* activate the model : right click the load entry in the `Result list` and select `Re-apply this model's configuration`
* set the `Test options` to `Use training set` and apply the model with `Start`. If you select `Percentage split`, the model will be recreated using 80% of the data and evaluated on the remaining 20%.
