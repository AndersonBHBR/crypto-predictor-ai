# Usa uma imagem estável do Python
FROM python:3.11-slim

# Define o diretório de trabalho
WORKDIR /app

# Instala apenas o essencial para o Python rodar pacotes compilados
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copia o requirements.txt
COPY requirements.txt .

# Instala as bibliotecas Python
RUN pip install --no-cache-dir -r requirements.txt

# Copia o código (seguindo sua estrutura de pastas)
COPY . .

# Expõe a porta do Streamlit
EXPOSE 8501

# Comando para rodar
ENTRYPOINT ["streamlit", "run", "src/app.py", "--server.port=8501", "--server.address=0.0.0.0"]