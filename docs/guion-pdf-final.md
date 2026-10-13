# Guion del PDF final — ReparaCampus

Este archivo sirve como base para armar el PDF final. Se mantiene un lenguaje claro de estudiantes y solo se incluyen evidencias reales.

## 1. Portada

- Universidad Simón Bolívar
- Programa: Ingeniería de Sistemas
- Asignatura: BAQ INGENIERÍA DEL SOFTWARE I - 5906 - T04 - 2026 - 2
- Título: Examen SDD — ReparaCampus
- Equipo: Henry Berrio, Juan González, Leyter López, Milton Ramírez, Santiago Hernández, Steven Reyes
- Henry Berrio: 202511271544
- Juan González: 202511275006
- Leyter López: 20221343876
- Milton Ramírez: 202511274317
- Santiago Hernández: 202511272788
- Steven Reyes: 202511274612
- Grupo: T04
- Docente: IGLESIAS SOLANO ADRIANA MARIA
- Fecha: 2026-10
- Repositorio: https://github.com/nagiberrioreales-design/reparacampus

## 2. Índice

Se generará automáticamente en Word/PDF con las 11 secciones y número de página.

## 3. Problema y alcance

Explicar con palabras sencillas:
- necesidad de registrar y dar seguimiento a daños de infraestructura;
- actores: solicitante, coordinador y técnico;
- RF01–RF05;
- ubicaciones y categorías válidas;
- cinco cuentas ficticias;
- límites del prototipo: sin adjuntos, notificaciones, hosting obligatorio ni IA dentro del producto;
- reglas que no se pueden cambiar;
- tres preguntas al cliente y supuestos pendientes documentados.

Fuente interna: `docs/preguntas-cliente.md`.

## 4. Cinco SPECS

Presentar S01–S05 con:
- historia;
- alcance;
- entradas;
- permisos;
- reglas;
- criterios de aceptación;
- tareas;
- versión 0.1;
- revisión previa por Steven Reyes en PR #6.

Fuentes:
- `specs/S01-registro.md`
- `specs/S02-priorizacion-asignacion.md`
- `specs/S03-atencion-solucion.md`
- `specs/S04-validacion-reapertura.md`
- `specs/S05-consulta-historial.md`

Evidencia clave: PR #6 aprobado antes del código.

## 5. Diseño

Incluir:
- componentes;
- modelo de datos;
- UML de estados;
- secuencia de rechazo;
- decisión Flask + SQLite + Jinja + pytest;
- alternativas consideradas y por qué no se usaron.
- interfaz institucional incorporada mediante el PR #21.

Fuentes:
- `docs/arquitectura.md`
- `docs/uml/componentes.puml`
- `docs/uml/modelo-datos.puml`
- `docs/uml/estados.puml`
- `docs/uml/secuencia-rechazo.puml`

## 6. IA e implementación

Explicar cuatro intervenciones reales:
1. especificación;
2. implementación sencilla;
3. pruebas y límites;
4. revisión final.

Para cada una mostrar:
- contexto;
- prompt resumido;
- respuesta útil;
- decisión humana;
- error o limitación;
- corrección;
- evidencia.

Fuente: `docs/ia-bitacora.md`.

También resumir la implementación de RF01–RF05 y enlazar PR #7 a #11.

## 7. Validación

Incluir:
- Matriz RF → SPEC → AC → código → prueba;
- Comando `pytest -q`;
- Ejecuciones históricas separadas: Milton documentó 56 pruebas locales en un SHA anterior; Henry documentó 58 en copia temporal; Santiago ejecutó 67 pruebas locales sobre `1176f261a976...`. No son equivalentes entre sí;
- Último CI positivo comprobado para el PR documental #30: [GitHub Actions #38323411541](https://github.com/nagiberrioreales-design/reparacampus/actions/runs/38323411541), **67 passed in 26.88s**, sobre `4be3d411a5c6...`; falta verificar la versión concreta que se declare como entrega;
- Los tres recorridos de integración;
- Límites 19/20, 800/801, 48 h y 48 h + 1 s;
- Regresión completa de S01–S05 correspondiente a la versión entregada;

