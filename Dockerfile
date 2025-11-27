FROM python:3.11-slim

WORKDIR /app

# Copiar requisitos e instalar
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copiar el código
COPY . /app

ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/app  

# Puerto que expone el servicio
EXPOSE 8001

# Arrancar uvicorn al iniciar el contenedor
# CMD ["pytest", "-q"]
CMD ["behave"]
# CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8001"]

