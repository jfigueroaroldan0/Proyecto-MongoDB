# 🛡️ MongoDB & Python: Gestión de Vulnerabilidades (CISA)

Este proyecto demuestra la integración de una base de datos NoSQL (**MongoDB**) con un lenguaje de programación (**Python**) para gestionar y analizar el catálogo de vulnerabilidades explotadas de la CISA.

---

## 📋 Características del Proyecto

El sistema permite la gestión completa del ciclo de vida de datos de ciberseguridad, cumpliendo con los siguientes requisitos técnicos:

- **Modelado NoSQL:** Uso de todos los tipos de datos BSON (String, Double, Int32, Boolean, Date, Array, Object y Null).
- **Operaciones CRUD:** Implementación de métodos de inserción, eliminación y actualización avanzada (operadores `$set`, `$inc`, `$currentDate`).
- **Consultas Complejas:** Uso de proyecciones, operadores de comparación/lógicos, ordenación (`sort`) y limitación de resultados (`limit`).
- **Agregación:** Pipeline para estadísticas avanzadas (promedios y conteos por fabricante).
- **Interfaz CLI:** Programa en Python modularizado y validado para la gestión interactiva.

---

## 🛠️ Requisitos e Instalación

### Requisitos Previos

- **MongoDB** (Local o Atlas)
- **Python**
- **Biblioteca PyMongo**

```bash
pip install pymongo
```

---

## 📥 Importación de Datos

Para cargar el dataset inicial enriquecido, utiliza la utilidad `mongoimport` desde la terminal:

```bash
mongoimport --db seguridad --collection vulnerabilidades --file vulnerabilidades_modificado.json --jsonArray
```

---

## 📂 Estructura de la Base de Datos

Cada documento en la colección `vulnerabilidades` sigue este esquema enriquecido:

| Campo | Tipo BSON | Descripción |
|---|---|---|
| `cveID` | String | Identificador único de la vulnerabilidad |
| `cvssV3BaseScore` | Double | Puntuación de severidad decimal |
| `exploitsCount` | Int32 | Número entero de exploits detectados |
| `isPatched` | Boolean | Estado de resolución |
| `discoveryDate` | Date | Fecha de registro (`ISODate`) |
| `affectedVersions` | Array | Lista de versiones de software |
| `mitigationDetails` | Object | Documento embebido con detalles técnicos |
| `patchUrl` | Null / String | URL del parche o valor nulo |

---

## 🚀 Uso del Programa Python

Ejecuta el script principal para acceder al menú interactivo:

```bash
python main.py
```

### Opciones Disponibles

- **Inserción:** Añade nuevas vulnerabilidades con IDs dinámicos.
- **Eliminación:** Borrado selectivo por `cveID`.
- **Modificación:** Actualización de estado y contadores mediante operadores.
- **Consultas:** Cuatro modos de visualización:
  - Simple
  - Arrays
  - Embebidos
  - Agregación

---

## 📁 Estructura Recomendada del Proyecto

```text
📦 Proyecto-Mongodb
├── main.py    
├── funciones.py
├── original_vulnerabilidades.json
├── vulnerabilidades_modificado.json
├── README.md
└── requirements.txt
```

---

## 📚 Tecnologías Utilizadas

- Python 3
- MongoDB
- PyMongo
- MongoDB Shell
