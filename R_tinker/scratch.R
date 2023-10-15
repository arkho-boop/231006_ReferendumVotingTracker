df <- read.csv('filtered_master.csv')
CN_voters <- read.csv('CN_voters.csv')
AUS_voters <- read.csv('AUS_voters.csv')
IN_voters <- read.csv('IN_voters.csv')

IN_result <- left_join(IN_voters, df, by = c('CED_NAME_2021' = 'Seat')) |> 
  arrange(desc(IN_PROP))
IN_result <- IN_result[c(1:15),]

CN_result <- left_join(CN_voters, df, by = c('CED_NAME_2021' = 'Seat')) |> 
  arrange(desc(CN_PROP))
CN_result <- CN_result[c(1:15),]

AUS_voters <- left_join(AUS_voters, df, by = c('CED_NAME_2021' = 'Seat'))

IN_result <- IN_result |> arrange(-desc(Australian.Labor.Party.Percentage))

IN_result_display <- data.frame(
  'Prop_IN' = rep(IN_result$IN_PROP, 2),
  'Seat_names' = rep(IN_result$CED_NAME_2021, 2),
  'Score' = c(IN_result$No_pc_so_far, 1-IN_result$Australian.Labor.Party.Percentage)*100,
  'Type' = c(rep('No vote', nrow(IN_result)), rep('Coalition 2PP 2022', nrow(IN_result)))
)

df <- df |> filter(dem_rating %in% c('Outer Metropolitan', 'Inner Metropolitan')) |> arrange(-desc(Swing))
df$CN_anc <- FALSE
i <- 1
while (i <= nrow(df)) {
  
  if (df$Seat[[i]] %in% CN_result$CED_NAME_2021) {
    df$CN_anc[[i]] <- TRUE
  }
  
  i <- i + 1
}


CN <- ggplot(df, aes(x = factor(Seat, level = df$Seat), y = Swing*100, fill = CN_anc)) +
  geom_bar(stat = 'identity', alpha = 0.7) +
  geom_hline(aes(yintercept = mean(filter(df, CN_anc == FALSE)$Swing)*100, colour = FALSE), linetype = 'dashed', linewidth = 1) +
  geom_hline(aes(yintercept = mean(filter(df, CN_anc == TRUE)$Swing)*100, colour = TRUE), linetype = 'dashed', linewidth = 1)+
  ylim(-40, 40) +
  labs(title = 'Inner Metro seats swing to Yes from Labor 2PP 2022', subtitle = 'Top 15 Chinese-ancestry seats') + 
  theme(axis.text.x = element_text(angle = 90, vjust = 0.5, hjust = 1))

df <- read.csv('filtered_master.csv')
df <- df |> filter(dem_rating %in% c('Outer Metropolitan', 'Inner Metropolitan')) |> arrange(-desc(Swing))
df$IN_anc <- FALSE
i <- 1
while (i <= nrow(df)) {
  
  if (df$Seat[[i]] %in% IN_result$CED_NAME_2021) {
    df$IN_anc[[i]] <- TRUE
  }
  
  i <- i + 1
}


IN <- ggplot(df, aes(x = factor(Seat, level = df$Seat), y = Swing*100, fill = IN_anc)) +
  geom_bar(stat = 'identity', alpha = 0.7) +
  geom_hline(aes(yintercept = mean(filter(df, IN_anc == FALSE)$Swing)*100, colour = FALSE), linetype = 'dashed', linewidth = 1) +
  geom_hline(aes(yintercept = mean(filter(df, IN_anc == TRUE)$Swing)*100, colour = TRUE), linetype = 'dashed', linewidth = 1)+
  ylim(-40, 40) +
  labs(title = 'Outer Metro and inner metro seats swing to Yes from Labor 2PP 2022', subtitle = 'Top 15 Indian-ancestry seats') + 
  theme(axis.text.x = element_text(angle = 90, vjust = 0.5, hjust = 1))

df <- read.csv('filtered_master.csv')
df <- df |> filter(dem_rating %in% c('Outer Metropolitan', 'Inner Metropolitan')) |> arrange(-desc(Swing))
df$anc <- FALSE
i <- 1
while (i <= nrow(df)) {
  
  if (df$Seat[[i]] %in% IN_result$CED_NAME_2021) {
    df$anc[[i]] <- 'Indian'
  } else if (df$Seat[[i]] %in% CN_result$CED_NAME_2021) {
    df$anc[[i]] <- 'Chinese'
  }
  
  i <- i + 1
}

dg <- data.frame(
  'Seat' = df$Seat,
  'Else' = NA,
  'China' = NA,
  'India' = NA
)

i <- 1
while (i <= nrow(dg)) {
  
  if (dg$Seat[[i]] %in% IN_result$CED_NAME_2021) {
    dg$India[[i]] = filter(IN_result, CED_NAME_2021 == dg$Seat[[i]])$Swing
  } else if (dg$Seat[[i]] %in% CN_result$CED_NAME_2021) {
    dg$China[[i]] = filter(CN_result, CED_NAME_2021 == dg$Seat[[i]])$Swing
  } else {
    dg$Else[[i]] = filter(df, Seat == dg$Seat[[i]])$Swing
  }
  
  i <- i + 1
}