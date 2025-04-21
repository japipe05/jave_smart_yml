# app/services/github_service.py

import os
import subprocess
import requests
from dotenv import load_dotenv
from pathlib import Path
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

load_dotenv()

def obtener_usuario_github(token):
    headers = {
        "Authorization": f"token {token}"
    }

    response = requests.get("https://api.github.com/user", headers=headers)
 
    if response.status_code == 200:
        return response.json()["login"]
    else:
        raise Exception("No se pudo obtener el nombre de usuario de GitHub.")

def crear_repositorio_github(nombre_repo, descripcion, token):
    logger.info(f"<1.2>. crea repo")

    usuario = obtener_usuario_github(token)
    url_repo = f"https://api.github.com/repos/{usuario}/{nombre_repo}"
    headers = {
        "Authorization": f"token {token}"
    }
    logger.info(f"<1.3>. crea repo")
    # Verificar si ya existe
    response = requests.get(url_repo, headers=headers)
    if response.status_code == 200:
        logger.info(f"Repositorio '{nombre_repo}' ya existe en la cuenta de {usuario}.")
        return response.json()["clone_url"]
    elif response.status_code != 404:
        raise Exception(f"Error al verificar repositorio: {response.status_code}, {response.json()}")
    logger.info(f"<1.3>. crea repo")
    # Crear si no existe
    url_create = "https://api.github.com/user/repos"
    data = {
        "name": nombre_repo,
        "description": descripcion,
        "private": False
    }
    logger.info(f"<1.4>. crea repo")
    response = requests.post(url_create, json=data, headers=headers)

    if response.status_code == 201:
        logger.info(f"<1.5>. crea repo")
        return response.json()["clone_url"]
    else:
        logger.info(f"<1.5>. crea repo")
        raise Exception(f"Error al crear el repositorio: {response.status_code}, {response.json()}")


def ejecutar_comando(comando, cwd):
    subprocess.run(comando, check=True, cwd=cwd)


def subir_proyecto_a_github(github_token_match: str, folder_path: Path, nombre_repo: str, descripcion: str = "Subido automáticamente"):
    token = github_token_match
    if not token:
        raise Exception("Token de GitHub no encontrado.")
    
    logger.info(f"<1>. crea repo")
    # Aquí obtenemos la URL del repo desde la API (usualmente sin token)
    remote_url_clean = crear_repositorio_github(nombre_repo, descripcion, token)
    
    # Inyectamos el token en la URL HTTPS
    # Ejemplo: https://<token>@github.com/usuario/repositorio.git
    remote_url_with_token = remote_url_clean.replace("https://", f"https://{token}@")

    logger.info(f"<1>. crea repo crear_repositorio_github")

    ejecutar_comando(["git", "init"], cwd=folder_path)
    ejecutar_comando(["git", "branch", "-M", "main"], cwd=folder_path)
    ejecutar_comando(["git", "add", "."], cwd=folder_path)
    
    logger.info(f"<2>. valida")
    result = subprocess.run(["git", "status", "--porcelain"], capture_output=True, text=True, cwd=folder_path)
    if result.stdout.strip() != "":
        ejecutar_comando(["git", "commit", "-m", "Subida inicial"], cwd=folder_path)

    logger.info(f"<3>. valida origin")
    remotes = subprocess.run(["git", "remote"], capture_output=True, text=True, cwd=folder_path).stdout
    if "origin" in remotes:
        ejecutar_comando(["git", "remote", "set-url", "origin", remote_url_with_token], cwd=folder_path)
    else:
        ejecutar_comando(["git", "remote", "add", "origin", remote_url_with_token], cwd=folder_path)

    logger.info(f"<4>. valida contenido")
    # Verificamos si ya hay contenido remoto
    try:
        subprocess.run(["git", "fetch"], cwd=folder_path, check=True, capture_output=True)
        result = subprocess.run(["git", "ls-remote", "--heads", "origin", "main"],
                                cwd=folder_path, capture_output=True, text=True)
      
        if result.stdout.strip():
            logger.info("⚠️  El repositorio remoto ya tiene una rama 'main'. Se recomienda revisar para evitar conflictos.")
    except subprocess.CalledProcessError as e:
        logger.error(f"Error al verificar el estado remoto: {e}")

    logger.info(f"<5>. push")
    ejecutar_comando(["git", "push", "-u", "--force", "origin", "main"], cwd=folder_path)
    logger.info(f"<6>. fin push")

    return remote_url_clean  # devolvemos la URL sin token por seguridad

