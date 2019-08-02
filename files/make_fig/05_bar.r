library(tidyverse)

df_tmp <-
  tibble(
    X = c("A", "A", "B", "C")
  )

df_tmp %>%
  ggplot(aes(X)) +
  geom_bar() +
  scale_y_continuous(breaks = c(0, 1, 2)) +
  theme_minimal() +
  theme(
    axis.text.x  = element_text(size = 16),
    axis.title.x = element_text(size = 20),
    axis.text.y  = element_text(size = 16),
    axis.title.y = element_text(size = 20)
  ) +
  labs(
    y = "Count"
  )

ggsave("../../fig/05_bar.png")