Fuentes:
- `docs/matriz-spec-codigo.md`
- `docs/resultados-pruebas.md`
- Historial de GitHub Actions correspondiente a la versión que finalmente se entregue.

**Importante:** no mezclar las 56 pruebas de cierres históricos con las 67 del CI ampliado. El workflow corre con `pull_request` y **no** hay CI `push` registrado para el `main` posterior. Distinguir el SHA de cada evidencia y las siete observaciones de cobertura parcial de aserciones de la auditoría de Henry.

## 8. Riesgos

Mostrar los cuatro riesgos:
- R-IA-01: transición inventada por IA;
- R-IA-02: prueba que repite el mismo error del código;
- R-PROD-01: acceso a incidencias ajenas;
- R-PROD-02: estado e historial inconsistentes.

Para cada uno: causa, impacto, control, responsable y evidencia.

Fuente: `docs/riesgos.md`.

## 9. Entrega reproducible

Debe quedar:
- URL del repositorio;
- Tag histórico `release-examen` comprobado: `b7988274e6173dc13158fd112657e6dc512eb6e0` (release anterior; **no es el SHA del `main` actual**);
- SHA del código definitivo probado, una vez integrados los cambios pendientes;
- instalación;
- arranque;
- seed;
- cuentas ficticias;
- `pytest -q`;
- README accesible.

Fuente: `README.md`.

## 10. Contribuciones y cierre

Explicar aportes verificables por integrante.

Estado actual:
- Henry Berrio: revisión cruzada del PR #18 y auditoría de 43 AC (PR #22 aprobado externamente y fusionado, con siete observaciones de aserciones parciales aún documentadas).
- Steven Reyes: aprobación previa PR #6 y revisión del PR #16; PR documental #18 creado y fusionado.
- Juan González: Issue #12 y APPROVED PR #16 desde `GM-Talent`; PR #25 de mejoras RF02/RF05 descrito como suyo pero publicado desde `gmtalentscompany-source`, **abierto, aprobado y no fusionable**; no presentar los cambios de PR #25 como ya integrados.
- Leyter López: Issue #13 cerrado y revisión APPROVED PR #16 desde `leiter11447-crypto`; no consta una nueva revisión personal del último `main`.
- Milton Ramírez: Issue #14 cerrado y APPROVED PR #16 desde `Bellator07`; PR #27 contiene su informe de 56 pruebas locales anteriores, CI 67, pero **está abierto, sin aprobación formal y no fusionable**.
- Santiago Hernández: Issue #15 cerrado, PR #23/#24/#26/#28/#30 fusionados desde `snt-10`; informe de 67 pruebas locales en un SHA histórico, CI del PR #30 con 67 aprobadas. Verificar PDF y versión final del equipo.
- Contrastar los aportes con el archivo de contribuciones y las evidencias reales.

Fuente: `docs/contribuciones.md`.

Cierre final del equipo:
- qué aprendimos al trabajar primero con SPEC;
- por qué las pruebas ayudaron a detectar reglas límite;
- qué dificultad tuvimos con estados, permisos y revisión;
- conclusión sobre cumplimiento del examen.

## 11. Referencias

Usar las referencias oficiales registradas en `docs/referencias.md`, incluyendo el enunciado de ReparaCampus entregado por el docente.

## Pendientes antes de exportar el PDF

1. Confirmar el estado del GitHub Project y sus cuatro estados requeridos.
2. Verificar GitHub Actions para la versión que se entregará.
3. Resolver qué hacer con PR #25 (mejoras visuales; abierto y no fusionable) y PR #27 (informe de Milton; abierto, sin revisión y no fusionable); integrar solo con revisión y permiso, o documentar exclusión.
4. Acordar el SHA definitivo y distinguirlo del tag histórico `release-examen` (`b7988274...`), sin mover ni recrear el tag sin acuerdo explícito.
5. Generar el Word y el PDF definitivos con evidencias de esa versión.
6. Abrir el PDF IEEE, comprobar citas y referencias, índices con enlaces internos, figuras y cuatro UML legibles, además de la numeración `n de N` en **todas** las páginas.
7. Coordinar que todos los integrantes entreguen el mismo PDF.