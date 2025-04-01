conditional_tree <- function(  prob_text = expression(P(A), 
                                                       P(bar(A)),
                                                       P(B~"|"~A),
                                                       P(bar(B)~"|"~A),
                                                       P(B~"|"~bar(A)),
                                                       P(bar(B)~"|"~bar(A))),
                               final_text = expression(P(A*intersect(B)) == P(A) ~ "x" ~ P(B~"|"~A),
                                                        P(A*intersect(bar(B))) == P(A) ~ "x" ~ P(bar(B)~"|"~A),
                                                        P(bar(A)*intersect(B)) == P(bar(A)) ~ "x" ~ P(B~"|"~bar(A)),
                                                        P(bar(A)*intersect(bar(B))) == P(bar(A)) ~ "x" ~ P(bar(B)~"|"~bar(A)))){
  df <- data.frame(x0 = c(0,0,5,5,5,5), 
                   x1 = c(5,5,10,10,10,10),
                   y0 = c(0,0,5,5,-5,-5),
                   y1 = c(5,-5,8,3,-3,-8))

  ang <- c(27,333, 20,349,14,346)
  tposy <- c(3.5,-3.5, 2.6,-2.3,2.3,-2.7)
  plot(1, axes = F, xlab = '', ylab = '', ylim = c(-10,12), xlim = c(-1,20), type = "n")
  segments(x0 = df$x0,x1 = df$x1,y0 = df$y0, y1 = df$y1)
  points(x = df$x0, y = df$y0, pch = 19, cex = 2)
  points(x = df$x1, y = df$y1, pch = 19, cex = 2)
  arrows(x0 = c(0,5, 10), x1 = c(0,5,10), y0 = 10.5, y1 = c(1,6,9), length = 0.15)
  for (i in 1:length(prob_text)){
    text(x =  df$x0[i]+2.5, y = df$y0[i] + tposy[i], labels = prob_text[i], srt = ang[i])
  }
  text(x = df$x1[-c(1,2)]+4.5, y = df$y1[-c(1,2)], labels = final_text, cex = 0.8)
  text(x = c(0,5, 10), y = 11.5, labels = c("1a Etapa", "2a Etapa", "Resultado Final"), cex = 0.9)  
}


                              
     