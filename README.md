# jave_smart_yml
 Contenerización de aplicaciones en nextjs y pipelines de github actions más vercel 

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
