# Usa una imagen oficial de Python
FROM python:3.12-slim

# Establece directorio de trabajo
WORKDIR /app

# Copia dependencias
COPY requirements.txt .

# Instala dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copia el código
COPY . .

# Expone el puerto
EXPOSE 7001

# Comando de arranque
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "7001"]
