import requests
import pandas as pd
import os

def fetch_binance_data(symbol="BTCUSDT", interval="1h"):
    diretorio_atual = os.getcwd()
    print(f"📍 Pasta atual: {diretorio_atual}")
    
    base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    data_dir = os.path.join(base_path, 'data')
    file_path = os.path.join(data_dir, 'crypto_data.csv')
    
    url = "https://api.binance.com/api/v3/klines"
    params = {"symbol": symbol, "interval": interval, "limit": 500}
    
    try:
        response = requests.get(url, params=params)
        if response.status_code == 200:
            data = response.json()
            df = pd.DataFrame(data, columns=[
                'timestamp', 'open', 'high', 'low', 'close', 'volume', 
                'close_time', 'quote_asset_volume', 'number_of_trades', 
                'taker_buy_base_asset_volume', 'taker_buy_quote_asset_volume', 'ignore'
            ])
            
            # Tratamento de tipos corrigido
            df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
            cols_to_fix = ['open', 'high', 'low', 'close', 'volume']
            df[cols_to_fix] = df[cols_to_fix].astype(float)
            df = df[['timestamp'] + cols_to_fix]
            
            if not os.path.exists(data_dir):
                os.makedirs(data_dir)
                
            df.to_csv(file_path, index=False)
            print(f"✅ SUCESSO! Arquivo salvo em: {file_path}")
        else:
            print(f"❌ Erro na API: {response.status_code}")
    except Exception as e:
        print(f"⚠️ Ocorreu um erro: {e}")

if __name__ == "__main__":
    fetch_binance_data()