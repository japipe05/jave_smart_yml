import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.database.postgres import SessionLocal
from app.models.prompt_model import Prompt


db = SessionLocal()

descripcion = (
    "Descomprime el archivo .zip y analiza su contenido y con base a ese contenido realiza lo siguiente:\n"
    "1. Creame el archivo Dockerfile, estructura de salida comience obligatorio con ```Dockerfile con las siguientes características:\n"
    "a. Usa una imagen ligera de Node.js basada en Alpine Linux y una versión mayor o igual a la 20 y la nombra builder\n"
    "b. Define el directorio de trabajo dentro del contenedor\n"
    "c. Copia solo package.json y package-lock.json primero\n"
    "d. Instala todas las dependencias de la aplicación\n"
    "e. Copia el resto del código fuente al contenedor\n"
    "f. Ejecuta next build para compilar el código de Next.js y generar la carpeta\n"
    "g. Se usa otra imagen limpia de Node.js para reducir el tamaño del contenedor final\n"
    "h. Copia solo los archivos necesarios desde la fase builder: package.json, .next, public, node_modules\n"
    "i. Abre el puerto 3000 para que la aplicación Next.js pueda recibir tráfico\n"
    "j. Ejecuta la aplicación en modo producción\n"
    "2. Crea el archivo docker-compose.yml, estructura de salida comience obligatorio con ```yaml con las siguientes características:\n"
    "a. Especifica la versión de docker-compose >= 3.8 (compatible con Docker 19.03.0)\n"
    "b. Establece el container_name como frontend_app\n"
    "c. Mapea puertos entre el contenedor y el host\n"
    "3. Crea el archivo vercel.yml, estructura de salida comience obligatorio con ```yamlVercel con las siguientes características:\n"
    "a. Nombre del flujo de trabajo, solo una etiqueta para identificarlo en GitHub Actions\n"
    "b. Acción al hacer push sobre la rama main\n"
    "c. Crea un job llamado deploy\n"
    "d. Se ejecutará en un entorno Linux\n"
    "e. Clona el código del repositorio al runner con <= v3\n"
    "f. Configura Node.js en versión 20 para usar herramientas JS como npm\n"
    "g. Instala CLI de Vercel necesaria para el despliegue\n"
    "h. Realiza el despliegue del proyecto\n"
    "i. --prod despliegue en producción\n"
    "j. --yes responde automáticamente preguntas interactivas\n"
    "k. --Token=llavesecretavercel\n"
)

nuevo_prompt = Prompt(opcion="generacion_archivos_docker", descripcion=descripcion)
db.add(nuevo_prompt)
db.commit()
db.refresh(nuevo_prompt)
db.close()
