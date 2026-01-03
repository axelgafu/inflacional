Feature: Generación de Tabla de Reporte de Banxico
  Como economista
  Quiero generar automáticamente una tabla resumen de las reuniones de política monetaria de Banxico
  Para analizar la relación entre inflación, tasas de interés y tipo de cambio.

  Scenario: Generar reporte exitosamente
    Given un token de SIE válido
    And el año actual es 2026
    When ejecuto el generador de reportes
    Then debería ver una tabla Markdown con las fechas de las reuniones de 2026
    And las reuniones pasadas deben tener datos de inflación, tasa y variación FIX
    And las reuniones futuras deben tener celdas vacías
    And el reporte debe guardarse en un archivo con marca de tiempo
