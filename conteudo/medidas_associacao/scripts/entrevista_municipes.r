entrevista_municipes = function(){
  set.seed(2)
  N = 200
  mun = data.frame(Entrevistado = 1:N,
                   Opiniao = sample(c('A favor', 'Contra'),
                                    size = N, repl = T,
                                    prob = c(0.75, 0.25)),
                   Moradia = sample(c('Residente', 'Não-Residente'),
                                    size = N, repl = T,
                                    prob = c(0.4, 0.6)))
  return(mun)
}
