# Cotejo técnico de la matriz de 43 criterios — ReparaCampus

**Fecha:** 12/10/2026  
**Rama:** `docs/auditoria-tecnica-specs`  
**Referencia de auditoría:** [PR #22](https://github.com/nagiberrioreales-design/reparacampus/pull/22)  
**Naturaleza:** inspección documental y estática inicialmente asistida por IA; esa inspección, por sí sola, **no constituye aprobación personal ni revisión independiente**.

**Actualización posterior verificada:** Henry participó en un cotejo guiado de 43/43 criterios con asistencia de IA; una cuenta diferente, `gmtalentscompany-source`, aprobó formalmente el [PR #22](https://github.com/nagiberrioreales-design/reparacampus/pull/22) el **12/10/2026 22:57:42 UTC**, y el PR se **fusionó a `main`** el **12/10/2026 23:07:33 UTC**. Commit de fusión: `f982945598c6143ee0ca6eea15cdeea7c07fab00`. Esta revisión no elimina automáticamente las siete observaciones de aserciones parciales de la matriz.

## Alcance verificado

- Cinco SPECS v0.1 cotejadas: S01 = 8, S02 = 8, S03 = 8, S04 = 9 y S05 = 10: **43 criterios distintos**.
- La matriz `docs/matriz-spec-codigo.md` contiene los 43 identificadores, cada uno con comportamiento esperado, código, prueba y efecto esperado.
- Se comprobó contra los archivos del repositorio que **todas las funciones test_ expresamente citadas por nombre existen**. Las menciones «misma prueba» remiten a pruebas de la fila anterior.
- Se inspeccionó la implementación en `app/domain.py`, `app/incidents.py`, `app/reporting.py`, `app/auth.py`, las plantillas de historial/tablero y las pruebas de S01 a S05, integración y auditoría complementaria.
- **Último CI confirmado antes de este documento:** [GitHub Actions #38313354286](https://github.com/nagiberrioreales-design/reparacampus/actions/runs/38313354286), `tests/pytest`, **success**, commit `960e88d2a39fbd8a603ee300719fdcef39a3befd`. La ejecución con resultados explícitos registró **67 pruebas aprobadas** en [CI #38312929603](https://github.com/nagiberrioreales-design/reparacampus/actions/runs/38312929603). No se presupone que el commit generado por este documento ya tenga CI aprobado.

**Interpretación:** «Referencia localizada» confirma la existencia y relación documental de código/test; no equivale a una revisión manual firmada, ni a prueba exhaustiva de cada subcondición del criterio. Las observaciones siguientes identifican limitaciones concretas de la aserción en algunas filas.

## Cotejo criterio por criterio

| Criterio | Comportamiento resumido de la matriz | Resultado del cotejo de evidencia |
|---|---|---|
| AC-S01-01 | Datos válidos crean incidencia con código, autor de sesión, UTC y REGISTRADA | Referencia localizada; observación de cobertura |
| AC-S01-02 | Descripción de 19 caracteres se rechaza | Referencia localizada; observación de cobertura |
| AC-S01-03 | Descripción de 20 caracteres se acepta | Referencia localizada; sin contradicción evidente en el cotejo estático |
| AC-S01-04 | Más de 500 caracteres se rechaza | Referencia localizada; observación de cobertura |
| AC-S01-05 | Ubicación/categoría/impacto fuera del catálogo se rechaza | Referencia localizada; sin contradicción evidente en el cotejo estático |
| AC-S01-06 | Usuario no solicitante no registra | Referencia localizada; observación de cobertura |
| AC-S01-07 | Autor enviado por cliente no reemplaza usuario de sesión | Referencia localizada; sin contradicción evidente en el cotejo estático |
| AC-S01-08 | Texto parecido a HTML/script no se ejecuta | Referencia localizada; sin contradicción evidente en el cotejo estático |
| AC-S02-01 | Riesgo=true produce CRITICA | Referencia localizada; sin contradicción evidente en el cotejo estático |
| AC-S02-02 | Sin riesgo + ALTO produce ALTA | Referencia localizada; sin contradicción evidente en el cotejo estático |
| AC-S02-03 | Sin riesgo + BAJO produce NORMAL | Referencia localizada; sin contradicción evidente en el cotejo estático |
| AC-S02-04 | Coordinador asigna REGISTRADA a técnico activo | Referencia localizada; sin contradicción evidente en el cotejo estático |
| AC-S02-05 | Actor distinto de coordinador no asigna | Referencia localizada; sin contradicción evidente en el cotejo estático |
| AC-S02-06 | Técnico inactivo se rechaza | Referencia localizada; sin contradicción evidente en el cotejo estático |
| AC-S02-07 | Incidencia ya asignada no se reasigna | Referencia localizada; sin contradicción evidente en el cotejo estático |
| AC-S02-08 | Prioridad manipulada por cliente se ignora | Referencia localizada; sin contradicción evidente en el cotejo estático |
| AC-S03-01 | Técnico asignado inicia ASIGNADA → EN_ATENCION | Referencia localizada; sin contradicción evidente en el cotejo estático |
| AC-S03-02 | Otro técnico recibe 403 | Referencia localizada; observación de cobertura |
| AC-S03-03 | Estado incompatible no permite iniciar | Referencia localizada; sin contradicción evidente en el cotejo estático |
| AC-S03-04 | Solución 20–800 desde EN_ATENCION pasa a PENDIENTE_VALIDACION | Referencia localizada; sin contradicción evidente en el cotejo estático |
| AC-S03-05 | Solución de 19 se rechaza | Referencia localizada; sin contradicción evidente en el cotejo estático |
| AC-S03-06 | Solución de 801 se rechaza | Referencia localizada; sin contradicción evidente en el cotejo estático |
| AC-S03-07 | No se registra solución antes de EN_ATENCION | Referencia localizada; sin contradicción evidente en el cotejo estático |
| AC-S03-08 | Texto HTML/script de solución se muestra escapado | Referencia localizada; sin contradicción evidente en el cotejo estático |
| AC-S04-01 | Dueño confirma PENDIENTE_VALIDACION → CERRADA | Referencia localizada; sin contradicción evidente en el cotejo estático |
| AC-S04-02 | Otro solicitante no confirma | Referencia localizada; observación de cobertura |
| AC-S04-03 | Rechazo válido vuelve a EN_ATENCION y conserva técnico/solución | Referencia localizada; sin contradicción evidente en el cotejo estático |
| AC-S04-04 | Motivo 9/301 se rechaza | Referencia localizada; sin contradicción evidente en el cotejo estático |
| AC-S04-05 | Exactamente 48 h permite reapertura | Referencia localizada; sin contradicción evidente en el cotejo estático |
| AC-S04-06 | 48 h + 1 s se rechaza | Referencia localizada; sin contradicción evidente en el cotejo estático |
| AC-S04-07 | Coordinador no confirma ni reabre | Referencia localizada; sin contradicción evidente en el cotejo estático |
| AC-S04-08 | Cierres y soluciones previas se conservan en orden | Referencia localizada; sin contradicción evidente en el cotejo estático |
| AC-S04-09 | Operaciones inválidas no dejan efectos parciales | Referencia localizada; observación de cobertura |
| AC-S05-01 | Solicitante ve solo sus incidencias | Referencia localizada; sin contradicción evidente en el cotejo estático |
| AC-S05-02 | Técnico ve incidencias asignadas a él | Referencia localizada; sin contradicción evidente en el cotejo estático |
| AC-S05-03 | Coordinador combina estado y prioridad | Referencia localizada; sin contradicción evidente en el cotejo estático |
| AC-S05-04 | Historial ordenado incluye eventos y soluciones | Referencia localizada; sin contradicción evidente en el cotejo estático |
| AC-S05-05 | Historial no se edita ni borra | Referencia localizada; sin contradicción evidente en el cotejo estático |
| AC-S05-06 | Tablero cuenta estados, prioridades y críticas abiertas | Referencia localizada; sin contradicción evidente en el cotejo estático |
| AC-S05-07 | Porcentaje = CERRADAS/total × 100 con 1 decimal | Referencia localizada; sin contradicción evidente en el cotejo estático |
| AC-S05-08 | Sin registros muestra 0,0 % | Referencia localizada; sin contradicción evidente en el cotejo estático |
| AC-S05-09 | Texto persistido no se ejecuta como HTML/script | Referencia localizada; sin contradicción evidente en el cotejo estático |
| AC-S05-10 | Acceso directo no autorizado se rechaza | Referencia localizada; sin contradicción evidente en el cotejo estático |

## Observaciones de alcance de prueba

- **AC-S01-01:** La prueba de integración citada sí comprueba el estado, código y evento CREADA, pero no afirma explícitamente que requester_id provenga de la sesión ni que created_at tenga UTC; ambas reglas se observan por inspección de app/incidents.py.
- **AC-S01-02:** La prueba citada llama al validador de dominio y comprueba el error de 19 caracteres; no realiza una solicitud POST ni comprueba SQLite vacío.
- **AC-S01-04:** La prueba citada valida 501 caracteres en dominio; no realiza POST de registro ni comprueba ausencia de inserciones.
- **AC-S01-06:** La prueba de integración citada comprueba coordinador → HTTP 403 y base vacía. El caso adicional de acceso sin sesión se verifica en el decorador role_required mediante inspección de código; no tiene una aserción independiente en esta prueba.
- **AC-S03-02:** La prueba verifica 403 y estado ASIGNADA para otro técnico; no compara explícitamente los registros de eventos antes y después.
- **AC-S04-02:** La prueba verifica que otro solicitante no puede confirmar y conserva el estado; no inspecciona explícitamente todos los datos y eventos para afirmar ausencia total de efectos.
- **AC-S04-09:** Se ejecutan seis escenarios de operaciones inválidas y se comparan instantáneas completas de SQLite. Es cobertura representativa comprobada, no una demostración matemática de todos los escenarios posibles.

Las observaciones anteriores **no significan que los tests existentes estén fallando**. Significan que algunas afirmaciones de cobertura requieren contrastar conjuntamente los tests con la implementación, o añadir aserciones complementarias si se pretende acreditar cada efecto persistido directamente con tests.

## Cinco criterios técnicos reforzados

| Criterio | Evidencia complementaria ya publicada |
|---|---|
| AC-S03-07 | `test_ac_s03_07_solution_before_attention_preserves_all_persisted_data`: instantáneas antes/después de incidencia, eventos y soluciones. |
| AC-S04-08 | `test_ac_s04_08_and_s05_04_complete_history_in_chronological_order`: historial de rechazo, reapertura, soluciones y cierres; conserva actores, secuencia y fechas. |
| AC-S04-09 | `test_ac_s04_09_invalid_actions_have_no_partial_effects`: seis combinaciones de estado, motivo y plazo; instantáneas SQLite idénticas. |
| AC-S05-04 | Prueba compartida con AC-S04-08, con comprobación de HTML, orden de eventos, autores, fechas y soluciones. |
| AC-S05-06 | `test_ac_s05_06_dashboard_exact_state_priority_and_open_critical_counts`: siete incidencias, métricas exactas y porcentaje 28,6 %. |

Pruebas localizadas en `tests/test_auditoria_henry_criteria.py`. Los nueve casos parametrizados y no parametrizados de esta batería están incluidos en la ejecución con 67 aprobadas.

## Estado de las revisiones y pendientes posteriores

- [x] Henry realizó un **cotejo guiado de las 43 filas** frente a SPEC, código y pruebas, con asistencia de IA. Esta actividad quedó documentada en `docs/revision-specs-henry.md`; **no implica cobertura exhaustiva** de las subaserciones señaladas.
- [ ] No consta una declaración personal adicional de Henry, desde su cuenta, que cierre expresamente las siete limitaciones de aserciones o solicite nuevas pruebas. No se inventa esa declaración.
- [x] Una cuenta GitHub diferente (`gmtalentscompany-source`) revisó el PR #22 y registró **`APPROVED`** el 12/10/2026.
- [x] El PR #22 fue **fusionado** a la rama `main` el 12/10/2026, merge SHA `f982945598c6143ee0ca6eea15cdeea7c07fab00`.
- [ ] El equipo debe validar y aprobar el **PDF IEEE definitivo**, incorporando el aporte realmente realizado y todas sus evidencias con referencias actuales.

**Distinción necesaria:** cotejo asistido, revisión independiente del Pull Request, validación exhaustiva de criterios y aceptación del PDF definitivo son actividades diferentes. La revisión independiente está completada; los otros alcances se documentan según sus evidencias, sin asumir resultados que no se comprobaron.
