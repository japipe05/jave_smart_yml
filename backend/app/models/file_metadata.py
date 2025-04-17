from pydantic import BaseModel

class FileMetadata(BaseModel):
    filename: str
    message: str
    dockerfile_path: str
    yml_path: str
    vercel_path: str
    zip_path: str
    github_url: str | None = None
