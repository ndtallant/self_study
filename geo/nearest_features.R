library(sf)
library(tidyverse)

r = sqrt(2)/10
b1 = st_buffer(st_point(c(.1,.1)), r)
b2 = st_buffer(st_point(c(.9,.9)), r)
b3 = st_buffer(st_point(c(.9,.1)), r)

circles <- tibble("circle.id" = c("a","b","c"),
                  geometry = st_sfc(b1, b2, b3))

plot(circles$geometry, col = NA, border = 2:4)

pts <- tibble("pt.id" = 1:4,
             geometry = st_sfc(
               st_point(c(.3,.1)), st_point(c(.6,.2)), st_point(c(.6,.6)), st_point(c(.4,.8)
            )))

# Add points to plot        
plot(pts$geometry, add = TRUE, col = 1)

# Nearest Feature returns an index for nearest feature in 2nd geometry.
nearest.index <- try(st_nearest_feature(pts$geometry, circles$geometry))

# Returns a linestring connecting the nearest points between geometries
# Note the second geometry is indexed such that you get the nearest point of
# the nearest geometry.
ls <- st_nearest_points(pts$geometry, circles$geometry[nearest.index], pairwise = TRUE)
plot(ls, col = 5:8, add = TRUE)

pts$nearest.circle <- circles$circle.id[nearest.index]
pts$dist.to.nearest <- st_length(ls) # Unit?
pts
