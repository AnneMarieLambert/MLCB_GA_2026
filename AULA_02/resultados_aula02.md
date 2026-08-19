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




