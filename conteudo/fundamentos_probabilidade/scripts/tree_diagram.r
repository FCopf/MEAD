# This function returns a DOT code block you can place in a Quarto .qmd
bayes_tree_diagram <- function(
  A_name = "A",
  B_name = "B",
  pA,      # P(A)
  pB,      # P(B)
  pAB,     # P(A ∩ B)
  digits = 3
) {
  # Basic validation checks
  if (any(c(pA, pB, pAB) <= 0 | c(pA, pB, pAB) >= 1)) {
    stop("All probabilities must be strictly between 0 and 1.")
  }
  if (pAB > pA || pAB > pB) {
    stop("P(A ∩ B) cannot exceed P(A) or P(B).")
  }
  
  # Derive the conditional probabilities
  pA_givenB <- pAB / pB  # P(A|B)
  pB_givenA <- pAB / pA  # P(B|A)
  
  # Derive complementary conditional probabilities
  pB_givenB <- 1 - pA_givenB  # P(B|B)
  pA_givenA <- 1 - pB_givenA  # P(A|A)
  
  # Intersection probabilities for the second level
  # e.g., P(A and A) = P(A)*P(A|A)
  #       P(A and B) = P(A)*P(B|A)
  #       P(B and A) = P(B)*P(A|B)
  #       P(B and B) = P(B)*P(B|B)
  pAA <- round(pA * pA_givenA, digits)
  pAB2 <- round(pA * pB_givenA, digits)  # naming pAB2 to not confuse with pAB
  pBA <- round(pB * pA_givenB, digits)
  pBB <- round(pB * pB_givenB, digits)
  
  # Create the DOT code block
  dot_code <- sprintf('```{dot}
digraph G {
  node [shape=circle, fontsize=8];
  edge [fontsize=8];

  Root [label="Início"];
  A [label="%s"];
  B [label="%s"];
  AA [label="%s\\n%.3f"];
  AB [label="%s\\n%.3f"];
  BA [label="%s\\n%.3f"];
  BB [label="%s\\n%.3f"];

  Root -> A [label="P(%s)"];
  Root -> B [label="P(%s)"];

  A -> AA [label="P(%s|%s)"];
  A -> AB [label="P(%s|%s)"];

  B -> BA [label="P(%s|%s)"];
  B -> BB [label="P(%s|%s)"];
}
```',
    A_name,             # A node label
    B_name,             # B node label
    A_name, pAA,        # AA leaf label
    B_name, pAB2,       # AB leaf label
    A_name, pBA,        # BA leaf label
    B_name, pBB,        # BB leaf label
    
    A_name,             # label for Root->A
    B_name,             # label for Root->B
    
    A_name, A_name,     # label for A->AA
    B_name, A_name,     # label for A->AB
    
    A_name, B_name,     # label for B->BA
    B_name, B_name      # label for B->BB
  )
  
  return(dot_code)
}
