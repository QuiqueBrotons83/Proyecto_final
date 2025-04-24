
# ⚙️ Segundo Entregable: ETL y Preprocesamiento de Datos

## 1. Descripción del Pipeline ETL

El proceso ETL (Extract, Transform, Load) desarrollado en este proyecto incluye:

### 🔹 Extracción:
- El dataset fue descargado desde Kaggle utilizando la API oficial de Kaggle.
- Dataset original: [Amazon Products Dataset - Lokesh Parab](https://www.kaggle.com/datasets/lokeshparab/amazon-products-dataset)
- El archivo `.zip` se descomprimió y se combinaron múltiples archivos CSV en un único DataFrame.

### 🔹 Transformación:
- Se eliminaron columnas irrelevantes como `Unnamed: 0`, `image`, `link`.
- Se transformaron columnas de texto numérico (`actual_price`, `discount_price`, `no_of_ratings`) a tipos numéricos válidos.
- Se imputaron valores nulos en `ratings` (usando la mediana por categoría) y `discount_price` (rellenando con el valor de `actual_price` si no existía).
- Se creó la columna `discount_percent` para representar el porcentaje de descuento aplicado a cada producto.
- Se eliminaron filas con valores nulos críticos (`ratings`, `actual_price`) y se generó un nuevo DataFrame limpio (`df_eda`).

### 🔹 Carga:
- El dataset limpio fue exportado como `amazon_data_clean.csv`.
- Se utilizó SQLAlchemy y psycopg2 para cargar los datos en una base de datos PostgreSQL.
- El dataset se importó a DBeaver para su visualización, consultas y posterior conexión con Power BI.

---

## 2. Herramientas y Librerías Utilizadas

| Herramienta        | Uso                                       |
|--------------------|--------------------------------------------|
| **Python**         | Programación principal                     |
| **Pandas / NumPy** | ETL, transformación y manejo de datos      |
| **Kaggle API**     | Descarga automatizada del dataset          |
| **SQLAlchemy**     | Conexión y carga de datos a PostgreSQL     |
| **psycopg2**        | Motor de conexión para PostgreSQL          |
| **PostgreSQL + DBeaver** | Base de datos y gestión visual       |
| **Jupyter / VS Code** | Desarrollo y testing                    |

---

## 3. Resultado del Dataset Procesado

- Dataset final limpio: `amazon_data_clean.csv`
- Total de registros tras limpieza: más de **X mil** productos (ajustar según el conteo final)
- Columnas clave:  
  - `name`, `main_category`, `sub_category`
  - `ratings`, `no_of_ratings`
  - `actual_price`, `discount_price`, `discount_percent`

