# Usa una imagen base con Python
FROM python:3.11-slim

# Establece el directorio de trabajo
WORKDIR /app

# Instala git
RUN apt-get update && apt-get install -y git && apt-get clean

# Configurar Git globalmente con el nombre y correo del autor
RUN git config --global user.name "japipe05" && \
    git config --global user.email "felipehuchija@gmail.com" && \
    git config --global init.defaultBranch main

# Copia los archivos necesarios
COPY . /app

# Crea el directorio 'uploads' si no existe y da permisos
RUN mkdir -p /app/uploads && chmod -R 777 /app/uploads

# Actualiza pip antes de instalar dependencias
RUN pip install --upgrade pip

# Instala dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Expone el puerto si usas FastAPI/Flask
EXPOSE 8000

# Comando para ejecutar el backend (ajústalo a tu framework)
# Modo desarrollo con recarga automática
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
