# permutation_inference.R
# -----------------------

# Two-Sample Permutation Test

# Pool the m + n values.
# repeat
#   Draw a resample of size m without replacement.
#   Use the remaining n observations for the other sample.
#   Calculate the difference in means or another statistic that compares samples.
# until we have enough samples
# Calculate the P-value as the fraction of times the random statistics exceed the original statistic.
# Multibply b 2 for a two-sided test.
# Optionally, plot a histogram of the random statistic values.


# Data can be found here: https://sites.google.com/site/chiharahesterberg/data2
df <- readr::read_csv("Beerwings.csv")

# Base R Version
# --------------

# Find the observed difference in the data.
means <- tapply(df$Hotwings, df$Gender, mean)
observed <- means[2] - means[1]
hotwings <- df$Hotwings

# Repeatedly sample a placebo difference and store.
N <- 10^5 - 1 # number of times to repeat this process
result <- numeric(N)
for (i in 1:N) {
  index <- sample(30, size = 15, replace = FALSE) 
  result[i] <- mean(hotwings[index]) - mean(hotwings[-index])
}

# Plot a histogram
hist(result, xlab = "xbar1 - xbar2", main = "Permutation Distribution for hot wings")
abline(v = observed, col = "blue")

# Calculate the p-value
(sum(result >= observed) + 1) / (N + 1)

# Tidyverse Version
library(tidyverse)

df %>%
  group_by(Gender) %>%
  summarize(avg.hotwings = mean(Hotwings))

take.sample <- function(n, vec) {
  index <- sample(30, size = 15, replace = FALSE)
  return(mean(vec[index]) - mean(vec[-index]))
}

result <- purrr::map_dbl(1:N, take.sample, vec = hotwings)
(sum(result >= observed) + 1) / (N + 1)
