# ReparaCampus: instalacion y publicacion

1. En GitHub Desktop, nueva rama `feat/interfaz-responsive-render` desde `main`.
2. Extraer este ZIP y copiar su contenido a la raiz del repositorio clonado, conservando el resto de archivos.
3. VS Code: activar entorno y ejecutar `python -m pip install -r requirements.txt`, luego `pytest -q`.
4. Probar `flask --app app run` en PC y vista responsive F12 (390px y 768px).
5. Crear commit y push; abrir pull request, revisar y fusionar en `main` solo con pruebas exitosas.
6. Render: New > Web Service, conectar repositorio, branch `main`, Language `Python 3`.
   Build: `pip install -r requirements.txt`
   Start: `gunicorn --bind 0.0.0.0:$PORT --workers 1 wsgi:app`
   Environment: `SECRET_KEY` aleatoria larga (solo en panel Render; no subir a Git).
7. PARA PERSISTENCIA SQLITE: se requiere Web Service de pago con disco persistente
   montado exactamente en `/opt/render/project/src/instance`.
   La base se inicializa automaticamente en primer arranque. No ejecutar `init-db` de nuevo.
8. Abrir URL HTTPS, probar inicio de sesion, RF01, asignacion y ciclo completo; revisar SQLite persiste al reimplementar.
9. Actualizar README y PDF del examen y anotar nuevo SHA (sin alterar tag release-examen).

Importante: Render Free no preserva SQLite entre reinicios o despliegues.
Nunca copiar claves ni datos reales de Aula Extendida. Sitio academico de demostracion.
