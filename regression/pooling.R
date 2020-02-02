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

# Plot County Estimates from No Pooled Model
broom::tidy(no.pool) %>%
  filter(term != "x") %>%
  arrange(estimate) %>%
  mutate(x = row_number()) %>%
    ggplot(aes(x, estimate)) +
      geom_point() +
      geom_errorbar(aes(ymin=(estimate - std.error),
                    ymax=(estimate + std.error)))

# Partially Pooled
p.pool <- stan_glmer(y ~ x + (1 | county), data = df)
p.pool.est <- as_tibble(p.pool) %>%
  select(contains("b["))

m.est <- as_tibble(t(map_df(p.pool.est, mean)), name_repair = "min")
sd.est <- as_tibble(t(map_df(p.pool.est, sd)), name_repair = "min")
bind_cols(c(m.est, sd.est)) %>%
  select(estimate = V1, std.error = V11) %>%
  arrange(estimate) %>%
  mutate(x = row_number()) %>%
    ggplot(aes(x, estimate)) +
      geom_point() +
      geom_errorbar(aes(ymin=(estimate - std.error),
                    ymax=(estimate + std.error)))
