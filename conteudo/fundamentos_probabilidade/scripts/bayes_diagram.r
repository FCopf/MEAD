library(DiagrammeR)
library(purrr)

bayes_probability_tree <- function(
  prior, A = "A", B = "B",
  true_positive, true_negative,
  edges_names = NULL,
  node_lab = TRUE,
  digitos = 3,
  node_width = 1.2,
  node_height = 1.2,
  node_fontsize = 16,
  edges_fontsize = 14
) {
  
  # Verificação de validade das probabilidades
  if (any(c(prior, true_positive, true_negative) <= 0 | c(prior, true_positive, true_negative) >= 1)) {
    stop("Todas as probabilidades devem estar entre 0 e 1 (exclusivo).", call. = FALSE)
  }

  # Probabilidades complementares
  complement <- function(p) 1 - p
  c_prior <- complement(prior)
  c_tp <- complement(true_positive)
  c_tn <- complement(true_negative)

  # Cálculos das probabilidades nos ramos
  round_d <- partial(round, digits = digitos)
  b1 <- round_d(prior * true_positive)
  b2 <- round_d(prior * c_tp)
  b3 <- round_d(c_prior * c_tn)
  b4 <- round_d(c_prior * true_negative)

  # Probabilidade a posteriori via Teorema de Bayes
  bp <- round_d(b1 / (b1 + b3))

  # Labels dos nós
  if (is.logical(node_lab)) {
    if (node_lab) {
      node_labels <- c(
        "Início",
        A, B,
        A, B, B, A,
        b1, b2, b4, b3
      )
    } else {
      node_labels <- rep("", 11)
    }
  } else if (length(node_lab) == 11) {
    node_labels <- node_lab
  } else {
    stop("node_lab deve ser TRUE, FALSE ou um vetor de 11 rótulos.", call. = FALSE)
  }

  # Nomes das arestas
  Px <- function(X) {paste("P(", X, ")", sep = "")}
  Px_cond <- function(X, Cond) {paste("P(", X, "|", Cond, ")", sep = "")}
    
  if (is.null(edges_names)) {
    edges_names <- c(Px(A), Px(A),
                     Px_cond(A,A), Px_cond(B,A),
                     Px_cond(A,B), Px_cond(B,B),
                     "", "", "", "")
  } else if (length(edges_names) != 10) {
    stop("edges_names deve ter exatamente 10 elementos.", call. = FALSE)
  }

  # Criando grafo
  graph <- create_graph() |> 
    add_n_nodes(
      n = 11,
      label = node_labels,
      type = "path",
      node_aes = node_aes(
        shape = "circle",
        x = c(0, 3, 3, 6, 6, 6, 6, 8, 8, 8, 8),
        y = c(0, 2, -2, 3, 1, -3, -1, 3, 1, -3, -1),
        width = node_width,
        height = node_height,
        fontsize = node_fontsize,
        fillcolor = "#4e73a3",
        style = "filled"
      )
    ) |> 
    add_edges_w_string("1->2 1->3 2->4 2->5 3->6 3->7 4->8 5->9 6->10 7->11") |> 
    set_edge_attrs("label", edges_names) |> 
    set_edge_attrs("fontsize", edges_fontsize)

  # Renderizando o gráfico
  render_graph(graph)
  }
