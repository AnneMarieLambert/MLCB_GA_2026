
ATIVIDADE 1: CHATBOT VERSÃO 1 (KNN)

=== RELATÓRIO DE CLASSIFICAÇÃO ===
                    precision    recall  f1-score   support

logistica_entregas       1.00      1.00      1.00         6
       reclamacoes       1.00      1.00      1.00         6
           suporte       1.00      1.00      1.00         6
 trocas_devolucoes       1.00      1.00      1.00         6
            vendas       1.00      1.00      1.00         6

          accuracy                           1.00        30
         macro avg       1.00      1.00      1.00        30
      weighted avg       1.00      1.00      1.00        30


=== MATRIZ DE CONFUSÃO ===
[[6 0 0 0 0]
 [0 6 0 0 0]
 [0 0 6 0 0]
 [0 0 0 6 0]
 [0 0 0 0 6]]

=== INICIANDO BATERIA DE TESTES (10 INPUTS OBRIGATÓRIOS) ===

[Teste 1/10]
Digite a frase do cliente: "Olá, boa tarde! Tem alguém disponível para me ajudar?"
Intenção Identificada: 'vendas' com 100.00% de certeza.

[Teste 2/10]
Digite a frase do cliente: "Qual é o prazo de entrega para o sofá retrátil no CEP 01701-000?"
Intenção Identificada: 'logistica_entregas' com 100.00% de certeza.

[Teste 3/10]
Digite a frase do cliente: "Vocês fazem esse guarda-roupa de casal sob medida ou em outras cores?"
Intenção Identificada: 'vendas' com 100.00% de certeza.

[Teste 4/10]
Digite a frase do cliente: "Quero saber o preço dessa mesa de jantar com 6 cadeiras."
Intenção Identificada: 'vendas' com 100.00% de certeza.

[Teste 5/10]
Digite a frase do cliente: "Quanto custa uma passagem de avião para o Rio de Janeiro?"
Intenção Identificada: 'vendas' com 66.67% de certeza.

[Teste 6/10]
Digite a frase do cliente: onde posso comer coxinha 
Intenção Identificada: 'suporte' com 66.67% de certeza.

[Teste 7/10]
Digite a frase do cliente: onde posso pegar um aviao pra noronha baratinho
Intenção Identificada: 'suporte' com 66.67% de certeza.

[Teste 8/10]
Digite a frase do cliente: palmeiras n tem mundial
Intenção Identificada: 'vendas' com 100.00% de certeza.

[Teste 9/10]
Digite a frase do cliente: cinco mentes bem pensantes
Confiança muito baixa (33.33%).
Fallback: Desculpe, não consegui compreender com clareza. Redirecionando para a equipe humana...

[Teste 10/10]
Digite a frase do cliente: planta faz isso
Confiança muito baixa (33.33%).
Fallback: Desculpe, não consegui compreender com clareza. Redirecionando para a equipe humana...


ATIVIDADE 2:  
Construção do Zero (Versão 2 — Decision Tree e 8 Testes Digitados)

=== MATRIZ DE CONFUSÃO ===
[[4 0 0 0 2]
 [1 2 0 0 3]
 [0 0 5 0 1]
 [0 2 0 2 2]
 [0 0 0 0 6]]

=== RELATÓRIO DE CLASSIFICAÇÃO (PRECISION, RECALL, F1-SCORE) ===
                    precision    recall  f1-score   support

logistica_entregas       0.80      0.67      0.73         6
       reclamacoes       0.50      0.33      0.40         6
           suporte       1.00      0.83      0.91         6
 trocas_devolucoes       1.00      0.33      0.50         6
            vendas       0.43      1.00      0.60         6

          accuracy                           0.63        30
         macro avg       0.75      0.63      0.63        30
      weighted avg       0.75      0.63      0.63        30


=== INICIANDO BATERIA DE TESTES (8 INPUTS OBRIGATÓRIOS) ===

[Teste 1/8]
Digite a frase do cliente: oi quero pizza
Intenção Detectada: 'suporte' (Confiança: 100.00%)

[Teste 2/8]
Digite a frase do cliente: esse sistema é muito ruim 
Intenção Detectada: 'vendas' (Confiança: 58.33%)

[Teste 3/8]
Digite a frase do cliente: palhação
Intenção Detectada: 'vendas' (Confiança: 58.33%)

[Teste 4/8]
Digite a frase do cliente: vire a esqueda a 300 metros
Intenção Detectada: 'vendas' (Confiança: 58.33%)

[Teste 5/8]
Digite a frase do cliente: gostaria de ver o filme poderoso chefinho
Intenção Detectada: 'vendas' (Confiança: 58.33%)

[Teste 6/8]
Digite a frase do cliente: voces fazem entrega?
Intenção Detectada: 'vendas' (Confiança: 58.33%)

[Teste 7/8]
Digite a frase do cliente: "Por favor quero devolver a mesa que veio arranhada"
Intenção Detectada: 'vendas' (Confiança: 58.33%)

[Teste 8/8]
Digite a frase do cliente: "Oi preciso de ajuda como montar o rack da sala"
Intenção Detectada: 'suporte' (Confiança: 100.00%)

atividade 3: 

3.1: 
| Modelo | Acurácia Geral | F1-Score (Weighted) | Principais Erros na Matriz |
| :--- | :--- | :--- | :--- |
| **KNN (K=3)** | 100% | 100% | Vulnerável a ruídos: Atribui de 66% a 100% de confiança para frases aleatórias ("palmeiras", "coxinha") baseado apenas na presença isolada de palavras comuns como "tem" ou "onde". Só ativou o Fallback em frases com 0% de termos conhecidos por gerar empate triplo de distância. |
| **Decision Tree** | 63% | 63% | Superficialidade e Viés em Vendas: A classe vendas teve um recall de 1.00 mas precision baixíssima (0.43), agindo como uma "lixeira" do modelo. Qualquer frase com palavras desconhecidas caiu por exclusão no nó de vendas com 58.33% de certeza, burlando o limiar de 50% e impedindo o Fallback de funcionar no mundo real. |


3.2: KNN (K=3): Teve acurácia aparente de 100% no teste fixo, mas se mostrou vulnerável a ruídos em produção. Ele flutua as probabilidades (33.33%, 66.67%, 100%) baseado na contagem dos vizinhos. O Fallback só funcionou por "cegueira total" (empate triplo de 33.33% quando nenhuma palavra era conhecida).

Decision Tree: Teve acurácia real menor (63% no console) e sofreu de "arrogância algorítmica". O modelo criou um nó generalista que classificou quase todos os ruídos inéditos como vendas com exatamente 58.33% de confiança. Isso burlou o limiar de 50%, impedindo o acionamento do Fallback humano para frases absurdas (como "poderoso chefinho" ou "palhação").


3.3: Pelos testes realizados, o melhor modelo a se usar é o KNN pois ele é mais treinado e consegue avaliar/separar melhor as solicitações dos usuários. 

Justificativa técnica: Ele acertou mais nos dados controlados, alcançando 100% de acurácia contra apenas 63% da Árvore de Decisão. Quando o KNN não conhece as palavras da frase, ele assume a dúvida, derruba a confiança para 33.33% e chama o atendente humano. A Árvore de Decisão, por outro lado, tenta adivinhar por exclusão e dá 58.33% de certeza para qualquer besteira, enganando o sistema de segurança e deixando o cliente sem resposta correta.





