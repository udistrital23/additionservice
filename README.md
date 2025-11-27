# Base Converter Service

Servicio simple en FastAPI que expone POST `/converter` en el puerto `8001`.

Payload JSON esperado:

```
{
  "numero": "1207",
  "base_origen": 8,
  "base_destino": 10
}
```

Respuesta esperada (200):

```
{ "resultado": "511" }
```

Construir y ejecutar con Docker:

```bash
# Desde la carpeta del proyecto (donde está este README)
docker build -t baseconverterservice:latest .
docker run --rm -p 8001:8001 baseconverterservice:latest
```

También se incluyen tests pytest en `tests/test_validator.py`.
