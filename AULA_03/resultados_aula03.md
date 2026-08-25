 LAB 01 - AULA 03 (MLCB): Pré-processamento e Stopwords

 --- RESULTADOS DO LAB 01 (AULA 03) ---
Mensagem: 'Preciso urgente da segunda via da fatura'
Intenção Predita: [segunda_via]
Vocabulário Filtrado (sem stopwords): ['2a', '2a via', 'aberto', 'acordo', 'acordo pagar', 'alterar', 'alterar endereço', 'app', 'atrasada', 'atualizo', 'atualizo dados', 'boleto', 'cadastramento', 'dados', 'dados residenciais', 'débito', 'débito aberto', 'dívida', 'emitir', 'emitir segunda', 'endereço', 'endereço cadastramento', 'fatura', 'fatura atrasada', 'fazer', 'fazer um', 'gostaria', 'gostaria alterar', 'negociar', 'negociar pagamento', 'no', 'no app', 'onde', 'onde atualizo', 'pagamento', 'pagamento dívida', 'pagar', 'pagar débito', 'posso', 'posso emitir', 'residenciais', 'residenciais no', 'segunda', 'segunda via', 'um', 'um acordo', 'via', 'via boleto', 'via fatura']


1- O impacto da remoção do mesmo consiste no aumento dos erros da interpretação do algoritmo. è importante que seja usado o stopwords para melhores filtros nos testes.

2- O ngram_range=(1,2) é utilizado para que não haja duplo sentido em uma mesma palavra, é usado 1,2 na maioria dos casos para que a quantidade de acertos seja maior. Exemplo: Quando utilizamos uma frase que obtenha "segunda via", as palavras separadas podem significar "segunda" como "segunda feira" e "via" como "via de estrada".

3- Ajuda no processamento, para que os dados genéricos não ocupem um espaço desnecessário na aplicação.
