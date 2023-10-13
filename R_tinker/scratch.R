library(tidyverse)
library(gganimate)

df <- read.csv('filtered_master.csv')
df$Coalition.point.lead <- df$Coalition.point.lead/100
df <- select(df, t_ed, Coalition.point.lead, Yes_lead_pts_so_far, Party)
dg <- data.frame(
  't_ed' = rep(df$t_ed, 2),
  'Value' = c(-(df$Coalition.point.lead), df$Yes_lead_pts_so_far),
  'State' = c(rep('Labor lead 2022 2PP', nrow(df)), rep('Yes lead so far', nrow(df))),
  'Party' = rep(df$Party, 2)
)

p <- ggplot(data = dg, aes(x = t_ed, y = Value, colour = Party)) +
  geom_point() +
  transition_states(State, transition_length = 2, state_length = 4) +
  shadow_wake(wake_length = 0.5, alpha = TRUE) + 
  labs(subtitle = "Election: {closest_state}")

# Render the animation
animate(p, renderer = gifski_renderer(), width = 800, height = 450, res = 100)