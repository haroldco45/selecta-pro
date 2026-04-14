# SelectaPro — Sistema de Selección de Personal 🇨🇴

![SelectaPro](https://img.shields.io/badge/SelectaPro-v1.0-1e3a5f?style=for-the-badge)
![HTML](https://img.shields.io/badge/HTML5-Single%20File-e34f26?style=for-the-badge&logo=html5&logoColor=white)
![License](https://img.shields.io/badge/Licencia-Propietaria-red?style=for-the-badge)
![Colombia](https://img.shields.io/badge/Normativa-Colombia-yellow?style=for-the-badge)

**SelectaPro** es una aplicación web de selección de personal diseñada para empresas colombianas. Funciona como un único archivo HTML — sin servidores, sin instalaciones, sin internet requerido. Solo descarga, configura con el logo de tu empresa y empieza a entrevistar.

---

## ✨ Características principales

- **Panel de administración** protegido con contraseña para personalizar logo y nombre de empresa
- **Dos modalidades** de evaluación: Candidato a Empleo y Practicante SENA
- **Entrevista estructurada** en 3 bloques con calificación por estrellas (1–5) y campo de observaciones
- **Prueba psicotécnica + técnica** adaptada automáticamente según el área de la empresa:
  - Comercial / Ventas
  - Bodega y Logística
  - Contabilidad y Finanzas
  - Recursos Humanos
  - Sistemas e IT
- **Perfil conductual** con escala Likert incluido en cada prueba
- **Puntaje combinado** (55% entrevista + 45% prueba) con veredicto automático de aptitud
- **Informe PDF** profesional con logo de la empresa, detalle completo y concepto del entrevistador
- **Checklist legal** basado en normativa colombiana vigente
- **100% offline** — funciona desde cualquier navegador sin conexión a internet

---

## 🚀 Cómo usar

### 1. Descarga el archivo
Descarga `SelectaPro_v1.html` desde este repositorio.

### 2. Abre en el navegador
Haz doble clic en el archivo o ábrelo con Chrome, Edge o Firefox.

### 3. Configura tu empresa
Al abrirlo por primera vez aparecerá el panel de configuración. Ingresa la contraseña por defecto:

```
selectapro2024
```

Sube el logo de tu empresa, escribe el nombre y slogan, y guarda. ¡Listo!

### 4. Empieza a evaluar
Selecciona el tipo de candidato (Empleo o SENA), completa los datos, realiza la entrevista y la prueba psicotécnica, y genera el informe PDF al finalizar.

---

## 🔐 Panel de administración

| Campo | Descripción |
|-------|-------------|
| **Nombre de empresa** | Aparece en el encabezado y en todos los informes PDF |
| **Slogan** | Subtítulo descriptivo (opcional) |
| **Logo** | PNG, JPG o SVG — máx. 2MB. Se guarda localmente en el navegador |
| **Contraseña** | Personalizable. Por defecto: `selectapro2024` |

> El botón **⚙ Configurar** en la esquina superior derecha permite volver al panel en cualquier momento.

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

## ⚖️ Normativa colombiana incluida

| Norma | Aplicación |
|-------|-----------|
| Ley 1581 de 2012 (Habeas Data) | Aviso de privacidad en recolección de datos |
| Decreto 1377 de 2013 | Tratamiento autorizado de datos personales |
| Art. 26 C.N. / Ley 931 de 2004 | Prohibición de preguntas discriminatorias |
| Ley 1010 de 2006 | Prevención de acoso laboral |
| Ley 1709 de 2014 | Restricción sobre antecedentes penales |
| Art. 57 CST | Derecho del empleador a verificar idoneidad |
| Decreto 055 de 2015 | ARL obligatoria para practicantes SENA |
| Ley 789 de 2002, Art. 30–32 | Contrato de aprendizaje SENA |

---

## 🏢 Áreas y pruebas psicotécnicas

Cada área tiene una prueba personalizada de 10 preguntas (7 técnicas + 3 conductuales):

| Área | Tipo de preguntas técnicas |
|------|---------------------------|
| Comercial / Ventas | Razonamiento numérico, técnicas de venta, facturación |
| Bodega y Logística | Cálculo de cargas, inventario, PEPS, picking |
| Contabilidad y Finanzas | Ecuación contable, IVA, retenciones, DIAN |
| Recursos Humanos | CST, SGSST, clima organizacional, selección |
| Sistemas e IT | Lógica, bases de datos, redes, ciberseguridad |

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
- Tamaño del archivo: ~68 KB

---

## 📁 Estructura del repositorio

```
selectapro/
│
├── SelectaPro_v1.html      # Aplicación completa (único archivo)
└── README.md               # Este documento
```

---

## 📌 Versiones

| Versión | Fecha | Cambios |
|---------|-------|---------|
| v1.0 | Abril 2026 | Lanzamiento inicial — 5 áreas, panel de configuración, normativa colombiana |

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
