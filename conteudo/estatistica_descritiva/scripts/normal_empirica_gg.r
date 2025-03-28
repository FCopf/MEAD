
normal_empirica_gg <- function(){
  mean.1 <-0
  sd.1 <- 1
  zstart <- -4
  zend <- 4
  zcritical <- 1.65
  
  my_col <- "#00998a"
  
  x <- seq(from = mean.1 + zstart*sd.1, to = mean.1 + zend*sd.1, by = .01)
  
  
  MyDF <- data.frame(x = x, y = dnorm(x, mean = mean.1, sd = sd.1))
  
  shade_curve <- function(MyDF, zstart, zend, fill = "red", alpha = .5){
    geom_area(data = subset(MyDF, x >= mean.1 + zstart*sd.1
                            & x < mean.1 + zend*sd.1),
              aes(y=y), fill = fill, color = NA, alpha = alpha)
  }
  
  xlabels = expression(mu - 4*sigma,
                       mu - 3*sigma,
                       mu - 2*sigma,
                       mu - 1*sigma,
                       mu,
                       mu + 1*sigma,
                       mu + 2*sigma,
                       mu + 3*sigma,
                       mu + 4*sigma)
  
  normal_areas = diff(pnorm(q = c(zstart:zend))) * 100
  area3 = round(diff(pnorm(q = c(-3,3)))*100,2)
  area2 = round(diff(pnorm(q = c(-2,2)))*100,2)
  area1 = round(diff(pnorm(q = c(-1,1)))*100,2)
  normal_text3 = paste(area3, '% a 3 desvios padrões da média', sep = '')
  normal_text2 = paste(area2, '% a 2 desvios padrões da média', sep = '')
  normal_text1 = paste(area1, '% a 1 desvio padrão da média', sep = '')
  
  p1a <- ggplot(MyDF, aes(x = x, y = y)) + geom_line() +
    shade_curve(MyDF = MyDF, zstart = -1, zend = 1, fill = my_col, alpha = .9) +
    shade_curve(MyDF = MyDF, zstart = 1, zend = 2, fill = my_col, alpha = .7) +
    shade_curve(MyDF = MyDF, zstart = -2, zend = -1, fill = my_col, alpha = .7) +
    shade_curve(MyDF = MyDF, zstart = 2, zend = 3, fill = my_col, alpha = .5) +
    shade_curve(MyDF = MyDF, zstart = -3, zend = -2, fill = my_col, alpha = .5) +
    shade_curve(MyDF = MyDF, zstart = 3, zend = zend, fill = my_col, alpha = .3) +
    shade_curve(MyDF = MyDF, zstart = zstart, zend = -3, fill = my_col, alpha = .3) +
    annotate(geom = 'text', x = 0.5 + (zstart:zend)[-9], 
             y = rep(0.05, length(normal_areas)),
             label = paste(round(normal_areas,2),"%", sep = '')) +
    annotate(geom = 'segment', 
             x = (zstart:zend)[-c(1,9)], 
             xend = (zstart:zend)[-c(1,9)],
             y = 0, yend = c(0.65, 0.55, 0.45, 0.4, 0.45, 0.55, 0.65),
             linetype = 2) +
    annotate(geom = 'segment',
             x = c(-3,-2,-1),
             xend = c(3,2,1),
             y = c(0.65, 0.55, 0.45),
             yend = c(0.65, 0.55, 0.45)) +
    annotate(geom = 'text',
             x = 0, y = c(0.67, 0.57, 0.47),
             label = c(normal_text3, normal_text2, normal_text1)) +
    scale_x_continuous(breaks = zstart:zend,
                       labels = xlabels) +
    scale_y_continuous(breaks = NULL) +
    ylab('Densidade da distribuição normal') +
    theme_classic(base_size = 15) +
    ylab("") + xlab("")
  
  p1a
  
}

