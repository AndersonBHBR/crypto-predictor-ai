import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt

st.set_page_config(page_title="Crypto Predictor AI", layout="wide")

st.title("📈 Crypto Predictor AI Dashboard")
st.write("Análise preditiva de preços de Bitcoin baseada em Machine Learning.")
df = pd.read_csv('data/processed_data.csv')
model = joblib.load('data/crypto_model.pkl')

# Gráfico de Preços Melhorado
st.subheader("Histórico de Preços e Médias Móveis")
fig, ax = plt.subplots(figsize=(12, 6))

# Pegando apenas os últimos 50 registros para não poluir
plot_df = df.tail(50)

ax.plot(plot_df['timestamp'], plot_df['close'], label="Preço Real", linewidth=2)
ax.plot(plot_df['timestamp'], plot_df['ma_7'], label="Média 7h", linestyle="--", alpha=0.8)
ax.plot(plot_df['timestamp'], plot_df['ma_21'], label="Média 21h", linestyle=":", color="orange")

ax.legend()
ax.set_ylabel("Preço em USD")
# Mostra apenas algumas datas para não encavalar
plt.xticks(rotation=45, ha='right')
ax.xaxis.set_major_locator(plt.MaxNLocator(10)) 

st.pyplot(fig)

# Área de Predição
st.subheader("🧠 Simulação de Predição")
col1, col2, col3 = st.columns(3)

with col1:
    ma7 = st.number_input("Média Móvel 7h", value=float(df['ma_7'].iloc[-1]))
with col2:
    ma21 = st.number_input("Média Móvel 21h", value=float(df['ma_21'].iloc[-1]))
with col3:
    retorno = st.number_input("Retorno Atual", value=float(df['returns'].iloc[-1]))

if st.button("Prever Preço"):
    input_data = pd.DataFrame([[ma7, ma21, retorno]], columns=['ma_7', 'ma_21', 'returns'])
    prediction = model.predict(input_data)
    st.success(f"O preço previsto para a próxima hora é: **${prediction[0]:,.2f}**")