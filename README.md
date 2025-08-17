# 📊 Streamlit Dashboard - Anuncios de Vehículos Usados

[![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-red?logo=streamlit)](https://streamlit.io/)
[![Plotly](https://img.shields.io/badge/Plotly-Graphs-orange?logo=plotly)](https://plotly.com/python/)
[![Deploy](https://img.shields.io/badge/Deploy-Render-success?logo=render)](https://dashboard-sprint-7.onrender.com)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

---

## 🚀 Descripción

**Streamlit Dashboard - Anuncios de Vehículos Usados** es una aplicación web interactiva diseñada para analizar datos de anuncios de autos usados en Estados Unidos.
Permite explorar la relación entre el **kilometraje (`odometer`)** y el **precio (`price`)** de los vehículos, ofreciendo una interfaz clara y visualmente atractiva para el análisis de mercado.

---

## ✨ Funcionalidades

* 📈 **Histograma dinámico** para visualizar la distribución del kilometraje (`odometer`).
* 🔍 **Gráfico de dispersión interactivo** que relaciona `odometer` y `price`.
* 🎨 Interfaz amigable basada en **Streamlit** con visualizaciones en **Plotly**.

---

## 🧰 Tecnologías

* [Python 3](https://www.python.org/) – lenguaje principal
* [Streamlit](https://streamlit.io/) – framework para dashboards interactivos
* [Pandas](https://pandas.pydata.org/) – manipulación y análisis de datos
* [Plotly](https://plotly.com/python/) – visualizaciones interactivas
* [Pipenv](https://pipenv.pypa.io/en/latest/) – gestión de entornos y dependencias

---

## ⚙️ Estructura del proyecto

```bash
.
├── app.py                # Código principal de la aplicación
├── vehicles_us.csv       # Dataset de anuncios de vehículos
├── notebooks/
│   └── EDA.ipynb         # Análisis exploratorio de datos inicial
├── Pipfile
├── Pipfile.lock
├── requirements.txt
└── README.md
```

---

## ▶️ Instalación y uso

1. **Clonar repositorio**

   ```bash
   git clone https://github.com/cjhirashi/streamlit-dashboard.git
   cd streamlit-dashboard
   ```

2. **Crear entorno e instalar dependencias**

   ```bash
   pipenv install
   pipenv shell
   ```

3. **Ejecutar aplicación**

   ```bash
   streamlit run app.py
   ```

---

## 🌐 Demo en línea

La aplicación está desplegada en Render:
👉 [https://dashboard-sprint-7.onrender.com](https://dashboard-sprint-7.onrender.com)

---

## 👨‍💻 Autor

**Carlos Jiménez Hirashi**
💼 Data Scientist Jr. | Python & Machine Learning

📧 \cjhirashi@gmail.com · 🌐 \LinkedIn: [cjhirashi](https://www.linkedin.com/in/cjhirashi)

---

## 📜 Licencia

Este proyecto está bajo la licencia **MIT** – consulta el archivo [LICENSE](LICENSE) para más detalles.

