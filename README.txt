
INSTRUCCIONES RÁPIDAS

1) Pon en una carpeta:
   - index.html (este archivo)
   - build_data.py
   - series_numeradas.csv   (tu CSV con columnas: numero, titulo)
   - TODOS los audios: 1.wav, 2.wav, ..., 100.wav

2) Crea el JSON con hashes (sin respuestas en claro):
   - Haz doble clic en build_data.py (o ejecútalo: python build_data.py)
   - Se generará data_hashed.json

3) Abre la web:
   - OPCIÓN A (recomendada): ejecuta "start_server.bat" y entra a http://localhost:8000
   - OPCIÓN B: súbelo a cualquier hosting estático y abre index.html desde tu móvil

Notas:
- La validación ignora mayúsculas/minúsculas y espacios, PERO respeta los acentos.
- Si aciertas una tarjeta, se queda verde y bloqueada. El progreso se guarda en el navegador (localStorage).
- Puedes moverte con botones o deslizando.
