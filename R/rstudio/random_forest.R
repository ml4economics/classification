# tidyverse includes dplyr, tidyr, readr, ggplot2
library(tidyverse)
library(caret)
library(ROCR)
library(randomForest)

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
model <- randomForest(y ~ ., 
                      data = train.df,
                      ntree = 100)

layout(matrix(c(1,2),nrow=1), width=c(4,1)) 
par(mar=c(5,4,4,0)) #No margin on the right side
plot(model, log="y")
par(mar=c(5,0,4,2)) #No margin on the left side
plot(c(0,1),type="n", axes=F, xlab="", ylab="")
legend("top", colnames(model$err.rate),col=1:4,cex=0.8,fill=1:4)

#------------------------------------------
#          evaluation
#------------------------------------------
predict.class =  predict(object = model,  
                         newdata = test.df,
                         type = "response")  

predict.probs = predict(object = model,  
                        newdata = test.df,   
                        type = "prob")
predict.probs.yes <- predict.probs[,"yes"]

evaluation <- confusionMatrix(data = predict.class,       
                              reference = test.df$y)

accuracy <- evaluation$overall["Accuracy"]

cat("Accuracy : ", accuracy, "\n")


pred <- prediction(predict.probs.yes, test.df$y)
roc_perf <- performance(pred,"tpr","fpr")
plot(roc_perf, colorize=TRUE)

auc_perf <- performance(pred,"auc")
auc <- auc_perf@y.values[[1]]
cat("AUC :", auc)

