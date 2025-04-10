from fastapi import APIRouter, Form, UploadFile, File, HTTPException
from fastapi.responses import FileResponse, JSONResponse
from pathlib import Path
from zipfile import ZipFile
import shutil
import os
import re
import logging

from app.services.file_service import save_uploaded_file, upload_file_to_openai, analyze_zip_with_gpt
from app.services.github_service import subir_proyecto_a_github


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

router = APIRouter(prefix="/files", tags=["Files"])

@router.post("/upload")
async def upload_and_process_file(
    message: str = Form(None),
    file: UploadFile = File(...),
    model_name: str = Form("gpt-4-turbo")):
    try:
        # Guardar el archivo temporalmente
        file_path = Path(save_uploaded_file(file))
        logger.info(f"Archivo guardado en: {file_path}")

        # Definir el directorio de extracción
        extracted_dir = file_path.with_suffix('')  # /uploads/holamundonextjs15

        # Si el directorio de extracción ya existe, eliminarlo
        if extracted_dir.exists():
            shutil.rmtree(extracted_dir)
            logger.info(f"Directorio existente eliminado: {extracted_dir}")

        # Descomprimir el archivo
        with ZipFile(file_path, 'r') as zip_ref:
            zip_ref.extractall(extracted_dir)
        logger.info(f"Archivo descomprimido en: {extracted_dir}")

        # Renombrar carpeta agregando 'prod'
        prod_dir = Path(f"{extracted_dir}prod")  # /uploads/holamundonextjs15prod
        if prod_dir.exists():
            shutil.rmtree(prod_dir)
            logger.info(f"Directorio 'prod' existente eliminado: {prod_dir}")
        extracted_dir.rename(prod_dir)
        logger.info(f"Directorio renombrado a: {prod_dir}")

        # Subir .zip a OpenAI
        file_id = upload_file_to_openai(file_path)
        logger.info(f"Archivo subido a OpenAI con ID: {file_id}")

        # Obtener archivos generados por OpenAI
        generated_content = analyze_zip_with_gpt(file_id, message, model_name)
        logger.info(f"Contenido generado por OpenAI: {generated_content}")

        # Extraer Dockerfile
        matches = re.findall(r'```Dockerfile\n(.*?)```', generated_content, re.DOTALL) or \
                  re.findall(r'```dockerfile\n(.*?)```', generated_content, re.DOTALL)
        dockerfile_content = matches[0].strip() if matches else ""

        # Extraer docker-compose.yml
        matches = re.findall(r'```yaml\n(.*?)```', generated_content, re.DOTALL)
        yml_content = matches[0].strip() if matches else ""

        # Guardar archivos en la carpeta renombrada
        dockerfile_path = prod_dir / "Dockerfile"
        yml_path = prod_dir / "docker-compose.yml"
        dockerfile_path.write_text(dockerfile_content)
        yml_path.write_text(yml_content)
        logger.info(f"Dockerfile y docker-compose.yml guardados en: {prod_dir}")

        # Comprimir la carpeta final
        output_zip_path = prod_dir.with_suffix('.zip')  # /uploads/holamundonextjs15prod.zip
        if output_zip_path.exists():
            output_zip_path.unlink()
            logger.info(f"Archivo ZIP existente eliminado: {output_zip_path}")
        shutil.make_archive(str(prod_dir), 'zip', root_dir=prod_dir)
        logger.info(f"Carpeta comprimida en: {output_zip_path}")

        # Subir la carpeta final a GitHub
        nombre_repo = prod_dir.name  # por ejemplo: holamundonextjs15prod
        try:
            github_url = subir_proyecto_a_github(prod_dir, nombre_repo)
            logger.info(f"Repositorio subido con éxito: {github_url}")
        except Exception as github_error:
            logger.error(f"No se pudo subir el repositorio a GitHub: {github_error}")
            github_url = None


        return JSONResponse(content={
                "message": "Archivo subido, analizado y procesado con éxito. \n"
                           "1. Descarga el archivo .zip. \n"
                           "2. Descomprime el archivo .zip. \n"
                           "3. Abre la carpeta y abre el terminal con CMD en Windows. "
                           "4. Ejecuta el siguiente comando: \n docker-compose up --build -d",
                "file_path": str(file_path),
                "generated_files": {
                    "dockerfile": str(dockerfile_path),
                    "yml": str(yml_path),
                    "zip_url": f"/files/download/{output_zip_path.name}"
                }
            })

    except Exception as e:
        logger.error(f"Error al procesar el archivo: {e}")
        raise HTTPException(status_code=500, detail="Error interno del servidor")

@router.get("/download/{filename}")
async def download_file(filename: str):
    zip_path = Path("uploads") / filename
    if not zip_path.exists():
        raise HTTPException(status_code=404, detail="Archivo no encontrado")
    return FileResponse(path=zip_path, filename=filename, media_type='application/zip')
