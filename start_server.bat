@echo off
echo Iniciando servidor local en http://localhost:8000
echo Copia todos los .wav, index.html, data_hashed.json y este .bat a la misma carpeta.
echo Pulsa Ctrl+C para parar.
python -m http.server 8000