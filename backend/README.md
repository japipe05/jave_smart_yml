pip install fastapi
pip install python-multipart
pip install uvicorn
pip install python-dotenv
pip install openai
pip install cryptography
pip install cassandra-driver


levantar el servidor python
uvicorn main:app --reload




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