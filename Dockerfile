# Usa una imagen base de Nginx
FROM nginx:alpine

# Copia los archivos de tu página web al directorio de Nginx
COPY . /usr/share/nginx/html

# (Opcional) Copia un archivo de configuración personalizado si lo tienes
# COPY nginx.conf /etc/nginx/conf.d/default.conf

# Expone el puerto 80
EXPOSE 80
