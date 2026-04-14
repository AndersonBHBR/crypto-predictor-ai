import pandas as pd
import os

def process_data():
    input_path = 'data/crypto_data.csv'
    output_path = 'data/processed_data.csv'
    
    if not os.path.exists(input_path):
        print("❌ Arquivo de dados não encontrado. Rode o ingestion.py primeiro.")
        return

    print("🛠️ Processando dados e criando indicadores técnicos...")
    df = pd.read_csv(input_path)

    # Criando Indicadores Técnicos Simples
    # 1. Média Móvel (Moving Average) de 7 períodos
    df['ma_7'] = df['close'].rolling(window=7).mean()
    
    # 2. Média Móvel de 21 períodos
    df['ma_21'] = df['close'].rolling(window=21).mean()

    # 3. Retorno percentual diário
    df['returns'] = df['close'].pct_change()

    # Removendo linhas com valores nulos (gerados pelas médias móveis no início)
    df.dropna(inplace=True)

    df.to_csv(output_path, index=False)
    print(f"✅ Dados processados salvos em {output_path}")

if __name__ == "__main__":
    process_data()