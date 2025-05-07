# Actualizar el contenido del entregable 3 con el texto real del notebook

eda_md_actualizado = """
# 🧾 Tercer Entregable – Análisis Exploratorio de Datos (EDA)

## 🎯 Objetivo del análisis
El objetivo de este análisis exploratorio es comprender mejor la estructura y distribución de los productos en Amazon, analizar la variabilidad entre categorías y detectar posibles oportunidades o anomalías que afecten la decisión entre modelos de negocio (Seller vs Vendor).

---

## 📊 Variables Analizadas
- `actual_price`: Precio original del producto
- `discount_price`: Precio final con descuento
- `ratings`: Valoración media (0 a 5)
- `no_of_ratings`: Cantidad de valoraciones recibidas
- `discount_percent`: Porcentaje de descuento aplicado

---

## 📈 Hallazgos clave

1. **Ratings**: La mayoría de los productos tienen calificaciones entre 4.0 y 4.5. Esto dificulta distinguir calidad solo por la media de valoraciones.
2. **Número de valoraciones**: Distribución altamente sesgada. Muchos productos tienen pocas reviews, unos pocos concentran miles. Se sugiere uso de escala logarítmica o percentiles.
3. **Precio original (`actual_price`)**: Concentración en rangos bajos pero con outliers extremos, lo que indica necesidad de depuración.
4. **Precio con descuento (`discount_price`)**: Comportamiento similar al precio original. Muchos productos tienen el mismo valor en ambas columnas (sin descuento).
5. **Porcentaje de descuento**: Pico claro entre el 50% y 60%, con un rango agresivo entre el 30% y 70%. Esto refleja la estrategia de Amazon.

---

## 🧠 Conclusión general del EDA numérico
Los datos muestran una plataforma con productos altamente valorados pero con gran desigualdad en visibilidad y precios. Los descuentos agresivos podrían ser un factor determinante en las decisiones de compra, y hay que considerar el sesgo de productos sin suficientes valoraciones. Además, se recomienda limpiar outliers extremos en precios.

---

## ✅ Recomendaciones
- Filtrar valores extremos en `actual_price` y `discount_price`
- Segmentar análisis por subcategoría para detectar oportunidades
- Incorporar visualizaciones clave en el dashboard final
