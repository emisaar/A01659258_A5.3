# 5.2 Ejercicio de programación 2 y análisis estático

## Compute Sales

Programa que calcula el costo total de ventas a partir de un catálogo de precios y un registro de ventas en formato JSON.

## Estructura

```
├── computeSales.py       # Programa principal
├── run_lint.sh           # Script de verificación PEP 8
├── tests/
│   ├── TC1/              # Caso de prueba 1 (catálogo + ventas)
│   ├── TC2/              # Caso de prueba 2 (cantidades grandes)
│   └── TC3/              # Caso de prueba 3 (datos inválidos)
└── results/              # Resultados generados
```

## Instalacion de dependencias

```bash
pip3 install -r requirements.txt
```

## Uso

```bash
python3 computeSales.py <catálogo_precios.json> <registro_ventas.json>
```

Ejemplo:

```bash
python3 computeSales.py tests/TC1/TC1.ProductList.json tests/TC1/TC1.Sales.json
```

Los resultados se imprimen en consola y se guardan en `results/SalesResults.txt`.

## Verificación de estilo

```bash
./run_lint.sh
```

Genera el reporte de flake8 y pylint en `results/lint_results.txt`.
