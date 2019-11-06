# tidyverse includes dplyr, tidyr, readr, ggplot2
library(tidyverse)
library(caret)
library(OneR)

options(warn=-1)

data_dir_default = "../../data/"
data_sets = c("bank-full", "bank-10percent", "bank-balanced")

read_data <- function(data_set, data_dir = data_dir_default) {
  data_set <- paste(data_dir, data_set, ".csv", sep='')
  read.csv(data_set)
}

partition_data <- function(data, prop = 0.8) {
  set.seed(4711)
  n <- nrow(data)
  n_train <- round(0.8 * n) 
  partition <- sample(1:n, n_train)
  
  first <-  data[partition,]
  second  <-  data[-partition,]
  
  list(first, second)
}

predicted <- function(model, data) {
  predicted_class = predict(object = model,  
                            newdata = data,
                            type = "class")  
  
  predicted_probs = predict(object = model,  
                            newdata = data,   
                            type = "prob")
  predicted_probs_yes <- predicted_probs[,"yes"]
  
  return (list(predicted_class, predicted_probs_yes))
}

build_and_evaluate_model <- function(data_set, classificator) {
  data <- read_data(data_set)
  partitions <- partition_data(data)
  train.df <- partitions[[1]]
  test.df  <- partitions[[2]]
  model <- classificator(train.df)
  summary(model)
  
  predicted_class_probs <- predicted(model, test.df)
  predict.class <- predicted_class_probs[[1]]
  predict.probs.yes <- predicted_class_probs[[2]]
  
  # this is a bit of a hack - the predictor creates 'UNSEEN' values
  # because it's working with 'cut' and has problems with float intervals
  # The workaround is to filter out the elements where predict returns UNSEEN
  retain <- predict.class != "UNSEEN"
  predict.class.filtered <- droplevels(predict.class[retain])
  test.df.filtered <- test.df$y[retain]
  
  evaluation <- confusionMatrix(data = predict.class.filtered,       
                                reference = test.df.filtered)
  
  accuracy <- evaluation$overall["Accuracy"]
  
  pred <- prediction(predict.probs.yes, test.df$y)
  auc_perf <- performance(pred,"auc")
  auc <- auc_perf@y.values[[1]]
  
  cat("Data : ", 
      data_set,
      "\t - accuracy : ", format(100*accuracy,digits = 4), 
      "\t - AUC : ", auc, 
      "\n")
  flush.console()
}

for (data_set in data_sets) {
  build_and_evaluate_model(data_set, OneR)
}

