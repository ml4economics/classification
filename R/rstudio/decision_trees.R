# tidyverse includes dplyr, tidyr, readr, ggplot2
library(tidyverse)
library(rpart)
library(rpart.plot)
library(caret)
library(ROCR)
library(Metrics)

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

#------------------------------------------
#         load data
#------------------------------------------
bank_data <- read_data(data_sets[1])
partitions <- partition_data(bank_data)
train.df <- partitions[[1]]
test.df  <- partitions[[2]]

#------------------------------------------
#        textual data exploration
#------------------------------------------
sprintf("# rows: %d - # columns: %d", nrow(bank_data), ncol(bank_data))
summary(bank_data)

#------------------------------------------
#        partition data
#------------------------------------------
partitions <- partition_data(bank_data)
train.df <- partitions[[1]]
test.df  <- partitions[[2]]

dim(train.df)
dim(test.df)

#------------------------------------------
#        model
#------------------------------------------
cp <- 0.01
bank_model <- rpart(formula = y ~ ., 
                    data = train.df, 
                    method = "class",
                    control = rpart.control(minsplit = 2, cp = cp))

print(bank_model)

rpart.plot(bank_model, type=5, extra = 0)

#------------------------------------------
#          evaluation
#------------------------------------------
predict.class =  predict(object = bank_model,  
                         newdata = test.df,
                         type = "class")  

predict.probs = predict(object = bank_model,  
                        newdata = test.df,   
                        type = "prob")
predict.probs.yes <- predict.probs[,"yes"]

evaluation <- confusionMatrix(data = predict.class,       
                              reference = test.df$y)

accuracy <- evaluation$overall["Accuracy"]

cat("Accuracy : ", accuracy, "\n")

ce(actual = test.df$y, 
   predicted = predict.class)


pred <- prediction(predict.probs.yes, test.df$y)
roc_perf <- performance(pred,"tpr","fpr")
plot(roc_perf, colorize=TRUE)

auc_perf <- performance(pred,"auc")
auc <- auc_perf@y.values[[1]]
cat("AUC :", auc)
