library(tidyverse)

df <- read.csv('filtered_master.csv')

# Linear regress of 2PP

print('2pp vs. Tertiary')
twopp_t_ed_lm <- lm(ALP.margin ~ t_ed, data = df)
summary(twopp_t_ed_lm)

print('2pp vs. Age')
twopp_age_lm <- lm(ALP.margin ~ age, data = df)
summary(twopp_age_lm)

print('2pp vs. Income')
twopp_income_lm <- lm(ALP.margin ~ income, data = df)
summary(twopp_income_lm)