# 📈 Crypto Predictor AI

Este projeto utiliza Inteligência Artificial para analisar dados históricos de criptoativos e prever tendências de preços futuros. Ele combina engenharia de dados em tempo real com modelos de Machine Learning. Em outras palavras, um projeto de Ciência de Dados e Machine Learning de ponta a ponta que consome dados da API da Binance, processa indicadores técnicos e utiliza um modelo de Regressão para prever preços de Bitcoin.

## 🚀 Funcionalidades
- **Ingestão de Dados:** Coleta automática de dados da API da Binance (intervalo de 1h).
- **Engenharia de Features:** Cálculo de Médias Móveis (7h e 21h) e retornos logarítmicos.
- **Machine Learning:** Modelo baseado em *Random Forest Regressor* para predição de preços.
- **Dashboard Interativo:** Interface construída em Streamlit para visualização e simulações.
- **Containerização:** Projeto totalmente Dockerizado para facilitar o deploy.

## 🛠️ Tecnologias Utilizadas
- **Python 3.11+**
- **Scikit-Learn**: Para modelagem preditiva.
- **Pandas & Numpy**: Processamento e manipulação de dados.
- **Binance API**: Fonte de dados em tempo real.
- **Streamlit**: Dashboard interativo.
- **Docker**: Conteinerização para deploy simplificado.

## 🧠 Diferenciais Técnicos
- **Pipeline de ETL**: Extração automatizada de dados via API REST.
- **Feature Engineering**: Cálculo de indicadores técnicos (Médias Móveis, RSI).
- **Deploy Pronto**: Inclui Dockerfile para execução em ambientes de nuvem (AWS/Azure).

## 🛠️ Como Executar
1. Clone o repositório: `git clone https://github.com/AndersonBHBR/crypto-predictor-ai.git
cd crypto-predictor-ai`
2. Construa a imagem Docker: `docker build -t crypto-predictor-ai .`
3. Execute o container: `docker run -p 8501:8501 crypto-predictor-ai`
4. Acesse o dashboard: Abra o navegador em `http://localhost:8501`.

## 🙋 Sobre o Autor

Feito com 💻 e ☕ por [Anderson Lima Araújo](https://www.linkedin.com/in/anderson-araujo-pcd)😊  
Sou desenvolvedor Full Stack com foco em IA, APIs modernas, soluções web escaláveis e interesse em projetos internacionais 🌍
<p>
    <img align=left margin=10 width=80 src="https://avatars.githubusercontent.com/u/7528140?v=4"/>
    <p>&nbsp&nbsp&nbspAnderson Lima Araújo<br>
    &nbsp&nbsp&nbsp<a href="http://instagram.com/andersonbhbr">Instagram</a>&nbsp;|&nbsp;<a href="https://github.com/AndersonBHBR">GitHub</a>&nbsp;|&nbsp;<a href="https://www.linkedin.com/in/anderson-araujo-pcd/">LinkedIn</a>&nbsp;|&nbsp;<a href="https://www.behance.net/andersonbhbr">Behance</a></p>
</p>
<br/><br/>
