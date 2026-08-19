--- RESULTADOS DO LAB 01 ---
Mensagem: 'Quero consultar quanto dinheiro tenho' ==> Intenção Predita: [consultar_saldo]
Mensagem: 'Pode me ajudar a fazer um pix?' ==> Intenção Predita: [fazer_pix]
Mensagem: 'Gostaria de cancelar meu cartão de crédito' ==> Intenção Predita: [cancelar_conta]

 1 - Dois deles vieram de forma correta e o um deles não 'Quero consultar quanto dinheiro tenho' . Após ajustar o resultado foi correto do algoritimo resultando o valor [consultar saldo].
 2- A melhor forma de corrigir um erro de algoritimo é colocando mais um exemplo de mensagem para que ele entenda a forma correta de devolver um resultado, como corrigido acima.
 3 - Ele é o algoritmo de inteligência artificial responsável por aprender a tomar as decisões.
 O LogisticRegression atua como o classificador que aprende a associar as palavras vetorizadas às suas respectivas intenções (fit).
 Ele calcula pesos matemáticos para cada termo e, por fim, prevê a categoria mais provável para novas mensagens enviadas (predict).




 --- RESULTADOS DO LAB 02 ---
Mensagem de Teste: 'Gostaria de devolver o produto que comprei'
Intenção Predita: troca_devolucao

--- Distribuição de Probabilidades por Classe ---
Classe [duvida_frete]: 27.99%
Classe [rastrear_pedido]: 24.54%
Classe [troca_devolucao]: 47.46%

1- Sim, estão 100% corretos baseados nas frases.
2- Não há erros, mas podemos melhorar nosso código para maior eficiência aumentando a base de dados.
3- Calcula a frequência com que cada palavra aparece durante o treino. Ele multiplica as probabilidades individuais de cada termo de forma independente e gera uma distribuição percentual, classificando o texto na intenção de maior probabilidade.



 --- RESULTADOS DO LAB 03 ---

 Acurácia do Modelo: 33.33%


1- O resultado foi: 33.33% e isso pode ser enganoso pois acertar poucas frases de teste não garante que o modelo aprendeu variações reais e cada único acerto ou erro altera o resultado final.
2- Ela toma a decisão através de regras lógicas de "sim ou não" com base nas palavras.
3- O risco é o Overfitting, pois a árvore decora os testes aprendendo um padrão específico e com novas frases terá falhas recorrentes.




 --- RESULTADOS DO LAB 04 ---

Mensagem do Usuário: 'Preciso reservar um voo para São Paulo com urgência' 
==> Intenção Identificada: [comprar_passagem]

Mensagem do Usuário: 'Não vou mais viajar e quero o cancelamento' 
==> Intenção Identificada: [cancelar_reserva]

Mensagem do Usuário: 'Alguém pode me ajudar? Quero falar com suporte humano' 
==> Intenção Identificada: [falar_atendente]


Justificativa técnica: 

Vetorizador Escolhido (TF-IDF Vectorizer): Usamos o TF-IDF em vez do CountVectorizer porque ele é mais inteligente na hora de ler o texto. Ele deixa de lado aquelas palavras que só servem para ligar a frase (como "para", "um", "o") e foca no que realmente importa para a agência, dando um peso maior para palavras marcantes como "voo", "cancelamento" e "humano".

Algoritmo de Classificação (Regressão Logística): Escolhemos a Regressão Logística por ser um modelo muito seguro e direto para classificar textos curtos. Ela lida melhor com bases de dados menores sem ficar chutando resultados como o Naive Bayes, e também não corre o risco de simplesmente decorar as frases do treino, que é o grande problema da Árvore de Decisão.







