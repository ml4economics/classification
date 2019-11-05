# tidyverse includes dplyr, tidyr, readr, ggplot2
library(tidyverse)
library(caret, quietly = TRUE)
library(ROCR)

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

if (any(bank_data$y == "yes")) {
bank_data <- bank_data %>%
              mutate(y = ifelse(y=="yes", 1, 0))
}

set.seed(4711)
partition <- createDataPartition(bank_data$y, p = 0.8, list=FALSE)

train.df <-  bank_data[partition,]
test.df  <-  bank_data[-partition,]

dim(train.df)
dim(test.df)

#------------------------------------------
#        model
#------------------------------------------
mod.log <- glm(y ~ ., data = train.df, family=binomial)
summary(mod.log)

#------------------------------------------
#          evaluation
#------------------------------------------
thresh.pred <-.5
probs <- predict(mod.log,newdata=test.df,type="response")

test.df <- test.df %>% 
            mutate(pred.log= ifelse(probs < thresh.pred ,0,1))

# confusion matrix
with(test.df, table(y, pred.log))

# classification accuracy
with(test.df, mean(y == pred.log))

pred <- prediction(probs, test.df$y)
roc_perf <- performance(pred,"tpr","fpr")
plot(roc_perf, colorize=TRUE)

auc_perf <- performance(pred,"auc")
auc <- auc_perf@y.values[[1]]
