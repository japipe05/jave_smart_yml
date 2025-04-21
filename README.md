
# 🚀 Smart YML - GENERACIÓN AUTOMÁTICA DE PLANTILLAS PARA EL DESPLIEGUE DE APLICACIONES MEDIANTE INTELIGENCIA ARTIFICIAL  

![logo.png](public/img/logo.png)

Class: Trabajo de grado <br>
Code: 0000 <br>
Members:

    John Paul Jasin Martinez - @jpjassinm
    Andrés Felipe Rodríguez Roa - @japipe05


# 🚀 Smart YML 

Bienvenido a **Smart YML**, una solución fullstack de última generación que combina lo mejor del desarrollo moderno con herramientas poderosas y una arquitectura escalable. Esta plataforma es ideal para lanzar MVPs, startups o productos robustos de clase empresarial.

---

## 🧠 Arquitectura General

📦 El proyecto está dividido en dos módulos principales:

- 🖥️ **Frontend:** Next.js 15 + Tailwind + TypeScript  
- 🧪 **Backend:** FastAPI + Python + Arquitectura Modular

Totalmente integrado con soporte para Docker, despliegue continuo y buenas prácticas desde el inicio.

---

## 🌐 Frontend - Next.js 15

📁 Ruta: `./Frontend/`

✨ **Tecnologías y Características:**

- 🔥 Next.js 15 (App Router)
- 💨 Tailwind CSS
- 🧠 TypeScript
- 🌐 PWA listo para usar
- ⚙️ ESLint + Prettier + Docker
- ⚡ Arquitectura limpia y escalable

### 🚀 Ejecutar el Frontend

```bash
cd Frontend
npm install
npm run dev
```

---

## 🔧 Backend - Python FastAPI

📁 Ruta: `./Backend/`

✨ **Tecnologías y Características:**

- ⚡ FastAPI
- 🐍 Python 3.11+
- 🔐 Autenticación con JWT
- 🗂️ Modular: rutas, modelos, servicios, configuración
- 📄 Swagger UI y OpenAPI
- 🐳 Preparado para Docker
- 🛢️ Soporte para Cassandra / MongoDB / SQL

### 🚀 Ejecutar el Backend

```bash
cd Backend
pip install -r requirements.txt
uvicorn main:app --reload
```

---

## 🐳 Preparado para Docker

Lanza toda la plataforma utilizando Docker Compose:

```bash
docker-compose up --build
```

Configuración optimizada para ambientes de desarrollo y producción.

---

## 🧪 Buenas Prácticas

- ✅ Código limpio y escalable
- ✅ Separación clara de responsabilidades
- ✅ Entorno `.env` seguro y configurable
- ✅ Listo para pruebas de integración

---

## ✨ ¿Por Qué Usar Jave Smart YML?

- ✅ **Desarrollo rápido** con herramientas modernas
- ✅ **Escalable** para startups y sistemas empresariales
- ✅ **Dockerizado** y listo para la nube
- ✅ **Diseño moderno** y experiencia de usuario fluida

---

## 🤝 Contribuciones

Este proyecto está abierto a la comunidad. Si quieres contribuir con mejoras, ¡haz un fork y envía un PR!

---

## 👨‍💻 Desarrollado por

**Jave Smart Labs**  
💡 Tecnología con propósito. Innovación con resultados.

---

## 📄 Licencia

MIT — ¡Úsalo libremente y comparte el conocimiento!

---

## 🏗️ Estructura del Proyecto

**Frontend/**
```
├── app/                    # App Router (Next.js 13+)
│   ├── layout.tsx          # Diseño principal
│   ├── page.tsx            # Página raíz
│   └── ...(rutas)/
├── components/             # Componentes reutilizables
├── styles/                 # Estilos globales (Tailwind config, etc)
├── public/                 # Archivos públicos (imágenes, íconos)
├── utils/                  # Utilidades y helpers
├── hooks/                  # Custom Hooks de React
├── services/               # Lógica de acceso a APIs externas
├── middleware.ts           # Middlewares de Next.js
├── tailwind.config.ts      # Configuración de Tailwind
├── next.config.js          # Configuración de Next.js
├── tsconfig.json           # Configuración de TypeScript
├── .eslintrc.json          # Reglas de linting
├── .prettierrc             # Formato de código
├── Dockerfile              # Imagen Docker del Frontend
├── package.json            # Dependencias y scripts
└── README.md               # Documentación del frontend
```

**Backend/**
```
├── app/
│   ├── main.py             # Punto de entrada de la app
│   ├── api/                # Rutas organizadas por módulos
│   │   ├── v1/
│   │   │   ├── endpoints/  # Archivos de rutas
│   │   │   └── __init__.py
│   ├── core/               # Configuración general (ajustes, logs, etc)
│   ├── models/             # Modelos de base de datos (Pydantic y/o ORM)
│   ├── schemas/            # Esquemas Pydantic
│   ├── services/           # Lógica de negocio
│   ├── db/                 # Configuración de base de datos
│   ├── utils/              # Funciones auxiliares
│   └── middleware/         # Middlewares personalizados
├── tests/                  # Pruebas unitarias y de integración
├── requirements.txt        # Dependencias del proyecto
├── .env                    # Variables de entorno
├── Dockerfile              # Imagen Docker del backend
└── README.md               # Documentación del backend
```

---


### <a id='1'>Arquitectura AS-IS</a> 

![arquitectura_AS-IS.png](public/img/arquitectura_AS-IS.png)


### <a id='2'>Arquitectura To-Be</a> 

![Arquitectura_To-Be.png](public/img/Arquitectura_To-Be.png)

### <a id='3'>Login</a> 

![login.png](public/img/login.png)

### <a id='4'>Registro</a> 

![registro.png](public/img/registro.png)

### <a id='5'>Chat Web</a> 

![chat-web.png](public/img/chat-web.png)


## 🗃️ Consultas a la Base de Datos

### 🐘 PostgreSQL

```sql
SELECT * FROM prompts;
```

### 🔹 Cassandra

```sql
DESCRIBE KEYSPACES;
DESCRIBE TABLES;
SELECT * FROM appkeyspace.users;
```

### 🔧 Configuración Local en Docker

```bash
docker-compose up --build -d
```