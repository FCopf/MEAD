assoc_municipies = function(n = 200, p1 = 0.2, p2 = 0.8, seed = 2){
  set.seed(seed)
  Moradia = sample(0:1, size = n, repl = T, 
                   prob = c(0.75, 0.25))
  Opiniao = if_else(condition = Moradia == 1,
                    true = rbinom(n = n, size = 1, prob = p1),
                    false = rbinom(n = n, size = 1, prob = p2))
  df = data.frame(Entrevistado = 1:n,
                  Opiniao, Moradia)
  df = df %>% 
    mutate(Opiniao = recode(Opiniao,
                            `1` = 'A favor', 
                            `0` = 'Contra'),
           Moradia = recode(Moradia, 
                            `1` = 'Residente',
                            `0` = 'Não-Residente'))
  return(df)
}