library(tidyverse)
library(rstanarm)

# Join the two datasets so the variables are the same as the book.
df <- read_csv("srrs2.dat") %>%
  filter(state == "MN") %>%
  mutate(radon = activity,
         log.radon = log(ifelse(radon == 0, .1, radon)),
         fips = paste0(stfips, cntyfips),
         y = log.radon,
         x = floor) %>%
  left_join(
    read_csv("cty.dat") %>%
      filter(st == "MN") %>%
      mutate(u = log(ifelse(Uppm == 0, .1, Uppm)), # Uranium
             fips = paste0(stfips, ctfips)),
    by = c("fips")) %>%
  select(y, x, u, county)

# Complete Pooling
pooled <- lm(y ~ x, df)
summary(pooled)


# No Pooling, no intercept term.
no.pool <- lm(y ~ x + county - 1, df)
summary(no.pool)
