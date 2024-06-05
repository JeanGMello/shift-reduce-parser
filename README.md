Um analisador shift-reduce é um tipo de analisador descendente usado em compiladores para analisar a estrutura gramatical de uma entrada. é utilizado uma pilha para auxiliar na verificação e construção da estrutura sintática da linguagem. A análise feita com duas operações principais, empilhar (shift) e reduzir (reduce):

-Empilhar:
Nesta operação, o próximo símbolo da entrada é removido e colocado no topo da pilha. A ideia é avançar na leitura da entrada, preparando-se para possíveis reduções subsequentes.

-Reduzir:
Essa operação substitui um conjunto de símbolos no topo da pilha por um único não-terminal, de acordo com uma regra de produção da gramática. Se o topo da pilha corresponde ao lado direito de uma regra de produção, esses símbolos srão substituídos pelo símbolo não-terminal do lado esquerdo da regra.
