# 📊 Informe de Entrenamiento del Modelo de Corrección Gramatical

Este documento resume el proceso de entrenamiento simulado de un modelo de corrección gramatical en inglés basado en una arquitectura tipo Transformer. El propósito fue desarrollar un componente central que pueda integrarse a herramientas educativas de apoyo al aprendizaje del inglés en zonas rurales de Colombia.

---

## 🧠 Arquitectura del Modelo

- **Tipo**: Transformer Encoder
- **Capas**: 6
- **Tamaño de capa oculta**: 512 unidades
- **Dropout**: 0.1
- **Parámetros totales (simulados)**: ~25M
- **Framework**: PyTorch (simulado)
- **Idioma de entrenamiento**: Inglés (en-US)

---

## 🗃️ Datos Utilizados

> ⚠️ Nota: los archivos de datos no están incluidos debido a restricciones de tamaño en GitHub.

- **Fuente**: [English Grammar Errors Corpus (Kaggle)](https://www.kaggle.com/datasets/yakobchuk/english-grammar-errors-corpus)
- **Tamaño simulado del corpus**:
  - **Ejemplos de entrenamiento**: 50,000 frases con errores
  - **Ejemplos de validación**: 5,000 frases
- **Preprocesamiento aplicado**:
  - Normalización de texto
  - Tokenización por sub-palabras
  - Eliminación de ruido

---

## ⚙️ Hiperparámetros

| Parámetro         | Valor     |
|-------------------|-----------|
| Epochs            | 3         |
| Batch Size        | 32        |
| Optimizer         | Adam      |
| Learning Rate     | 0.0005    |
| Warmup Steps      | 500       |
| Max Length        | 64 tokens |

---

## 📈 Resultados Simulados

| Métrica     | Valor       |
|-------------|-------------|
| Accuracy    | 87.5%       |
| F1 Score    | 0.89        |
| Precision   | 0.91        |
| Recall      | 0.88        |
| Tiempo total de entrenamiento | ~5 minutos (simulado) |

---

## 📉 Ejemplo de Aprendizaje

```text
Input:    "She go to school every days."
Target:   "She goes to school every day."
Predicción: "She goes to school every day." ✅
