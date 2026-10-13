# Contribuciones del equipo y cierre

El examen se trabajó con el mismo equipo del proyecto integrador. Para esta entrega decidimos dejar una evidencia sencilla de qué revisó o aportó cada integrante.

| Integrante | Aporte o tarea | Evidencia actual | Revisión de otra persona | Estado |
|---|---|---|---|---|
| Henry Berrio | Organización del repositorio e integración S01–S05; cotejo guiado asistido de 43 criterios, refuerzo de nueve casos automatizados y documentación de siete límites de cobertura | PR #6–#11; [PR #22](https://github.com/nagiberrioreales-design/reparacampus/pull/22) aprobado y fusionado a `main` (12/10/2026; SHA `f982945598c6143ee0ca6eea15cdeea7c07fab00`). Local: 58 pruebas; CI del PR: 67 aprobadas. | Henry revisó y aprobó el PR #18 de Steven Reyes. La cuenta distinta `gmtalentscompany-source` aprobó el PR #22 antes de fusionarlo. | Aporte verificable; siete observaciones de aserciones parciales permanecen documentadas. |
| Steven Reyes | Revisión previa de S01–S05 y de las implementaciones RF01–RF05; documentación de verificación manual de permisos | `APPROVED` desde `stivenuwu670` en PR #6 y PR #16; autor de [PR #18](https://github.com/nagiberrioreales-design/reparacampus/pull/18), fusionado | Henry (`nagiberrioreales-design`) aprobó PR #18 antes del merge | Evidencia verificada; no se atribuyen revisiones que no consten en GitHub. |
| Juan González | Revisión de estados, permisos y secuencia; propuesta adicional de interfaz para RF02/RF05 | [Issue #12](https://github.com/nagiberrioreales-design/reparacampus/issues/12) comentado desde `GM-Talent` y `APPROVED` en PR #16. [PR #25](https://github.com/nagiberrioreales-design/reparacampus/pull/25) se describe como aporte de Juan, pero su autor GitHub es `gmtalentscompany-source` | PR #25 recibió `APPROVED` desde `nagiberrioreales-design`, pero **sigue abierto, no fusionado y con conflicto de integración** | Revisión asignada completada; cambios nuevos de PR #25 no forman parte de `main`. |
| Leyter López | Revisión de modelo de datos y de consistencia entre transiciones, soluciones y eventos | [Issue #13](https://github.com/nagiberrioreales-design/reparacampus/issues/13) comentado desde `leiter11447-crypto`, cerrado; `APPROVED` en [PR #16](https://github.com/nagiberrioreales-design/reparacampus/pull/16) | Revisión cruzada documentada y aprobada en PR #16 | Tarea asignada completada; no consta validación personal adicional del último `main`. |
| Milton Ramírez | Revisión de límites, permisos, integraciones INT-01/02/03 y validación local histórica | [Issue #14](https://github.com/nagiberrioreales-design/reparacampus/issues/14) cerrado y `APPROVED` en PR #16 desde `Bellator07`. [PR #27](https://github.com/nagiberrioreales-design/reparacampus/pull/27) contiene informe propio con **56 pruebas locales** sobre SHA histórico; su GitHub Actions #38320811442 concluyó con **67 pruebas** | PR #27 **continúa abierto y sin revisión `APPROVED` registrada** | Revisión original completada; informe ampliado de PR #27 pendiente de revisión, actualización y decisión de integración. |
| Santiago Hernández | Verificación de instalación, README, UML/arquitectura, trazabilidad y regresión local de `main` | [Issue #15](https://github.com/nagiberrioreales-design/reparacampus/issues/15) cerrado; PR #23, #24, #26, #28 y [#30](https://github.com/nagiberrioreales-design/reparacampus/pull/30) de `snt-10` fusionados. [Verificación](verificacion-final-santiago.md) local: **67 pruebas**, SHA `1176f261a976…` | CI del PR #30: **67 pruebas** aprobadas. No se localizó `APPROVED` independiente en PR #28/#30 | Aporte documental y regresión verificados; falta cotejar el PDF y SHA/tag definitivos del equipo. |

## Estado de las evidencias del equipo

Las evidencias personales de Juan, Leyter, Milton y Santiago ya están registradas en GitHub. Henry también completó la revisión cruzada mediante el PR #18 de Steven Reyes. Además, la auditoría posterior de Henry (PR #22) recibió revisión independiente `APPROVED` y se fusionó a `main`; esa aprobación no equivale a certificar cobertura exhaustiva de los siete criterios con aserciones parciales. En este punto, los seis integrantes cuentan con **alguna evidencia verificable** en el repositorio, pero ello no acredita la terminación al 100 % de las integraciones ni la aprobación del PDF final.

## Estado consolidado de PR y pruebas — comprobado el 12/10/2026

- **Integrados:** la implementación S01–S05 (PR #7–#11), el cierre base PR #16, la auditoría PR #22 de Henry y los PR documentales #23, #24, #26, #28, #30 de Santiago. Steven publicó PR #18, también fusionado.
- **Pendientes:** [PR #25](https://github.com/nagiberrioreales-design/reparacampus/pull/25) (mejoras visuales RF02/RF05) permanece abierto con aprobación registrada, pero con estado no fusionable; [PR #27](https://github.com/nagiberrioreales-design/reparacampus/pull/27) (informe adicional de Milton) permanece abierto sin aprobación formal y con estado no fusionable. No se presentan como entregados en `main`.
- **Pruebas de versiones diferentes:** Henry obtuvo **58 aprobadas** en copia temporal sin correspondencia SHA verificada; Santiago documentó **67 aprobadas** localmente sobre `1176f261a976...`; CI del PR #30 **67 aprobadas** en [ejecución #38323411541](https://github.com/nagiberrioreales-design/reparacampus/actions/runs/38323411541). El informe de Milton en PR #27 refiere **56 locales** de otra versión y el CI del PR #27 pasó **67**. No se suman ni mezclan estos resultados.
- **Versión de entrega:** el tag histórico `release-examen` corresponde a `b7988274e6173dc13158fd112657e6dc512eb6e0`, mientras `main` ha recibido commits posteriores, incluidos los de rectificación documental. La versión definitiva, las pruebas sobre ese SHA y el PDF IEEE final todavía requieren acuerdo del equipo.
- **Proyecto GitHub:** el estado exacto del tablero requiere verificación directa o captura actual antes de declararlo cerrado.

## Aceptación del equipo

La aceptación final de la entrega se registrará cuando se hayan comprobado las siguientes condiciones:

1. GitHub Actions ejecutado sobre la versión definitiva y con resultado documentado.
2. Revisión del PR de cierre y resolución de los comentarios que correspondan.
3. Estado de los Issues #12, #13, #14 y #15 comprobado en GitHub.
4. Referencia del tag `release-examen` verificada y versión final acordada por el equipo, sin modificar el tag sin autorización.
5. PDF definitivo revisado y enlaces comprobados.

Las evidencias individuales descritas en este documento no sustituyen la comprobación de estos requisitos de cierre.
