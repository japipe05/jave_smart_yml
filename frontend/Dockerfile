# Fase de build
FROM node:20-alpine AS builder

WORKDIR /app

COPY package.json package-lock.json ./
#COPY frontend/package.json frontend/package-lock.json ./

RUN npm install

COPY . .
#COPY frontend . 
RUN npm run build

# Fase de producción
FROM node:20-alpine AS runner

WORKDIR /app

COPY --from=builder /app/package.json ./
COPY --from=builder /app/.next ./.next
COPY --from=builder /app/public ./public
COPY --from=builder /app/node_modules ./node_modules

EXPOSE 3000

CMD ["npm", "run", "start"]
