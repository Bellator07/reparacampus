# Matriz SPEC versus código y pruebas

**Versión de SPECS evaluada:** 0.1  
**Revisión previa:** PR #6 aprobado por Steven Reyes antes de implementar.  
**Estado de esta matriz:** cotejo documental de 43 criterios (S01=8, S02=8, S03=8, S04=9, S05=10) y verificación automatizada complementaria. Las 37 referencias a funciones de prueba explícitamente nombradas en las filas corresponden a pruebas existentes. **La revisión independiente del PR #22 está completada:** `gmtalentscompany-source` registró `APPROVED` el 12/10/2026; el PR quedó fusionado a `main` (SHA `f982945598c6143ee0ca6eea15cdeea7c07fab00`). No significa que todas las subaserciones estén cubiertas exhaustivamente.

**Evidencia actual (12/10/2026):** `pytest -q` — **67 passed in 25.88s, 0 fallidas**. Commit de las pruebas: `a78b5a741c444dc2139e9ef38812f3b334c00091` · [GitHub Actions #38312929603](https://github.com/nagiberrioreales-design/reparacampus/actions/runs/38312929603) (éxito). Se amplió la suite mediante `tests/test_auditoria_henry_criteria.py` con nueve casos automatizados.

La lectura de cada fila es: requisito → criterio → comportamiento esperado → archivo que lo implementa → prueba que lo comprueba.

**Informe de auditoría documental:** [Cotejo asistido de los 43 criterios](cotejo-asistido-matriz-43-ac.md). Se localizaron las referencias y pruebas para las 43 filas. Siete criterios muestran **observaciones sobre aserciones que no comprueban explícitamente algún subefecto**; por transparencia, sus estados se marcan como cobertura de aserciones parcial. Henry realizó un cotejo guiado de los 43 criterios con asistencia de IA el 12/10/2026 y aportó una ejecución local de 58 pruebas aprobadas. El cotejo asistido no equivale por sí mismo a revisión independiente ni resuelve las siete observaciones de aserciones parciales. **La revisión externa sí se registró posteriormente:** `APPROVED` de `gmtalentscompany-source` en el [PR #22](https://github.com/nagiberrioreales-design/reparacampus/pull/22), fusionado el 12/10/2026. La rama del PR incluyó 67 pruebas aprobadas en CI.

## Cotejo guiado por Henry — 12/10/2026

Durante una revisión interactiva con asistencia de IA, Henry cotejó las **43 filas de aceptación** de esta matriz (S01=8, S02=8, S03=8, S04=9, S05=10) con funciones y pruebas compartidas. Se revisaron los comportamientos principales, sin convertir esta lectura en una aprobación independiente ni en certificación de cobertura exhaustiva.

**Evidencia local aportada:** Python 3.12 en Windows, copia temporal `%TEMP%\reparacampus_revision_henry`. Comando `py -3.12 -m pytest -q -p no:cacheprovider` → **58 passed in 21.84s, 0 fallidas**. Desglose de módulos: S01=14, S02=8, S03=13, S04=11, S05=9; la suite completa incorpora tres pruebas de integración adicionales. No se verificó equivalencia de commit SHA entre la copia temporal y el PR.

**Evidencia CI separada:** la rama del PR #22 contiene nueve pruebas adicionales, con **67/67 aprobadas** en [GitHub Actions #38312929603](https://github.com/nagiberrioreales-design/reparacampus/actions/runs/38312929603). El HEAD anterior a esta actualización documental (`fc2f36861cb8e2cb8f91fe944cc64736584f0f3e`) también pasó [GitHub Actions #38313756028](https://github.com/nagiberrioreales-design/reparacampus/actions/runs/38313756028).

**Estados de la matriz:** las siete filas identificadas como cobertura de aserciones parcial **no cambian de calificación** por este cotejo: AC-S01-01, AC-S01-02, AC-S01-04, AC-S01-06, AC-S03-02, AC-S04-02 y AC-S04-09. Recomendaciones complementarias: fallo forzado y rollback en S04-09; comprobación de cronología global por fecha en S05-04; conteos exactos del tablero en la copia local para S05-06 (ya reforzados en CI). Quedan pendientes la revisión independiente, la decisión formal y el PDF final.

## S01 / RF01 — Registrar

| Criterio | Comportamiento esperado | Código | Prueba / datos | Efecto esperado en SQLite | Estado |
|---|---|---|---|---|---|
| AC-S01-01 | Datos válidos crean incidencia con código, autor de sesión, UTC y REGISTRADA | `app/incidents.py` | `test_s01_registration_persists_incident_and_history` | 1 incidencia + 1 evento CREADA | Referencia localizada; cobertura de aserciones parcial (ver cotejo de 43 AC) |
| AC-S01-02 | Descripción de 19 caracteres se rechaza | `app/domain.py` | `test_s01_rejects_description_outside_limits[19]` | sin alta | Referencia localizada; cobertura de aserciones parcial (ver cotejo de 43 AC) |
| AC-S01-03 | Descripción de 20 caracteres se acepta | `app/domain.py` | `test_s01_accepts_valid_data` | validación sin error | Cumple en suite automatizada — 67 pruebas pasan en CI |
| AC-S01-04 | Más de 500 caracteres se rechaza | `app/domain.py` | `test_s01_rejects_description_outside_limits[501]` | sin alta | Referencia localizada; cobertura de aserciones parcial (ver cotejo de 43 AC) |
| AC-S01-05 | Ubicación/categoría/impacto fuera del catálogo se rechaza | `app/domain.py` | `test_s01_rejects_invalid_catalog_or_boolean` | sin alta | Cumple en suite automatizada — 67 pruebas pasan en CI |
| AC-S01-06 | Usuario no solicitante no registra | `app/auth.py`, `app/incidents.py` | `test_s01_non_requester_cannot_register_and_database_stays_unchanged` | 0 incidencias y 0 eventos | Referencia localizada; cobertura de aserciones parcial (ver cotejo de 43 AC) |
| AC-S01-07 | Autor enviado por cliente no reemplaza usuario de sesión | `app/incidents.py` | `test_s01_ignores_forged_author_and_escapes_stored_text` | requester_id = usuario autenticado | Cumple en suite automatizada — 67 pruebas pasan en CI |
| AC-S01-08 | Texto parecido a HTML/script no se ejecuta | Jinja + `app/templates/incidents/index.html` | misma prueba anterior | texto persiste, salida escapada | Cumple en suite automatizada — 67 pruebas pasan en CI |

## S02 / RF02 — Priorizar y asignar

| Criterio | Comportamiento esperado | Código | Prueba / datos | Efecto esperado en SQLite | Estado |
|---|---|---|---|---|---|
| AC-S02-01 | Riesgo=true produce CRITICA | `calculate_priority` | `test_s02_calculates_priority_on_server` | prioridad CRITICA | Cumple en suite automatizada — 67 pruebas pasan en CI |
| AC-S02-02 | Sin riesgo + ALTO produce ALTA | `calculate_priority` | misma prueba parametrizada | prioridad ALTA | Cumple en suite automatizada — 67 pruebas pasan en CI |
| AC-S02-03 | Sin riesgo + BAJO produce NORMAL | `calculate_priority` | misma prueba parametrizada | prioridad NORMAL | Cumple en suite automatizada — 67 pruebas pasan en CI |
| AC-S02-04 | Coordinador asigna REGISTRADA a técnico activo | `assign` | `test_s02_coordinator_assigns_active_technician_and_history` | estado ASIGNADA + evento | Cumple en suite automatizada — 67 pruebas pasan en CI |
| AC-S02-05 | Actor distinto de coordinador no asigna | autorización Flask | `test_s02_non_coordinator_cannot_assign` | incidencia sigue REGISTRADA | Cumple en suite automatizada — 67 pruebas pasan en CI |
| AC-S02-06 | Técnico inactivo se rechaza | consulta de técnico activo | `test_s02_inactive_technician_is_rejected_without_history_change` | no cambia estado ni historial | Cumple en suite automatizada — 67 pruebas pasan en CI |
| AC-S02-07 | Incidencia ya asignada no se reasigna | condición de estado/asignación | `test_s02_second_assignment_is_rejected_and_keeps_original_technician` | conserva técnico original; 1 evento ASIGNADA | Cumple en suite automatizada — 67 pruebas pasan en CI |
| AC-S02-08 | Prioridad manipulada por cliente se ignora | cálculo en servidor | `test_s02_coordinator_assigns_active_technician_and_history` envía NORMAL y espera ALTA | prioridad calculada ALTA | Cumple en suite automatizada — 67 pruebas pasan en CI |

## S03 / RF03 — Atender y registrar solución

| Criterio | Comportamiento esperado | Código | Prueba / datos | Efecto esperado en SQLite | Estado |
|---|---|---|---|---|---|
| AC-S03-01 | Técnico asignado inicia ASIGNADA → EN_ATENCION | `start_attention` | `test_s03_assigned_technician_starts_attention` | estado EN_ATENCION + evento | Cumple en suite automatizada — 67 pruebas pasan en CI |
| AC-S03-02 | Otro técnico recibe 403 | autorización por assigned_technician_id | `test_s03_other_technician_cannot_start_attention` | conserva ASIGNADA | Referencia localizada; cobertura de aserciones parcial (ver cotejo de 43 AC) |
| AC-S03-03 | Estado incompatible no permite iniciar | condición `state == ASIGNADA` | `test_s03_cannot_start_attention_from_incompatible_state` | sin evento nuevo | Cumple en suite automatizada — 67 pruebas pasan en CI |
| AC-S03-04 | Solución 20–800 desde EN_ATENCION pasa a PENDIENTE_VALIDACION | `propose_solution` | `test_s03_solution_moves_to_pending_validation_and_keeps_history` | solución + evento + nuevo estado | Cumple en suite automatizada — 67 pruebas pasan en CI |
| AC-S03-05 | Solución de 19 se rechaza | `validate_solution` | `test_s03_solution_limits[19-False]` | sin solución | Cumple en suite automatizada — 67 pruebas pasan en CI |
| AC-S03-06 | Solución de 801 se rechaza | `validate_solution` | `test_s03_solution_limits[801-False]` | sin solución | Cumple en suite automatizada — 67 pruebas pasan en CI |
| AC-S03-07 | No se registra solución antes de EN_ATENCION | condición de estado | `test_s03_cannot_propose_solution_before_starting_attention` + `test_ac_s03_07_solution_before_attention_preserves_all_persisted_data` | conserva ASIGNADA; 0 soluciones; sin eventos ni efectos parciales | Cumple en suite automatizada — 67 pruebas pasan en CI |
| AC-S03-08 | Texto HTML/script de solución se muestra escapado | Jinja + historial | `test_s03_solution_text_is_escaped_when_shown` | texto guardado sin ejecución | Cumple en suite automatizada — 67 pruebas pasan en CI |

## S04 / RF04 — Validar, rechazar y reabrir

| Criterio | Comportamiento esperado | Código | Prueba / datos | Efecto esperado en SQLite | Estado |
|---|---|---|---|---|---|
| AC-S04-01 | Dueño confirma PENDIENTE_VALIDACION → CERRADA | `confirm_solution` | `test_s04_owner_confirms_pending_solution_and_closes` | closed_at UTC + evento cierre | Cumple en suite automatizada — 67 pruebas pasan en CI |
| AC-S04-02 | Otro solicitante no confirma | `get_owned_incident` | `test_s04_other_requester_cannot_confirm` | conserva PENDIENTE_VALIDACION | Referencia localizada; cobertura de aserciones parcial (ver cotejo de 43 AC) |
| AC-S04-03 | Rechazo válido vuelve a EN_ATENCION y conserva técnico/solución | `reject_solution` | `test_s04_rejection_returns_to_attention_and_preserves_technician_and_solution` | evento de rechazo; misma asignación | Cumple en suite automatizada — 67 pruebas pasan en CI |
| AC-S04-04 | Motivo 9/301 se rechaza | `validate_reason` | `test_s04_reason_limits` + `test_s04_invalid_rejection_reason_has_no_effect` | sin evento de rechazo | Cumple en suite automatizada — 67 pruebas pasan en CI |
| AC-S04-05 | Exactamente 48 h permite reapertura | `reopen_incident` + reloj de servidor | `test_s04_reopen_exactly_48_hours_is_allowed` | EN_ATENCION + evento REABIERTA | Cumple en suite automatizada — 67 pruebas pasan en CI |
| AC-S04-06 | 48 h + 1 s se rechaza | misma función | `test_s04_reopen_after_48_hours_is_rejected_without_changes` | conserva CERRADA | Cumple en suite automatizada — 67 pruebas pasan en CI |
| AC-S04-07 | Coordinador no confirma ni reabre | autorización por rol | `test_s04_coordinator_cannot_confirm_or_reopen_for_requester` | 403; sin cambios | Cumple en suite automatizada — 67 pruebas pasan en CI |
| AC-S04-08 | Cierres y soluciones previas se conservan en orden | tablas `solutions` y `events` | `test_flow_close_reopen_new_solution_and_close_again` + `test_ac_s04_08_and_s05_04_complete_history_in_chronological_order` | 2 cierres, 1 reapertura, 1 rechazo y 3 soluciones ordenadas sin pérdida de historia | Cumple en suite automatizada — 67 pruebas pasan en CI |
| AC-S04-09 | Operaciones inválidas no dejan efectos parciales | transacciones + validación previa | `test_ac_s04_09_invalid_actions_have_no_partial_effects` (6 escenarios: estado, motivo y plazo) | instantáneas SQLite idénticas antes/después: incidencia, eventos y soluciones | Referencia localizada; cobertura de aserciones parcial (ver cotejo de 43 AC) |

## S05 / RF05 — Consultar e historizar

| Criterio | Comportamiento esperado | Código | Prueba / datos | Efecto esperado / salida | Estado |
|---|---|---|---|---|---|
| AC-S05-01 | Solicitante ve solo sus incidencias | `app/reporting.py` | `test_s05_requester_only_sees_own_incidents` | propia visible; ajena ausente | Cumple en suite automatizada — 67 pruebas pasan en CI |
| AC-S05-02 | Técnico ve incidencias asignadas a él | `app/reporting.py` | `test_s05_technician_only_sees_assigned_incidents` | asignada visible; otra ausente | Cumple en suite automatizada — 67 pruebas pasan en CI |
| AC-S05-03 | Coordinador combina estado y prioridad | filtros del listado | `test_s05_coordinator_combines_state_and_priority_filters` | solo coincidencia | Cumple en suite automatizada — 67 pruebas pasan en CI |
| AC-S05-04 | Historial ordenado incluye eventos y soluciones | vista `history` | `test_s05_history_contains_events_solutions_and_escapes_text` + `test_ac_s04_08_and_s05_04_complete_history_in_chronological_order` | orden de 10 eventos, autores, fechas, 3 soluciones, rechazo, cierres y reapertura verificado en SQLite y HTML | Cumple en suite automatizada — 67 pruebas pasan en CI |
| AC-S05-05 | Historial no se edita ni borra | solo ruta GET | `test_s05_history_has_no_edit_operation` | POST responde 405 | Cumple en suite automatizada — 67 pruebas pasan en CI |
| AC-S05-06 | Tablero cuenta estados, prioridades y críticas abiertas | `_dashboard` | `test_s05_dashboard_counts_and_close_percentage` + `test_ac_s05_06_dashboard_exact_state_priority_and_open_critical_counts` | 7 incidencias: conteos exactos por estado y prioridad, 2 críticas abiertas y cierre 28,6 % | Cumple en suite automatizada — 67 pruebas pasan en CI |
| AC-S05-07 | Porcentaje = CERRADAS/total × 100 con 1 decimal | `_dashboard` | misma prueba: 1/4 | muestra 25,0 % | Cumple en suite automatizada — 67 pruebas pasan en CI |
| AC-S05-08 | Sin registros muestra 0,0 % | `_dashboard` | `test_s05_dashboard_zero_records_is_zero_percent` | 0,0 % | Cumple en suite automatizada — 67 pruebas pasan en CI |
| AC-S05-09 | Texto persistido no se ejecuta como HTML/script | Jinja | `test_s05_history_contains_events_solutions_and_escapes_text` | salida escapada | Cumple en suite automatizada — 67 pruebas pasan en CI |
| AC-S05-10 | Acceso directo no autorizado se rechaza | `_authorized_incident` | `test_s05_direct_history_access_respects_permissions` | 403 | Cumple en suite automatizada — 67 pruebas pasan en CI |

## Recorridos de integración obligatorios

| ID | Recorrido | Prueba | Resultado esperado |
|---|---|---|---|
| INT-01 | registrar → asignar → iniciar → proponer → confirmar | `test_full_flow_register_assign_start_propose_confirm` | CERRADA e historial en orden |
| INT-02 | rechazo → nueva solución → confirmar | `test_flow_rejects_solution_and_accepts_new_solution` | 2 soluciones, 1 rechazo, CERRADA |
| INT-03 | cierre → reapertura → nueva solución → nuevo cierre | `test_flow_close_reopen_new_solution_and_close_again` | 2 cierres, 1 reapertura, 2 soluciones |

## Regresión

La suite final ejecuta también todas las pruebas de S01–S05. Una corrección del cierre no se aceptará si rompe una funcionalidad ya integrada.

## Auditoría complementaria — 12/10/2026

La inspección asistida por IA añadió `tests/test_auditoria_henry_criteria.py` con **9 casos** (uno S03-07, uno de secuencia para S04-08/S05-04, seis variantes de S04-09 y uno de S05-06). Su primera ejecución detectó una aserción de HTML mal planteada, porque contaba `ASIGNADA` tanto como acción como estado. Tras corregir la aserción, la segunda ejecución aprobó **67/67 pruebas** con cero fallas en [GitHub Actions #38312929603](https://github.com/nagiberrioreales-design/reparacampus/actions/runs/38312929603).

Estas comprobaciones acreditan **cobertura automatizada adicional y trazabilidad documental** de los cinco criterios reforzados; no constituyen por sí mismas una certificación humana del comportamiento completo. **Estado posterior comprobado:** `gmtalentscompany-source` aprobó el PR #22 el 12/10/2026 (22:57:42 UTC), y el PR se fusionó a `main` a las 23:07:33 UTC (merge `f982945598c6143ee0ca6eea15cdeea7c07fab00`). Las siete observaciones de cobertura parcial de aserciones siguen abiertas como límites de evidencia, no defectos confirmados. La versión IEEE definitiva del PDF debe reflejar el aporte, estas evidencias y los límites sin presentarlos como cobertura exhaustiva.
