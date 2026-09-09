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



