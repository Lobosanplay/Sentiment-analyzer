# Sentiment Analyzer - Análisis de Sentimiento en Español
## 📋 Descripción del Proyecto
Este proyecto implementa un analizador de sentimientos para reseñas de películas en español, utilizando dos enfoques diferentes:

1. Enfoque basado en diccionario léxico (pysentiment)
2. Enfoque basado en aprendizaje automático (scikit-learn)

El objetivo es clasificar reseñas de películas como positivas o negativas utilizando técnicas de procesamiento de lenguaje natural (NLP).

## 📁 Estructura del Proyecto
```text
📦src
 ┣ 📂data (Aca puedes guardar tu Dataset par probar)
 ┃ ┗ 📜BBDD.xlsx
 ┃ ┗ 📜sentiment_analysis.csv 
 ┣ 📂pysentiment
 ┃ ┗ 📜sentiment_analyzer_with_pysentiment.py    # Enfoque basado en diccionario
 ┗ 📂scikit-learn
 ┃ ┗ 📜sentiment_analyzer_with_pysentiment.ipynb # Enfoque basado en ML (Logistic Regression)
```

## 📊 Dataset
Si quieres encontrar Datasets para tus pruebas puedes buscar por [kaggle](https://www.kaggle.com/)
El dataset debe contener columnas con estos nombres para su funcionamiento:

Dataset de BBDD.xlsx:
Este dataset cuenta con 50000 rows
Las columnas mas importantes son: **sentimiento**, **review_es** (Porque son valores que estan en español pero **review_es y sentiment** Tambien funcionan)

Columnas:
- review_en: Reseña en inglés
- review_es: Reseña en español
- sentiment: Etiqueta de sentimiento en inglés (positive/negative)
- sentimiento: Etiqueta de sentimiento en español (positivo/negativo)

Dataset de sentiment_analysis.csv:
Este dataset solo cuenta con 500 rows (Se planea cambiarlo por una mas grande al futuro).
Las columnas mas importantes son: **text**, **sentiment**

Columnas:
- Year: Año de publicacion
- Month: Mes de publicacion
- Day: Dia de publicacion
- Time of Tweet: Tiempo desde la publicacion del tweet
- text: Contenio del tweet
- sentiment: Sentimiento que refleja el tweet (positive/negative/neutral)
- Platform: En que plataforma se hizo el tweet

## 🛠️ Requisitos
```txt
numpy
pandas
seaborn
matplotlib
scikit-learn
jupyter (para el notebook)
```

## 🚀 Uso
Para el enfoque basado en diccionario (pysentiment):
```bash
cd src/pysentiment
python sentiment_analyzer_with_pysentiment.py
Para el enfoque basado en ML (scikit-learn):
```

```bash
cd src/scikit-learn
jupyter notebook sentiment_analyzer_with_pysentiment.ipynb
```

## 📈 Resultados Actuales

<table>
    <tr>
        <th>Métrica</th>
        <td>Precisión</td>
    </tr>
    <tr>
        <th>Entrenamiento</th>
        <td>87.87%</td>
    </tr>
    <tr>
        <th>Prueba</th>
        <td>55.68%</td>
    </tr>
</table>

**Nota**: El modelo actual muestra sobreajuste significativo. Se recomiendan las correcciones mencionadas para mejorar la generalización.

### 📚 Referencias
- Documentación de [scikit-learn](https://scikit-learn.org/)
- TF-IDF Vectorization
- Logistic Regression para clasificación de texto
- Técnicas de evaluación de modelos de ML