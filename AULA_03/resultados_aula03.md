 LAB 01 - AULA 03 (MLCB): Pré-processamento e Stopwords

 --- RESULTADOS DO LAB 01 (AULA 03) ---
Mensagem: 'Preciso urgente da segunda via da fatura'
Intenção Predita: [segunda_via]
Vocabulário Filtrado (sem stopwords): ['2a', '2a via', 'aberto', 'acordo', 'acordo pagar', 'alterar', 'alterar endereço', 'app', 'atrasada', 'atualizo', 'atualizo dados', 'boleto', 'cadastramento', 'dados', 'dados residenciais', 'débito', 'débito aberto', 'dívida', 'emitir', 'emitir segunda', 'endereço', 'endereço cadastramento', 'fatura', 'fatura atrasada', 'fazer', 'fazer um', 'gostaria', 'gostaria alterar', 'negociar', 'negociar pagamento', 'no', 'no app', 'onde', 'onde atualizo', 'pagamento', 'pagamento dívida', 'pagar', 'pagar débito', 'posso', 'posso emitir', 'residenciais', 'residenciais no', 'segunda', 'segunda via', 'um', 'um acordo', 'via', 'via boleto', 'via fatura']


1- O impacto da remoção do mesmo consiste no aumento dos erros da interpretação do algoritmo. è importante que seja usado o stopwords para melhores filtros nos testes.

2- O ngram_range=(1,2) é utilizado para que não haja duplo sentido em uma mesma palavra, é usado 1,2 na maioria dos casos para que a quantidade de acertos seja maior. Exemplo: Quando utilizamos uma frase que obtenha "segunda via", as palavras separadas podem significar "segunda" como "segunda feira" e "via" como "via de estrada".

3- Ajuda no processamento, para que os dados genéricos não ocupem um espaço desnecessário na aplicação.



LAB 02 - AULA 03 (MLCB): Matriz de Confusão e Métricas

--- RESULTADOS DO LAB 02 (AULA 03) ---
--- Relatório de Classificação ---
                     precision    recall  f1-score   support

horario_atendimento       0.50      1.00      0.67         1
        localizacao       0.00      0.00      0.00         1
    troca_devolucao       0.00      0.00      0.00         1

           accuracy                           0.33         3
          macro avg       0.17      0.33      0.22         3
       weighted avg       0.17      0.33      0.22         3

--- Matriz de Confusão ---
[[1 0 0]
 [1 0 0]
 [0 1 0]]


 1- Precision: Mede as taxas de acertos evitando falsos alarmes. Seria mais ou menos uma divisão de testes (como ABC). Quanto A acertou, temos o percentual individual do mesmo, e isso ocorre com os outros também.  

 Recall: Evita perdas de chamados, medindo a capacidade de cobertura do boot.

 F1-Score: Media harmônica do precision e recall tendo que dar bons resultados. É um indicador principal para decidir se a classe está madura ou não. 

 2- Considerando a diagonal principal os acertos e fora da diagonal os erros.

 3-  Pois ela reflete apenas o desempenho da classe majoritária. 


LAB 03 - AULA 03 (MLCB): Scikit-Learn Pipeline (Modo TODO)


1- 

2- Automatiza e organiza todas as etapas do processo de machine learning, como o pré-processamento dos dados e o treinamento do modelo, em uma única estrutura.

3- Garante que as mesmas etapas de pré-processamento sejam aplicadas de forma consistente aos dados de treino e de teste.
