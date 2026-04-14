import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import joblib
import os

def train_model():
    input_path = 'data/processed_data.csv'
    model_path = 'data/crypto_model.pkl'
    
    if not os.path.exists(input_path):
        print("❌ Dados processados não encontrados. Rode o processing.py primeiro.")
        return

    print("🤖 Treinando o modelo de Machine Learning...")
    df = pd.read_csv(input_path)

    # Definindo o que queremos prever (o preço de fechamento)
    # E quais dados usaremos para prever (as médias móveis que você criou)
    features = ['ma_7', 'ma_21', 'returns']
    target = 'close'

    X = df[features]
    y = df[target]

    # Dividindo os dados: 80% para treino e 20% para teste
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Usando um algoritmo de Random Forest (Floresta Aleatória)
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Calculando a acurácia básica (R²)
    score = model.score(X_test, y_test)
    print(f"📈 Precisão do modelo (R²): {score:.4f}")

    # Salvando o modelo treinado para usar no Dashboard depois
    joblib.dump(model, model_path)
    print(f"✅ Modelo salvo em {model_path}")

if __name__ == "__main__":
    train_model()