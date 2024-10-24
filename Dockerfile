# Use uma imagem base oficial do Python
FROM python:3.10-slim

# Defina variáveis de ambiente
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Instale dependências do sistema
RUN apt-get update && apt-get install -y \
    libpango1.0-0 \
    libcairo2 \
    libgirepository1.0-dev \
    python3-gi \
    gobject-introspection \
    build-essential \
    && apt-get clean

# Crie e defina o diretório de trabalho
WORKDIR /usr/src/app

# Instale dependências do Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copie os arquivos do projeto
COPY . .

# Exponha a porta em que o app será executado
EXPOSE 8000

# Comando padrão para rodar a aplicação
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
