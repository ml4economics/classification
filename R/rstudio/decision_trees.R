# tidyverse includes dplyr, tidyr, readr, ggplot2
library(tidyverse)
library(rpart)
library(rpart.plot)
library(caret)
library(ROCR)
library(randomForest)

options(warn=-1)

#------------------------------------------
#         load data
#------------------------------------------
data_dir <- "../../data/bank-full.csv"
bank_data <- read.csv(data_dir)

#------------------------------------------
#        textual data exploration
#------------------------------------------
sprintf("# rows: %d - # columns: %d", nrow(bank_data), ncol(bank_data))
summary(bank_data)

#------------------------------------------
#        partition data
#------------------------------------------
set.seed(4711)
n <- nrow(bank_data)
n_train <- round(0.8 * n) 

train_indices <- sample(1:n, n_train)

train.df <-  bank_data[train_indices,]
test.df  <-  bank_data[-train_indices,]

dim(train.df)
dim(test.df)

#------------------------------------------
#        model
#------------------------------------------
cp <- 0.002
bank_model <- rpart(formula = y ~ ., 
                    data = train.df, 
                    method = "class",
                    control = rpart.control(minsplit = 2, cp = cp))

print(bank_model)

rpart.plot(bank_model, type=2)

#------------------------------------------
#          evaluation
#------------------------------------------
# predict.rpart supports types 'vector', 
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
