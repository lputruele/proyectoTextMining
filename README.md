# Proyecto sobre Mineria de Datos en Texto

Proyecto de la asignatura de Text Mining para la carrera de Doctorado en Ciencias de la Computación (FAMAF).

Este trabajo consiste en encontrar comunidades a favor y en contra sobre un tópico, en este caso el aborto.

El enfoque utilizado consiste en generar un grafo donde los nodos son tweets de un dataset y en donde los arcos que los unen representan n-gramas en común. Mientras mas n-gramas en común, más peso tiene el arco. En este trabajo se comparan bigramas, trigramas y cuadrigramas.

Los n-gramas a considerar son los que tienen mejor ranking en base a alguna métrica de asociación. Se comparan en este trabajo 6 métricas: pmi, chi-squared, poisson stirling, likelihood ratio, student-t y jaccard.

El grafo luego se particiona en base a un algoritmo de detección de comunidades, y finalmente se evaluan estas particiones contra el mismo dataset pero etiquetado.

El dataset se extrajo de: https://github.com/pablocelayes/twitter-aborto/tree/master/data
