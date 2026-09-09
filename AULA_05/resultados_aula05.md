EXERCICIO 1: 

Ambiente preparado com sucesso.

=== TESTE DA FUNÇÃO PRINCIPAL ===
Frase original: Gostaria de saber se vocês estão DEVOLVENDO os valores das mesas compradas!!!
Frase processada: gostar saber devolver valor meso comprada

========================================

=== EXECUÇÃO DO DIAGNÓSTICO DO DESAFIO ===
Texto original:
MEU sofá!!! chegou quebrado e quero DEVOLVER!!!

Texto normalizado:
sofá chegar quebrar querer devolver

Quantidade de caracteres:
47

Quantidade de tokens antes:
7

Quantidade de tokens depois:
5

Tokens removidos:
['meu', 'e']

Tokens finais:
['sofá', 'chegar', 'quebrar', 'querer', 'devolver']
--------------------------------------------------


EXERCICIO 2:

Dataset simulado carregado com sucesso.
Treinando o modelo FastText...
Modelo FastText treinado com sucesso!

=== TESTE DE MEAN POOLING ===
Frase original: 'MEU sofá!!! chegou quebrado e quero DEVOLVER!!!'
Frase limpa:    'sofá chegar quebrar querer devolver'
Formato do vetor gerado (Shape): (50,)
Primeiros 5 valores do vetor:    [-0.00131294  0.00268017 -0.00125948 -0.00134992 -0.00097263]...

Matriz final pronta para Classificação (X): Formato (5, 50)


EXERCICIO 3:

Dataset real carregado com sucesso! Total de linhas: 80
Aplicando a esteira de pré-processamento nas mensagens...
Transformando as mensagens do arquivo em vetores semânticos...
Utilizando a coluna 'intencao' como alvo da classificação.
Modelo de Regressão Logística treinado com dados reais!

=== RELATÓRIO DE CLASSIFICAÇÃO REAL ===
                    precision    recall  f1-score   support

logistica_entregas       0.80      1.00      0.89         4
   suporte_tecnico       0.75      0.75      0.75         4
 trocas_devolucoes       0.60      0.75      0.67         4
  vendas_orcamento       0.50      0.25      0.33         4

          accuracy                           0.69        16
         macro avg       0.66      0.69      0.66        16
      weighted avg       0.66      0.69      0.66        16


=== TESTANDO O CHATBOT COM INTENÇÕES E FALLBACK ===
Entrada: 'quero devolver meu sofá'
Ação:   FALLBACK_HUMANO - Confiança máxima de 25.00% é menor que o limiar.

Entrada: 'como faço para realizar a devolução?'
Ação:   FALLBACK_HUMANO - Confiança máxima de 25.00% é menor que o limiar.

Entrada: 'cadê meu pedido?'
Ação:   FALLBACK_HUMANO - Confiança máxima de 25.01% é menor que o limiar.

Entrada: 'meu pedido nao chego'
Ação:   FALLBACK_HUMANO - Confiança máxima de 25.01% é menor que o limiar.

Entrada: 'qual é a previsão do tempo?'
Ação:   FALLBACK_HUMANO - Confiança máxima de 25.00% é menor que o limiar.


EXERCICIO 4:

=== TABELA COMPARATIVA DO LABORATÓRIO ===
| Modelo              | Accuracy   | Precision   | Recall   | F1     |
|:--------------------|:-----------|:------------|:---------|:-------|
| Regressão Logística | 68.75%     | 66.25%      | 68.75%   | 65.97% |
| KNN                 | 56.25%     | 45.00%      | 56.25%   | 49.37% |

[RECOMENDAÇÃO TÉCNICA]: O algoritmo selecionado para o motor NLU deve ser a **Regressão Logística**, 
com base na métrica F1-Score que pondera melhor o desbalanceamento das intenções de SAC em cenários reais.


Questão 1 - Qual modelo apresentou melhor desempenho?

A Regressão Logística foi melhor. Ela acertou 68.75% de acurácia contra só 56.25% do KNN, se mostrando bem mais firme para entender as intenções das mensagens.

Questão 2 - Por que os resultados podem ser diferentes mesmo utilizando os mesmos embeddings?

Porque os dois pensam de um jeito completamente diferente. A Regressão Logística tenta olhar o cenário geral e traçar uma linha matemática para separar o que é cada intenção. Já o KNN não cria fórmula nenhuma, ele simplesmente olha quem são os vizinhos mais próximos e assume que a nova mensagem é igual a eles.

Questão 3 - O KNN utiliza distância. Por que a qualidade dos embeddings é particularmente importante para esse algoritmo?

O KNN depende 100% de mapa geométrico. Se o embedding juntar palavras que não têm nada a ver só porque parecem na escrita, o KNN vai se perder totalmente na conta e dar o palpite errado. Ele não tem como corrigir um mapa que já veio bagunçado.

Questão 4 - Se o sistema tivesse 100 mil mensagens e centenas de intenções, você escolheria KNN? Justifique.

Não, pois o KNN é aquele tipo "preguiçoso": ele não decora nada no treino. Toda vez que um cliente mandasse um "oi", o chatbot teria que calcular a distância dessa frase contra as 100 mil mensagens salvas na memória para achar os vizinhos. O sistema ia travar ou demorar uma eternidade para responder.

Questão 5 - Qual modelo você escolheria para colocar em produção neste cenário?

Regressão Logística. Além de ter sido bem mais precisa nos testes, a resposta para o cliente sai na hora com um custo de servidor quase zero.


