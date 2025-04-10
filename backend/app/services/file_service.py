import openai
import os
from pathlib import Path
from dotenv import load_dotenv
import shutil
# Cargar las variables de entorno 
load_dotenv()

# Cliente de OpenAI
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def save_uploaded_file(file) -> str:
    """Guarda el archivo en la carpeta uploads/ y devuelve la ruta"""
    upload_dir = Path("uploads")
    upload_dir.mkdir(parents=True, exist_ok=True)
    file_path = upload_dir / file.filename
    with file_path.open("wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return str(file_path)

def upload_file_to_openai(file_path: str) -> str:
    """Sube un archivo .zip a OpenAI y devuelve el ID del archivo"""
    with open(file_path, "rb") as file:
        response = client.files.create(
            file=file,
            purpose="assistants"
        )
    return response.id  # ✅ Acceder al atributo en lugar de usar corchetes


def analyze_zip_with_gpt(file_id: str,message: str,model_name: str) -> dict:
    """Envía un prompt a GPT-4 para analizar el .zip y generar Dockerfile + docker-compose.yml"""
    prompt = (
        f"Introducción: {message}\n"
        "Descomprime el archivo .zip y analiza su contenido y conbase a ese contenido realiza lo siguiente:\n"
        "1. Creame el archivo Dockerfile con las siguientes caacteristicas:\n"
        "a. Usa una imagen ligera de Node.js basada en Alpine Linux yna version mayor o igual a la 20 y la nombra builder\n"
        "b. Define el directorio de trabajo dentro del contenedor\n"
        "c. Copia solo package.json y package-lock.json primero\n"
        "d. Instala todas las dependencias de la aplicación\n"
        "e. Copia el resto del código fuente al contenedor\n"
        "f. Ejecuta next build para compilar el código de Next.js y generar la carpeta\n"
        "g. Se usa otra imagen limpia de Node.js para reducir el tamaño del contenedor final\n"
        "h. Copia solo los archivos necesarios desde la fase builder. package.json, .next, public, node_modules\n"
        "i. Abre el puerto 3000 para que la aplicación Next.js pueda recibir tráfico\n"
        "j. Ejecuta la aplicación en modo producción\n"
        "2. Crea el archivo docker-compose.yml con las siguientes características:\n"
        "a. Especifica la versión de docker-compose que se está utilizando. La versión mayor o igual a 3.8 es compatible con Docker 19.03.0\n"
        "b. Establece el nombre del container_name como frontend_app\n"
        "c. Mapea puertos entre el contenedor y el host\n"
    )


    response = client.chat.completions.create(
        model=model_name,
        messages=[
            {"role": "system", "content": "Eres un experto en Docker."},
            {"role": "user", "content": prompt, "file_ids": [file_id]}
        ],
        functions=[
            {
                "name": "generate_dockerfile",
                "description": "Genera un Dockerfile optimizado para una aplicación Next.js.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "dockerfile_content": {"type": "string", "description": "Contenido del Dockerfile"}
                    },
                    "required": ["dockerfile_content"]
                }
            },
            {
                "name": "generate_docker_compose",
                "description": "Genera un archivo docker-compose.yml optimizado para una aplicación Next.js.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "docker_compose_content": {"type": "string", "description": "Contenido del archivo docker-compose.yml"}
                    },
                    "required": ["docker_compose_content"]
                }
            }
        ],
        function_call="auto"
    )

    return response.choices[0].message.content


def create_dockerfile_and_yml(upload_dir: Path):
    dockerfile_path = upload_dir / "Dockerfile"
    yml_path = upload_dir / "docker-compose.yml"

    # Aquí deberías generar el contenido de los archivos
    dockerfile_content = "Contenido del Dockerfile"
    yml_content = "Contenido del docker-compose.yml"

    dockerfile_path.write_text(dockerfile_content.strip())
    yml_path.write_text(yml_content.strip())

    return {
        "dockerfile": str(dockerfile_path),
        "yml": str(yml_path)
    }