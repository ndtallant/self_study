### 01 - Intro
library(tidyverse)
library(faraway)

# Data from faraway package.
data(gavote)
head(gavote)
tidytallant::quick_summary(gavote)


### Analyzing undercount, where a registered vote did not go through
### due to malfunction, not voting, or voting for more than one candidate.

gavote$undercount <- (gavote$ballots - gavote$votes) / gavote$ballots

lmod <- lm(undercount ~ gore + perAA, gavote)

# See coefficients
coef(lmod)

# Fitted values
head(lmod$fitted.values)
head(predict(lmod))

# Residuals
residuals(lmod)


# Deviance (Residual Sum of Squares for OLS)
deviance(lmod)

# Degrees of Freedom (Number of cases - number of coefficients)
df.residual(lmod)
length(lmod$fitted.values) - length(coef(lmod))

# Variance of the error \sigma^2 = \sqrt(RSS/df)
sqrt(deviance(lmod)/df.residual(lmod))
sigma(lmod)

# Coef of Determination (Proportion of Explained Variance)
summary(lmod)$r.squared

# Equivalent to squared correlation to predictions and response
cor(predict(lmod), gavote$undercount)^2

# Adjusted R squared for kitchen sink regressors.
summary(lmod)$adj.r.squared

# See everything
summary(lmod)

# Contrast matrix of treatment encoding (leaving out a level in a factor)
contr.treatment(5)

## Come back to page 10
