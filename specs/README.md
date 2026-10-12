# Índice y trazabilidad de SPECS — ReparaCampus

**Estado documental comprobado:** 12/10/2026. **Línea base:** SPEC v0.1.
Esta actualización corrige el índice; no modifica requisitos, criterios, lógica, pruebas ni fechas históricas.

| RF | Historia / SPEC | Issue | AC | Revisión previa | Implementación |
|---|---|---|---:|---|---|
| RF01 | [S01 — Registrar](S01-registro.md) | #1 | 8 | [PR #6](https://github.com/nagiberrioreales-design/reparacampus/pull/6) | [PR #7](https://github.com/nagiberrioreales-design/reparacampus/pull/7) |
| RF02 | [S02 — Priorizar y asignar](S02-priorizacion-asignacion.md) | #2 | 8 | [PR #6](https://github.com/nagiberrioreales-design/reparacampus/pull/6) | [PR #8](https://github.com/nagiberrioreales-design/reparacampus/pull/8) |
| RF03 | [S03 — Atender y registrar solución](S03-atencion-solucion.md) | #3 | 8 | [PR #6](https://github.com/nagiberrioreales-design/reparacampus/pull/6) | [PR #9](https://github.com/nagiberrioreales-design/reparacampus/pull/9) |
| RF04 | [S04 — Validar, rechazar, reabrir](S04-validacion-reapertura.md) | #4 | 9 | [PR #6](https://github.com/nagiberrioreales-design/reparacampus/pull/6) | [PR #10](https://github.com/nagiberrioreales-design/reparacampus/pull/10) |
| RF05 | [S05 — Consultar e historizar](S05-consulta-historial.md) | #5 | 10 | [PR #6](https://github.com/nagiberrioreales-design/reparacampus/pull/6) | [PR #11](https://github.com/nagiberrioreales-design/reparacampus/pull/11) |

**Total:** cinco historias, cinco SPECS y 43 criterios de aceptación redactados en formato **Dado / Cuando / Entonces**.
Los PR #7–#11 figuran integrados en `main`. El índice anterior indicaba incorrectamente «pendiente de revisión» e «implementación no iniciada».

## Orden comprobado de revisión e implementación

El [PR #6](https://github.com/nagiberrioreales-design/reparacampus/pull/6) registra aprobación de `stivenuwu670` el **09/10/2026 a las 03:43 UTC** y fusión el mismo día a las **03:48 UTC**. El primer PR de implementación (#7) se abrió a las **03:52 UTC**. Esta revisión histórica corresponde al flujo original: **no se atribuye retrospectivamente a Henry**.

## Código y pruebas vinculadas

| RF | Código principal | Pruebas |
|---|---|---|
| RF01 | `app/domain.py`, `app/incidents.py` | `tests/test_s01_unit.py`, `tests/test_s01_integration.py` |
| RF02 | `app/domain.py`, `app/incidents.py` | `tests/test_s02_priority_assignment.py` |
| RF03 | `app/incidents.py` | `tests/test_s03_attention_solution.py` |
| RF04 | `app/incidents.py` | `tests/test_s04_validation_reopen.py` |
| RF05 | `app/reporting.py` | `tests/test_s05_query_history.py` |

Consultar la [matriz completa de los 43 AC](../docs/matriz-spec-codigo.md) y los [recorridos de integración](../tests/test_integration_flows.py).

## Resultados y revisión posterior

La ejecución [GitHub Actions #38017818628](https://github.com/nagiberrioreales-design/reparacampus/actions/runs/38017818628) terminó con el trabajo `pytest` exitoso. Después de incorporar cambios visuales, el equipo mostró por captura una ejecución local con **56 passed**; debe repetirse en cada rama antes de integrarla y vincularse al commit correspondiente.

La auditoría documental posterior asignada a Henry tiene un [registro de revisión pendiente](../docs/revision-specs-henry.md). **Su decisión humana no se considera completada hasta que él revise realmente y deje evidencia en el PR.**

## Preguntas abiertas

Las dudas y supuestos pendientes están documentados en [`docs/preguntas-cliente.md`](../docs/preguntas-cliente.md). Una respuesta de IA no se presenta como decisión del cliente.
