# 📊 Streamlit Dashboard - Anuncios de Vehículos Usados

Este proyecto es parte del Sprint 7 del programa de ciencia de datos de TripleTen. El objetivo es crear una aplicación web interactiva que permita visualizar datos sobre anuncios de vehículos usados en Estados Unidos, utilizando `Streamlit` y `Plotly`.

## 🚗 Descripción de la App

La aplicación permite al usuario:

- Visualizar un **histograma** de la columna `odometer` (kilometraje de los autos).
- Explorar un **gráfico de dispersión** que relaciona `odometer` con el `price`.

Estos elementos permiten analizar la relación entre el uso de un vehículo y su precio en el mercado.

## 🧰 Tecnologías utilizadas

- Python 3
- Streamlit
- Pandas
- Plotly
- Pipenv (gestión de entorno virtual)

## ⚙️ Estructura del proyecto

```
.
├── app.py                # Código principal de la app
├── vehicles_us.csv       # Dataset de anuncios de vehículos
├── notebooks/
│   └── EDA.ipynb         # Análisis exploratorio inicial
├── Pipfile
├── Pipfile.lock
├── requirements.txt
└── README.md
```

## ▶️ Cómo ejecutar la app localmente

1. Clona el repositorio:
```bash
git clone https://github.com/tu_usuario/streamlit-dashboard.git
cd streamlit-dashboard
```

2. Instala las dependencias con pipenv:
```bash
pipenv install
pipenv shell
```

3. Ejecuta la app:
```bash
streamlit run app.py
```

## 🌐 Despliegue en Render

La app está desplegada en:  
👉 [https://tu-nombre.onrender.com](https://tu-nombre.onrender.com) ← *(agrega la URL cuando la tengas)*

---

## 🧠 Autor

Carlos Jiménez Hirashi  
Proyecto del Sprint 7 - TripleTen
