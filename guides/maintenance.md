# Mantener los datos

Usá un ID corto y estable para cada marca. Su lugar en el ranking puede cambiar sin cambiar el nombre de sus archivos.

Guardá el resultado de TasteLabs en `data/raw/<id>.json`, con URL y fecha de captura. Conservá `result.design_system` y las referencias a artefactos; omití identificadores de cuenta, créditos, claves y metadatos de sesión. Nunca pegues credenciales en enlaces públicos.

Después actualizá la ficha, los tokens y el catálogo. Las notas de selección deben identificarse como inferencias; una regla cromática extraída y una recomendación nuestra tienen distinto origen. Usá `limited` si detectás campos críticos vacíos o estilos que parecen haber fallado. Registrá el motivo en `warnings` tanto en el índice como en los tokens.

El índice usa las etiquetas de `catalog/taxonomy.json`. Para sumar una etiqueta, definí primero su significado. Actualizá también los índices agrupados, la tabla y `llms.txt` si cambia un punto de entrada.

`data/manifest.json` registra el hash SHA-256 de cada JSON original. Calculalo de nuevo cuando cambie ese archivo y conservá el cambio en Git. Ejecutá `python3 scripts/validate.py` y las pruebas antes de publicar; el validador comprueba rutas, hashes y avisos, pero no puede evaluar el diseño visual.

La búsqueda funciona sin servicios externos. No agregues una reextracción automática al flujo de consulta: además de consumir créditos, reemplazaría evidencia anterior sin una decisión explícita.
