# ===================================================================== #
# LAB 1: NLU BANCÁRIO COM REGRESSÃO LOGÍSTICA #
# ===================================================================== #
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# Dados de exemplo para permitir a execução e teste do script
dados_treino = [
    ("Quero fazer um pix de 1 real", "fazer_transferencia"),
    ("Gostaria de transferir 200 reais para minha tia Sueli", "fazer_transferencia"),
    ("Gostaria de ver meu saldo na conta", "consultar_saldo"),
    ("Qual é o meu saldo atual?", "consultar_saldo"),
    ("Quero ver meu extrato desse mes", "consultar_extrato"),
    ("Como eu vejo o extrato da conta?", "consultar_extrato"),
    ("Bom dia tudo bem?", "fora_escopo"),
    ("Qual o horario do show do jao?", "fora_escopo")
]

stopwords = ["um", "uma", "o", "a", "os", "as", "de", "para", "por", "com", "me", "minha", "meu", "agora"]

# 1. PRÉ-PROCESSAMENTO
def pré_processar(texto):
    texto_limpo = re.sub(r'[^\w\s]', '', texto.lower()).strip()
    tokens = texto_limpo.split()
    
    # TODO 1.1: Filtre as stopwords da lista 'tokens' usando List Comprehension
    tokens_filtrados = [token for token in tokens if token not in stopwords]
    
    return " ".join(tokens_filtrados)

X_treino_limpo = [pré_processar(item[0]) for item in dados_treino]
y_treino = [item[1] for item in dados_treino]

# 2. VETORIZAÇÃO E TREINAMENTO
vectorizer = TfidfVectorizer()
# TODO 1.2: Aprenda o vocabulário e vetorize 'X_treino_limpo' em um único passo
X_vetorizado = vectorizer.fit_transform(X_treino_limpo)

modelo = LogisticRegression(C=10.0) 
modelo.fit(X_vetorizado, y_treino)

# 3. EXTRAÇÃO DE ENTIDADE (REGEX)
def extrair_valor_reais(texto_original):
    match = re.search(r'(\d+)\s*rea(?:is|l)', texto_original, re.IGNORECASE)
    # TODO 1.3: Se houver match, converta o grupo 1 para float. Caso contrário, retorne None.
    return float(match.group(1)) if match else None

# 4. PIPELINE NLU
def processar_nlu(mensagem_usuario, threshold=0.55):
    texto_p = pré_processar(mensagem_usuario)
    vetor_input = vectorizer.transform([texto_p])

    probas = modelo.predict_proba(vetor_input)[0]
    
    # TODO 1.4: Extraia a MAIOR probabilidade (max) e a intenção prevista (argmax em modelo.classes_)
    maior_confianca = max(probas)
    intencao_prevista = modelo.classes_[probas.argmax()]
    
    valor = extrair_valor_reais(mensagem_usuario)
    
    # TODO 1.5: Se maior_confianca < threshold ou intencao == "fora_escopo", retorne FALLBACK.
    # Caso contrário, retorne SUCESSO com a intenção, confiança e o valor extraído.
    if maior_confianca < threshold or intencao_prevista == "fora_escopo":
        return {
            "status": "FALLBACK",
            "intencao": "nao_entendido",
            "confianca": maior_confianca,
            "valor": None
        }
    else:
        return {
            "status": "SUCESSO",
            "intencao": intencao_prevista,
            "confianca": maior_confianca,
            "valor": valor
        }

# --- TESTE 1 ---
if __name__ == "__main__":
    resultado_sucesso = processar_nlu("Quero transferir 150 reais")
    print("Teste 1:", resultado_sucesso)
    
