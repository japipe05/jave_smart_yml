# 🚀 Jave Smart YML - Plataforma Fullstack Inteligente

Bienvenido a **Jave Smart YML**, una solución fullstack de última generación que combina lo mejor del desarrollo moderno con herramientas poderosas y arquitectura escalable. Esta plataforma es ideal para lanzar MVPs, startups o productos robustos de clase empresarial.

---

## 🧠 Arquitectura General

📦 Proyecto dividido en dos módulos:

- 🖥️ **Frontend:** Next.js 15 + Tailwind + TypeScript  
- 🧪 **Backend:** FastAPI + Python + Arquitectura modular

Todo integrado con soporte para Docker, despliegue continuo y buenas prácticas desde el inicio.

---

## 🌐 Frontend - Next.js 15

📁 Ruta: `./Frontend/`

✨ **Stack & Features:**

- 🔥 Next.js 15 (App Router)
- 💨 Tailwind CSS
- 🧠 TypeScript
- 🌐 PWA Ready
- ⚙️ ESLint + Prettier + Docker
- ⚡ Arquitectura limpia y escalable

### 🚀 Ejecutar Frontend

cd Frontend
npm install
npm run dev

---

## 🔧 Backend - Python FastAPI

📁 Ruta: `./Backend/`

✨ **Stack & Features:**

- ⚡ FastAPI
- 🐍 Python 3.11+
- 🔐 JWT Authentication
- 🗂️ Modular: routers, models, services, config
- 📄 Swagger UI y OpenAPI
- 🐳 Docker Ready
- 🛢️ Soporte Cassandra / MongoDB / SQL

### 🚀 Ejecutar Backend

cd Backend
pip install -r requirements.txt
uvicorn main:app --reload

---

## 🐳 Docker Ready

Lanza toda la plataforma con Docker Compose:

docker-compose up --build

Configuración optimizada para ambientes de desarrollo y producción.

---

## 🧪 Buenas Prácticas

- ✅ Código limpio y escalable
- ✅ Separación clara de responsabilidades
- ✅ Entorno `.env` seguro y configurable
- ✅ Pruebas listas para integración

---

## ✨ ¿Por qué usar Jave Smart YML?

- ✅ **Desarrollo veloz** con herramientas modernas
- ✅ **Escalable** para startups o sistemas empresariales
- ✅ **Dockerizado** y listo para la nube
- ✅ **Diseño moderno y experiencia fluida**

---

## 🤝 Contribuciones

Este proyecto está abierto a la comunidad. Si quieres aportar mejoras, ¡haz un fork y un PR!

---

## 👨‍💻 Desarrollado por

**Jave Smart Labs**  
💡 Tecnología con propósito. Innovación con resultados.

---

## 📄 Licencia

MIT — ¡Úsalo libremente y comparte el conocimiento!


### <a id='10.1'>Diagramas de Arquitectura </a> 

![arquitectura.png](public/img/arquitectura.png)

# jave_smart_yml
 Contenerización de aplicaciones en nextjs y pipelines de github actions más vercel 

# intalar requeriment
> pip install -r requirements.txt

# borrar
> docker-compose down -v   
# Construir y levantar contenedores
> docker-compose up --build -d

#desarrollo

remover
docker-compose -f docker-compose.dev.yml down -v

subir
docker-compose -f docker-compose.yml -f docker-compose.dev.yml up --build
docker-compose -f docker-compose.yml -f docker-compose.dev.yml up --build -d


posrtgres falta validar
pip install fastapi sqlalchemy psycopg2-binary uvicorn


postgres
select * from prompts

Cassandra
DESCRIBE KEYSPACES;
DESCRIBE TABLES;
select * from appkeyspace.users;