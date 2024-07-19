# Usa una imagen base de Python
FROM python:3.12-slim-bullseye

# Establece el directorio de trabajo
WORKDIR /app

# Copia el archivo de requisitos y el script de inicio
COPY requirements.txt .

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto del código de la aplicación
COPY . .

# Expone el puerto en el que correrá la aplicación
EXPOSE 8000

# Comando para ejecutar la aplicación
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

