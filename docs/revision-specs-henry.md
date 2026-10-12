# Revisión posterior de SPECS y trazabilidad — asignada a Henry Berrio

**Proyecto:** ReparaCampus — Ingeniería de Software I.
**Tipo:** lista de auditoría posterior a la implementación; no sustituye la revisión previa aprobada en [PR #6](https://github.com/nagiberrioreales-design/reparacampus/pull/6).
**Responsable de completar y validar:** Henry Berrio.
**Estado real:** PENDIENTE DE REVISIÓN HUMANA.
**Fecha real / usuario GitHub / SHA:** completar después de realizar la revisión, nunca antes.

## Hallazgo documental corregido

El antiguo `specs/README.md` mantenía «pendiente de revisión» y «No iniciada» para S01–S05, a pesar de los PR integrados #6–#11. Esta propuesta actualiza el índice con enlaces, recuentos de AC, pruebas y cronología histórica. No altera las SPECS aprobadas v0.1.

## Informe de inspección técnica asistida por IA (12/10/2026)

**Naturaleza:** lectura estática de fuentes GitHub, sin ejecución de código nuevo en esta rama. No corresponde a una revisión realizada por Henry ni a una aprobación por pares.

**Fuentes cotejadas:** las cinco SPECS v0.1; `app/domain.py`, `app/incidents.py`, `app/reporting.py`, `app/auth.py`; `tests/test_s01_unit.py`, `tests/test_s01_integration.py`, `tests/test_s02_priority_assignment.py`, `tests/test_s03_attention_solution.py`, `tests/test_s04_validation_reopen.py`, `tests/test_s05_query_history.py` y `tests/test_integration_flows.py`; matriz `docs/matriz-spec-codigo.md`.

| SPEC | Hallazgo de lectura estática | Evidencia trazable | Verificación humana |
|---|---|---|---|
| S01 / RF01 | `validate_new_incident` restringe los tres códigos, catálogos y descripción 20–500 tras `strip`. `create` toma el autor de sesión y guarda incidencia+evento en transacción. | `app/domain.py`, `app/incidents.py`, `tests/test_s01_unit.py`, `tests/test_s01_integration.py` | PENDIENTE |
| S02 / RF02 | `calculate_priority` devuelve CRITICA/ALTA/NORMAL según riesgo e impacto. `assign` exige coordinador, estado REGISTRADA, técnico activo y no asignación previa; registra evento en transacción. | `app/domain.py`, `app/incidents.py`, `tests/test_s02_priority_assignment.py` | PENDIENTE |
| S03 / RF03 | `start_attention` y `propose_solution` exigen técnico asignado y estado compatible; `validate_solution` limita texto a 20–800. | `app/incidents.py`, `app/domain.py`, `tests/test_s03_attention_solution.py` | PENDIENTE |
| S04 / RF04 | `get_owned_incident` comprueba propietario; confirmación, rechazo y reapertura aplican sus estados permitidos. La reapertura usa UTC del servidor y comprueba `elapsed <= timedelta(hours=48)`, preservando técnico y soluciones. | `app/incidents.py`, `tests/test_s04_validation_reopen.py`, `tests/test_integration_flows.py` | PENDIENTE |
| S05 / RF05 | `list_incidents` filtra por identidad, rol, estado y prioridad. `_authorized_incident` bloquea consultas ajenas; `_dashboard` calcula conteos, críticas abiertas y porcentaje con caso cero. | `app/reporting.py`, `tests/test_s05_query_history.py` | PENDIENTE |

**Cobertura documental:** cada una de las cinco SPECS tiene historia, entradas, precondiciones, reglas, errores, criterios Dado/Cuando/Entonces, tareas, pruebas esperadas y decisión de revisión previa. El recuento es S01=8, S02=8, S03=8, S04=9, S05=10: **43 criterios**, relacionados en `docs/matriz-spec-codigo.md` con rutas y nombres de pruebas.

**Evidencia de pruebas histórica:** una captura proporcionada por el equipo muestra `56 passed in 20.25s` sobre su instalación local después de cambios de interfaz. También hay una ejecución de CI anterior con trabajo `pytest` exitoso: [GitHub Actions #38017818628](https://github.com/nagiberrioreales-design/reparacampus/actions/runs/38017818628). Estos resultados **no equivalen a una ejecución de pytest sobre esta rama de documentación**; los resultados del nuevo PR deben comprobarse por separado.

**Conclusión limitada:** la lectura no identificó contradicciones evidentes entre las reglas principales y sus funciones correspondientes. Sin embargo, no se ha acreditado una nueva verificación humana criterio por criterio ni la ausencia absoluta de defectos. En particular, las preguntas de `docs/preguntas-cliente.md` continúan como supuestos, no decisiones del cliente.

**Revisión requerida:** Henry debe verificar las 43 correspondencias con resultados observados, ejecutar o presenciar las pruebas de la revisión final, registrar diferencias reales y dejar su decisión como comentario o commit desde su cuenta. Otro integrante debe revisar el PR. No debe atribuirse a Henry esta inspección asistida.

## Inspección que debe realizar Henry

Marcar únicamente después de verificar cada punto con el archivo SPEC, el código y las pruebas.

| SPEC / RF | AC | Qué revisar | Resultado / evidencia |
|---|---:|---|---|
| [S01 / RF01](../specs/S01-registro.md) | 8 | Catálogos permitidos; longitudes 19, 20, 500 y 501; rol; autor de sesión; incidencia y evento atómicos; texto escapado | PENDIENTE |
| [S02 / RF02](../specs/S02-priorizacion-asignacion.md) | 8 | Riesgo y prioridad; técnico activo; solo coordinador; REGISTRADA → ASIGNADA; no reasignación | PENDIENTE |
| [S03 / RF03](../specs/S03-atencion-solucion.md) | 8 | Solo técnico asignado; estados válidos; solución 19, 20, 800, 801; historial | PENDIENTE |
| [S04 / RF04](../specs/S04-validacion-reapertura.md) | 9 | Propiedad; motivo 9, 10, 300, 301; 48 h exactas y un instante después; conservación de técnico/soluciones | PENDIENTE |
| [S05 / RF05](../specs/S05-consulta-historial.md) | 10 | Permisos, filtros, historial, tablero; porcentaje con cero registros; escapado y acceso ajeno 403 | PENDIENTE |

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

- [ ] Comprobé individualmente las cinco SPECS y sus 43 criterios.
- [ ] Comprobé rutas, pruebas y resultados de la matriz.
- [ ] Contrasté permisos y transiciones con el enunciado original.
- [ ] Ejecuté `python -m pytest -q` y registré el resultado y SHA de esta rama.
- [ ] Registré diferencias reales encontradas o justifiqué por qué no existen.
- [ ] Un integrante diferente revisó el PR.
- [ ] Actualicé el PDF final con mi aporte realmente efectuado.

## Datos por completar después de ejecutar

| Evidencia | Valor verificado |
|---|---|
| Fecha/hora | PENDIENTE |
| Rama documental anterior | `docs/revision-specs-henry` (PR #19, ya fusionado) |
| Rama de la inspección asistida | `docs/auditoria-tecnica-specs` |
| Commit SHA | PENDIENTE |
| Pull Request | PENDIENTE |
| Usuario GitHub responsable | PENDIENTE |
| Revisor de otro integrante | PENDIENTE |
| Pruebas (comando, n.º aprobadas, fallidas, evidencia) | PENDIENTE |
| Hallazgos y correcciones | PENDIENTE |
| Decisión humana final, con justificación | PENDIENTE |

**Nota de integridad académica:** este registro ha sido preparado con ayuda de IA como plantilla y corrección documental. No equivale a una auditoría personal realizada por Henry, ni se debe afirmar que Henry escribió el cambio o aprobó revisiones que no ejecutó.
