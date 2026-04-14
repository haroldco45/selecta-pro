# SelectaPro — Sistema de Selección de Personal 🇨🇴

![SelectaPro](https://img.shields.io/badge/SelectaPro-v2.0-1e3a5f?style=for-the-badge)
![HTML](https://img.shields.io/badge/HTML5-Single%20File-e34f26?style=for-the-badge&logo=html5&logoColor=white)
![License](https://img.shields.io/badge/Licencia-Propietaria-red?style=for-the-badge)
![Colombia](https://img.shields.io/badge/Normativa-Colombia-yellow?style=for-the-badge)

**SelectaPro** es una aplicación web de selección de personal diseñada para empresas colombianas. Funciona como un único archivo HTML — sin servidores, sin instalaciones, sin internet requerido. El administrador personaliza la app con el logo, nombre de empresa y sus propias áreas y preguntas. Solo descarga, configura y empieza a evaluar candidatos.

---

## ✨ Características principales

- **Panel de administración** protegido con contraseña — 3 secciones: Empresa, Áreas y pruebas, Seguridad
- **Gestor completo de áreas y pruebas psicotécnicas** — agrega, edita, renombra y elimina áreas y preguntas sin tocar el código
- **Editor de preguntas** por sección — crea preguntas de selección múltiple o escala Likert, edita opciones y respuesta correcta
- **Dos modalidades** de evaluación: Candidato a Empleo y Practicante SENA
- **Entrevista estructurada** en 3 bloques con calificación por estrellas (1–5) y campo de observaciones
- **Prueba psicotécnica + técnica** adaptada automáticamente según el área seleccionada
- **Puntaje combinado** (55% entrevista + 45% prueba) con veredicto automático de aptitud
- **Informe PDF** profesional con logo, nombre de empresa, detalle completo y concepto del entrevistador
- **Checklist legal** basado en normativa colombiana vigente
- **100% offline** — funciona desde cualquier navegador sin conexión a internet
- **Configuración persistente** — los cambios se guardan automáticamente en el navegador

---

## 🚀 Cómo usar

### 1. Descarga el archivo
Descarga `SelectaPro_v2.html` desde este repositorio.

### 2. Abre en el navegador
Haz doble clic en el archivo o ábrelo con Chrome, Edge o Firefox.

### 3. Configura tu empresa
Al abrirlo por primera vez aparecerá el panel de administración. Ingresa la contraseña por defecto:

```
selectapro2024
```

Sube el logo, escribe el nombre de tu empresa y personaliza las áreas con tus propias preguntas.

### 4. Empieza a evaluar
Selecciona el tipo de candidato, completa los datos, realiza la entrevista, aplica la prueba psicotécnica y genera el informe PDF.

---

## 🔐 Panel de administración

El panel tiene tres pestañas:

### 🏢 Empresa
| Campo | Descripción |
|-------|-------------|
| **Nombre de la empresa** | Aparece en el encabezado y en todos los informes PDF |
| **Slogan** | Subtítulo descriptivo (opcional) |
| **Logo** | PNG, JPG o SVG — máx. 2MB. Se guarda localmente en el navegador |

### 📋 Áreas y pruebas
Gestor completo de áreas psicotécnicas:

| Acción | Descripción |
|--------|-------------|
| **Ver áreas** | Lista todas las áreas con número de secciones y preguntas |
| **Agregar área** | Crea una nueva área con preguntas de ejemplo listas para editar |
| **Renombrar área** | Cambia el nombre de cualquier área existente |
| **Eliminar área** | Elimina el área y todas sus preguntas |
| **Editar preguntas** | Abre el editor completo de preguntas por sección |

**Dentro del editor de preguntas:**
- Agregar preguntas de selección múltiple (con 4 opciones y respuesta correcta) o escala Likert
- Editar el texto, opciones y respuesta correcta de cualquier pregunta existente
- Eliminar preguntas individuales
- Agregar, renombrar y eliminar secciones dentro de un área

### 🔐 Seguridad
Cambia la contraseña de administrador en cualquier momento. Contraseña por defecto: `selectapro2024`

> El botón **⚙ Configurar** en la esquina superior derecha abre el panel desde cualquier paso de la evaluación.

---

## 📋 Flujo de evaluación

```
Datos del candidato
       ↓
Entrevista — Bloque 1: Competencias Técnicas
       ↓
Entrevista — Bloque 2: Competencias Conductuales
       ↓
Entrevista — Bloque 3: Actitud y Valores
       ↓
Introducción a la prueba psicotécnica
       ↓
Prueba — Bloque 1: Razonamiento lógico / numérico
       ↓
Prueba — Bloque 2: Conocimientos técnicos del área
       ↓
Prueba — Bloque 3: Perfil conductual (Likert)
       ↓
Resultado final + Informe PDF
```

---

## 📊 Áreas incluidas por defecto

La app viene con 5 áreas preconfiguradas. Todas son editables, renombrables y eliminables:

| Área | Contenido de la prueba |
|------|------------------------|
| Comercial / Ventas | Razonamiento numérico, técnicas de venta, facturación colombiana |
| Bodega y Logística | Cálculo de cargas, inventario, PEPS, picking, remisiones |
| Contabilidad y Finanzas | Ecuación contable, IVA, retenciones, DIAN, RUT |
| Recursos Humanos | CST, SGSST, clima organizacional, onboarding, Ley 1010 |
| Sistemas e IT | Lógica, bases de datos, redes, SQL, ciberseguridad |

Cada área incluye una sección de **perfil conductual** con escala Likert.

---

## ⚖️ Normativa colombiana incluida

| Norma | Aplicación |
|-------|-----------|
| Ley 1581 de 2012 (Habeas Data) | Aviso de privacidad en recolección de datos |
| Decreto 1377 de 2013 | Tratamiento autorizado de datos personales |
| Art. 26 C.N. / Ley 931 de 2004 | Prohibición de preguntas discriminatorias |
| Art. 57 CST | Derecho del empleador a verificar idoneidad del candidato |
| Ley 1010 de 2006 | Prevención de acoso laboral |
| Ley 1709 de 2014 | Restricción sobre antecedentes penales |
| Decreto 055 de 2015 | ARL obligatoria para practicantes SENA |
| Ley 789 de 2002, Art. 30–32 | Contrato de aprendizaje SENA |

---

## 📊 Criterios de aptitud

| Puntaje | Veredicto |
|---------|-----------|
| ≥ 80% | ✅ APTO — Altamente recomendado |
| 65% – 79% | ✅ APTO — Con seguimiento recomendado |
| 50% – 64% | ⚠️ EN CONSIDERACIÓN — Evaluación adicional |
| < 50% | ❌ NO APTO — No se recomienda continuar |

---

## 🛠️ Requisitos técnicos

- Cualquier navegador moderno: **Chrome**, **Edge**, **Firefox** o **Safari**
- No requiere internet, servidor ni instalación
- Compatible con Windows, macOS y Linux
- Tamaño del archivo: ~84 KB

---

## 📁 Estructura del repositorio

```
selectapro/
│
├── SelectaPro_v2.html      # Aplicación completa (único archivo)
└── README.md               # Este documento
```

---

## 📌 Historial de versiones

| Versión | Fecha | Cambios |
|---------|-------|---------|
| v2.0 | Abril 2026 | Panel de administración completo — gestor de áreas y preguntas, editor por sección, agregar/editar/eliminar áreas |
| v1.0 | Abril 2026 | Lanzamiento inicial — 5 áreas fijas, configuración de logo y nombre |

---

## 👨‍💻 Desarrollado por

**Vibras Positivas HM**
Desarrollo de soluciones digitales prácticas para empresas colombianas.

> *Desarrollada por Vibras Positivas HM — Derechos de Autor Reservados.*

---

## 📄 Licencia

Este software es propiedad de **Vibras Positivas HM**. Todos los derechos reservados.

No está permitido copiar, modificar, distribuir ni usar este software sin autorización expresa del titular. Para licenciamiento comercial, contactar al desarrollador.

---

## 📞 Contacto y soporte

¿Necesitas personalización adicional, integración con tu sistema o una versión con nuevas funcionalidades?

Contáctanos para cotizar una versión a la medida para tu empresa.
