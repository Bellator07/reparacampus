# Revisión posterior de SPECS y trazabilidad — asignada a Henry Berrio

**Proyecto:** ReparaCampus — Ingeniería de Software I.
**Tipo:** lista de auditoría posterior a la implementación; no sustituye la revisión previa aprobada en [PR #6](https://github.com/nagiberrioreales-design/reparacampus/pull/6).
**Responsable de completar y validar:** Henry Berrio.
**Estado real:** REVISIÓN TÉCNICA ASISTIDA Y PRUEBAS DOCUMENTADAS; cierre de verificaciones, revisión independiente y PDF final pendientes.
**Fecha / usuario GitHub / SHA:** evidencias documentadas en la sección «Datos por completar después de ejecutar»; la cuenta autora del PR no constituye por sí sola prueba de autoría personal de cada verificación.

## Hallazgo documental corregido

El antiguo `specs/README.md` mantenía «pendiente de revisión» y «No iniciada» para S01–S05, a pesar de los PR integrados #6–#11. Esta propuesta actualiza el índice con enlaces, recuentos de AC, pruebas y cronología histórica. No altera las SPECS aprobadas v0.1.

## Informe de inspección técnica asistida por IA (12/10/2026)

**Naturaleza:** la inspección inicial fue realizada con asistencia de IA mediante lectura estática de fuentes GitHub. Posteriormente, Henry ejecutó las pruebas automatizadas en una copia temporal del repositorio, obteniendo 58 pruebas aprobadas y 0 fallidas el 12/10/2026. Esta evidencia no equivale a una aprobación independiente ni garantiza la ausencia de defectos. La revisión por otro integrante continúa pendiente.

**Fuentes cotejadas:** las cinco SPECS v0.1; `app/domain.py`, `app/incidents.py`, `app/reporting.py`, `app/auth.py`; `tests/test_s01_unit.py`, `tests/test_s01_integration.py`, `tests/test_s02_priority_assignment.py`, `tests/test_s03_attention_solution.py`, `tests/test_s04_validation_reopen.py`, `tests/test_s05_query_history.py` y `tests/test_integration_flows.py`; matriz `docs/matriz-spec-codigo.md`.

| SPEC | Hallazgo de lectura estática | Evidencia trazable | Verificación humana |
|---|---|---|---|
| S01 / RF01 | `validate_new_incident` restringe los tres códigos, catálogos y descripción 20–500 tras `strip`. `create` toma el autor de sesión y guarda incidencia+evento en transacción. | `app/domain.py`, `app/incidents.py`, `tests/test_s01_unit.py`, `tests/test_s01_integration.py` | REVISIÓN PARCIAL (12/10/2026): Henry revisó AC-S01-01 a AC-S01-08. Resultado: 14 pruebas S01 aprobadas, 0 fallidas, ejecutadas en copia temporal. Acceso sin sesión y fecha UTC verificados mediante revisión del código en `app/auth.py` y `app/incidents.py`. SHA de la versión probada: `62fb7d1c0557ff6f0fd245bbef181ee4e3c7c921`.|
| S02 / RF02 | `calculate_priority` devuelve CRITICA/ALTA/NORMAL según riesgo e impacto. `assign` exige coordinador, estado REGISTRADA, técnico activo y no asignación previa; registra evento en transacción. | `app/domain.py`, `app/incidents.py`, `tests/test_s02_priority_assignment.py` | REVISADO (12/10/2026): Henry comprobó AC-S02-01 a AC-S02-08. Resultado: 8 pruebas aprobadas, 0 fallidas, ejecutadas en copia temporal. Se verificaron prioridades, asignación, permisos, técnico inactivo, prevención de reasignación e historial. SHA probado: 62fb7d1c0557ff6f0fd245bbef181ee4e3c7c921. |
| S03 / RF03 | `start_attention` y `propose_solution` exigen técnico asignado y estado compatible; `validate_solution` limita el texto a 20–800 caracteres. | `app/incidents.py`, `app/domain.py`, `tests/test_s03_attention_solution.py` | REVISIÓN PARCIAL (12/10/2026): 13 passed in 4.91s. Verificados los 8 AC mediante pruebas e inspección del código. Pendiente comprobar explícitamente la ausencia de eventos en AC-S03-07. Pruebas ampliadas publicadas en el PR #22. |
| S04 / RF04 | `get_owned_incident` comprueba el propietario; confirmación, rechazo y reapertura aplican los estados permitidos. La reapertura utiliza UTC y un límite de 48 horas, conservando técnico y soluciones. | `app/incidents.py`, `tests/test_s04_validation_reopen.py`, `tests/test_integration_flows.py` | REVISIÓN PARCIAL (12/10/2026): 11 passed in 3.85s. Prueba adicional de flujo completo aprobada (1 passed in 1.14s). Contrastados los 9 AC. Pendiente verificar explícitamente el orden cronológico de AC-S04-08 y ampliar la cobertura de AC-S04-09. Prueba ampliada publicada en el PR #22. |
| S05 / RF05 | `list_incidents` filtra por usuario, rol, estado y prioridad. La consulta del historial aplica controles de acceso y escapado HTML. El tablero calcula conteos y porcentaje de cierre, incluido el caso sin incidencias. | `app/reporting.py`, `tests/test_s05_query_history.py` | REVISIÓN PARCIAL (12/10/2026): 9 pruebas aprobadas (9 passed in 5.26s). Contrastados los 10 AC mediante pruebas e inspección. Pendiente reforzar la comprobación del orden cronológico del historial y los conteos detallados del tablero. |

**Cobertura documental:** cada una de las cinco SPECS tiene historia, entradas, precondiciones, reglas, errores, criterios Dado/Cuando/Entonces, tareas, pruebas esperadas y decisión de revisión previa. El recuento es S01=8, S02=8, S03=8, S04=9, S05=10: **43 criterios**, relacionados en `docs/matriz-spec-codigo.md` con rutas y nombres de pruebas.

**Evidencia de pruebas histórica:** una captura proporcionada por el equipo muestra `56 passed in 20.25s` sobre su instalación local después de cambios de interfaz. También hay una ejecución de CI anterior con trabajo `pytest` exitoso: [GitHub Actions #38017818628](https://github.com/nagiberrioreales-design/reparacampus/actions/runs/38017818628). Estos resultados históricos **no sustituyen la verificación actual**: en la revisión posterior se registraron `58 passed in 21.42s` en copia temporal, y el flujo `pytest` del PR #22 finalizó correctamente en [GitHub Actions #38287576768](https://github.com/nagiberrioreales-design/reparacampus/actions/runs/38287576768).

**Conclusión limitada:** la lectura no identificó contradicciones evidentes entre las reglas principales y sus funciones correspondientes. Sin embargo, no se ha acreditado una nueva verificación humana criterio por criterio ni la ausencia absoluta de defectos. En particular, las preguntas de `docs/preguntas-cliente.md` continúan como supuestos, no decisiones del cliente.

**Revisión requerida para el cierre:** completar la comprobación exhaustiva de las 43 correspondencias de la matriz y reforzar los casos pendientes identificados. Registrar la decisión humana final desde la cuenta del responsable, completar el PDF y obtener revisión independiente del PR. La inspección asistida por IA debe seguir identificada como tal.

## Inspección que debe realizar Henry

Marcar únicamente después de verificar cada punto con el archivo SPEC, el código y las pruebas.

| SPEC / RF | AC | Qué revisar | Resultado / evidencia |
|---|---:|---|---|
| [S01 / RF01](../specs/S01-registro.md) | 8 | Catálogos permitidos; longitudes 19, 20, 500 y 501; rol; autor de sesión; incidencia y evento atómicos; texto escapado | REVISIÓN PARCIAL (12/10/2026): 14 pruebas aprobadas, 0 fallidas. Revisados AC-S01-01 a AC-S01-08. Acceso sin sesión y fecha UTC comprobados mediante inspección de código. SHA base: 62fb7d1c0557ff6f0fd245bbef181ee4e3c7c921. |
| [S02 / RF02](../specs/S02-priorizacion-asignacion.md) | 8 | Riesgo y prioridad; técnico activo; solo coordinador; REGISTRADA → ASIGNADA; no reasignación | REVISADO (12/10/2026): 8 criterios comprobados mediante revisión de código y 8 pruebas aprobadas en copia temporal. SHA: 62fb7d1c0557ff6f0fd245bbef181ee4e3c7c921. |
| [S03 / RF03](../specs/S03-atencion-solucion.md) | 8 | Solo técnico asignado; estados válidos; solución 19, 20, 800, 801; historial | REVISIÓN PARCIAL (12/10/2026): 13 pruebas aprobadas en tests/test_s03_attention_solution.py (13 passed in 4.91s). Contrastados los 8 AC, incluidos permisos, estados, longitudes, persistencia, historial y escapado HTML. Pendiente comprobar explícitamente que AC-S03-07 no genere eventos. Pruebas ampliadas publicadas en el PR #22. |
| [S04 / RF04](../specs/S04-validacion-reapertura.md) | 9 | Propiedad; motivo 9, 10, 300, 301; 48 h exactas y un segundo después; conservación de técnico y soluciones; historial | REVISIÓN PARCIAL (12/10/2026): 11 pruebas aprobadas en test_s04_validation_reopen.py (11 passed in 3.85s). Flujo completo de cierre, reapertura y segundo cierre aprobado (1 passed in 1.14s). Verificados los 9 AC mediante pruebas e inspección. Pendiente comprobar explícitamente el orden cronológico de AC-S04-08 y ampliar la cobertura de AC-S04-09. Cambios publicados en el PR #22. |
| [S05 / RF05](../specs/S05-consulta-historial.md) | 10 | Permisos por rol; filtros de estado y prioridad; historial, soluciones y eventos; bloqueo de edición; conteos del tablero; porcentajes de cierre; escapado HTML; acceso ajeno HTTP 403 | REVISIÓN PARCIAL (12/10/2026): 9 pruebas aprobadas en tests/test_s05_query_history.py (9 passed in 5.26s). Revisados los 10 AC con evidencia automatizada e inspección. Pendiente reforzar el orden cronológico del historial (AC-S05-04) y los conteos detallados del tablero (AC-S05-06). |

## Cadena de trazabilidad

`RF → historia → SPEC v0.1 → AC → tarea → issue → código/PR → prueba → resultado`

- **RF01:** Issue #1, [PR #7](https://github.com/nagiberrioreales-design/reparacampus/pull/7); `tests/test_s01_unit.py` y `tests/test_s01_integration.py`.
- **RF02:** Issue #2, [PR #8](https://github.com/nagiberrioreales-design/reparacampus/pull/8); `tests/test_s02_priority_assignment.py`.
- **RF03:** Issue #3, [PR #9](https://github.com/nagiberrioreales-design/reparacampus/pull/9); `tests/test_s03_attention_solution.py`.
- **RF04:** Issue #4, [PR #10](https://github.com/nagiberrioreales-design/reparacampus/pull/10); `tests/test_s04_validation_reopen.py`.
- **RF05:** Issue #5, [PR #11](https://github.com/nagiberrioreales-design/reparacampus/pull/11); `tests/test_s05_query_history.py`.

Comparar las 43 filas de [`docs/matriz-spec-codigo.md`](matriz-spec-codigo.md) con los archivos de prueba. Verificar que los valores esperados se establezcan independientemente del código de producción.

Los tres recorridos de integración se encuentran en `tests/test_integration_flows.py`: cierre normal; rechazo y nueva solución; cierre y reapertura con segundo cierre.

## Lista de verificación de cierre

- [x] Se revisaron con asistencia de IA las cinco SPECS (S01–S05) y se contrastaron los 43 criterios con el código y las pruebas disponibles; las limitaciones de cobertura están documentadas.
- [ ] Comprobar exhaustivamente las 43 correspondencias de `docs/matriz-spec-codigo.md` con rutas, pruebas y resultados individualizados.
- [x] Se contrastaron los permisos y transiciones principales con el enunciado y las pruebas existentes; siguen pendientes de refuerzo S03-07, S04-08/09 y S05-04/06.
- [x] Se ejecutó `py -3.12 -m pytest -q` en la copia temporal (58 aprobadas, 0 fallidas); se registraron el SHA base, los commits del PR #22 y la ejecución exitosa de CI.
- [x] Se documentaron hallazgos, limitaciones y ampliaciones de pruebas de S03 y S04, sin afirmar ausencia total de defectos.
- [ ] Un integrante diferente revisó el PR #22 y dejó su evaluación.
- [ ] Se actualizó el PDF final con el aporte efectivamente realizado.

## Datos por completar después de ejecutar

| Evidencia | Valor verificado |
|---|---|
| Fecha/hora | 12/10/2026. Hora exacta pendiente de registrar. |
| Rama documental anterior | `docs/revision-specs-henry` (PR #19, ya fusionado). |
| Rama de la inspección asistida | `docs/auditoria-tecnica-specs`. |
| Commit SHA | `03a3a1d11311fb3f4785f0c90299be9ef3bafcaa` (commit publicado en PR #22; actualizar después del próximo commit). |
| Pull Request | PR #22 — `docs/auditoria-tecnica-specs` hacia `main`. Abierto y pendiente de revisión independiente. |
| Usuario GitHub responsable | `nagiberrioreales-design` (cuenta autora del PR #22). Identidad del responsable de la revisión humana pendiente de confirmar. |
| Revisor de otro integrante | PENDIENTE de revisión independiente. |
| Pruebas (comando, n.º aprobadas, fallidas, evidencia) | `py -3.12 -m pytest -q` — 58 passed in 21.42s, 0 fallidas. Ejecutadas en Windows con Python 3.12 desde `reparacampus_pruebas`. GitHub Actions #38286451808: trabajo `pytest` exitoso en PR #22. |
| Hallazgos y correcciones | Se ampliaron las pruebas de S03 y S04 para verificar persistencia, permisos e historial. Pendiente reforzar S03-07, orden cronológico de S04-08 y S05-04, casos inválidos de S04-09 y conteos detallados de S05-06. |
| Decisión humana final, con justificación | PENDIENTE: completar después de las verificaciones restantes y la revisión independiente. |
## Ejecución general de pruebas — 12/10/2026

Responsable: Henry Berrio.

Comando ejecutado:
`py -3.12 -m pytest -q`

Resultado:
**58 passed in 21.42s — 0 pruebas fallidas.**

Entorno: Python 3.12, Windows, copia temporal
`reparacampus_pruebas`.

Se ejecutaron las pruebas de S01, S02, S03, S04, S05
y los flujos de integración.

Se ampliaron las pruebas de S03 y S04 para reforzar
las verificaciones de persistencia e historial.

Observaciones pendientes: comprobación adicional del
historial en S03-07, orden cronológico en S04-08 y S05-04,
cobertura de operaciones inválidas en S04-09 y conteos
detallados del tablero en S05-06.

Los cambios de la auditoría y las pruebas ampliadas de S03 y S04 fueron publicados en el Pull Request #22.

GitHub Actions #38286451808 finalizó correctamente con el trabajo `pytest` aprobado.

La revisión independiente de otro integrante y la decisión humana final permanecen pendientes.

**Nota de integridad académica:** este registro fue preparado con asistencia de IA para la inspección y documentación. Las pruebas ejecutadas y las verificaciones realizadas se documentan por separado. La revisión independiente y la aprobación final permanecen pendientes.