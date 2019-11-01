# tidyverse includes dplyr, tidyr, readr, ggplot2
library(tidyverse)
library(gmodels)
library(ggmosaic)

#------------------------------------------
#      graphics settings
#------------------------------------------
## default theme for ggplot
theme_set(theme_bw())

## setting default parameters for mosaic plots
mosaic_theme = theme(axis.text.x = element_text(angle = 90,
                                                hjust = 1,
                                                vjust = 0.5),
                     axis.text.y = element_blank(),
                     axis.ticks.y = element_blank())

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

head(bank_data,10)

CrossTable(bank_data$y) # from gmodels

# This is a very condensed notation. Let's dissect it:
# 1. '. == unknown' is an expression (i.e. lambda) applied to a data frame column.
#    It creates a boolean vector (try : bank_data$job == "unknown")
# 2. sum just counts the number of 'TRUE' values
# 3. ~ makes this a formula (i.e. lambda expression). 
#    The '.' is a placeholder for the argument (checkout out ?formula)
# 4. dplyr::summarize_all takes a list of formulas and applies them to the data frame
#
# # see also : https://cran.r-project.org/web/packages/lazyeval/vignettes/lazyeval.html
#
# %>% is a pipe operator from the 'magrittr' package and heavily used in dplyr.
# x %>% f(y) is equivalent to f(x, y) )

bank_data %>% 
  summarise_all(list(~sum(. == "unknown"))) %>%
  gather(key = "variable", value = "nr_unknown") %>% 
  arrange(-nr_unknown)

#------------------------------------------
#        graphical data exploration
#------------------------------------------
hist(bank_data$age)

# show histograms for the 'age' feature for the different values of the 'y' column
bank_data %>% 
  ggplot() +
  aes(x = age) +
  geom_bar() +
  geom_vline(xintercept = c(30, 60), 
             col = "red",
             linetype = "dashed") +
  facet_grid(y ~ .,
             scales = "free_y") +
  scale_x_continuous(breaks = seq(0, 100, 5))

# show the distribution of jobs for the different values of the 'y' column
bank_data %>% 
  ggplot() +
  geom_mosaic(aes(x = product(y, job), fill = y)) +
  mosaic_theme +
  xlab("Job") +
  ylab(NULL)

