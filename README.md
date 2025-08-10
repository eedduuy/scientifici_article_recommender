# Recomendador de artículos científicos (WIP)

Este proyecto implementa un sistema de recomendación personalizado de artículos científicos usando técnicas modernas de NLP y aprendizaje profundo, incluyendo embeddings, autoencoders, transformers y modelos de lenguaje pequeños (SLMs).

---

## Objetivo

Construir un sistema que recomiende artículos relevantes a un usuario y justifique las recomendaciones mediante explicaciones generadas con un modelo de lenguaje fine-tuned. Se utilizará información semántica, embeddings, reducción de dimensionalidad, inyección de conocimiento y un modelo generativo.

---

## Componentes

- **Embeddings semánticos** de artículos científicos (abstracts) con Sentence Transformers.
- **Autoencoder** para reducción de dimensionalidad, detección de patrones latentes e inclusión de metadatos de artículos.
- **Sistema de recomendación** basado en similitud en espacio latente.
- **Generador de explicaciones** personalizado con un Small Language Model (SLM) ajustado.
- **Inyección de conocimiento** mediante ontologías científicas o estructuras jerárquicas.
- **Interfaz ligera** con Streamlit para interacción.

---

## Estructura del proyecto

```
scientific_article_recommender/
│
├── data/
│   ├── raw/               # Datos sin procesar (e.g. arXiv, S2ORC)
│   └── processed/         # Datos limpios y embeddings
│
├── models/
│   ├── autoencoder/       # Modelos entrenados del autoencoder
│   └── slm/               # Modelos ajustados para explicación
│
├── notebooks/             # Análisis exploratorio y pruebas
│
├── src/
│   ├── embedding/         # Scripts de extracción de embeddings
│   ├── autoencoder/       # Entrenamiento y aplicación del AE
│   ├── recommender/       # Recomendador basado en espacio latente
│   ├── generator/         # Generador de explicaciones personalizadas
│   └── ontology/          # Inyección de conocimiento y categorías científicas
│
├── app/                   # Interfaz en Streamlit
│
├── requirements.txt       # Librerías necesarias
├── config.py              # Rutas relativas a directorios y archivos, variables globales.
└── README.md              # Este archivo
```

---

## Tecnologías

- **Python 3.10+**
- `sentence-transformers` (embeddings)
- `torch`, `scikit-learn` (autoencoder, clustering)
- `transformers`, `peft`, `bitsandbytes` (SLM y ajuste fino)
- `faiss-cpu` (búsqueda de vecinos)
- `streamlit` (UI)
- `umap-learn` (visualización)

---

## Hoja de ruta y progreso

1. Recolección de artículos, análisis exploratorio y limpieza de abstracts. ✅
2. Generación de embeddings con `MiniLM`. ✅
3. Código del autoencoder y tratamiento de los metadatos para añadirlos al espacio latente. (WIP)
4. Entrenar autoencoder para obtener espacio latente. 
5. Simular perfiles de usuario.
6. Sistema de recomendación completo.
7. Fine-tuning de SLM para generar explicaciones.
8. Añadir inyección de conocimiento (ontologías científicas).
9. Construir interfaz web.

---



## 📄 Licencia

MIT
