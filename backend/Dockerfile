# Usa una imagen base con Python
FROM python:3.11-slim

# Establece el directorio de trabajo
WORKDIR /app

# Copia los archivos necesarios
COPY . /app

# Instala dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Expone el puerto si usas FastAPI/Flask
EXPOSE 8000

# Comando para ejecutar el backend (ajústalo a tu framework)
# Modo desarrollo con recarga automática
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
