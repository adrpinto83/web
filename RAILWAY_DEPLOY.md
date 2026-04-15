# Guía de Despliegue en Railway

Esta guía te ayudará a desplegar tu proyecto de Delta Amacuro en Railway para que esté accesible públicamente a través de un código QR.

## Requisitos Previos

1. Cuenta en [GitHub](https://github.com) (gratuita)
2. Cuenta en [Railway](https://railway.app) (tiene plan gratuito)
3. Git instalado en tu computadora

## Paso 1: Crear Repositorio en GitHub

1. Ve a [github.com](https://github.com) e inicia sesión
2. Haz clic en el botón verde "New" o "New repository"
3. Configura tu repositorio:
   - **Nombre:** `delta-amacuro-web` (o el nombre que prefieras)
   - **Descripción:** "Proyecto educativo sobre cultura Warao y Delta Amacuro"
   - **Visibilidad:** Public (para que Railway pueda acceder)
   - **NO** marques "Add a README file" (ya tenemos uno)
4. Haz clic en "Create repository"

## Paso 2: Subir el Proyecto a GitHub

Abre una terminal en la carpeta del proyecto y ejecuta:

```bash
# Inicializar repositorio Git (si aún no está inicializado)
git init

# Agregar todos los archivos
git add .

# Crear el primer commit
git commit -m "Proyecto inicial: Landing page Delta Amacuro"

# Conectar con GitHub (reemplaza USUARIO y REPO con tus datos)
git remote add origin https://github.com/USUARIO/REPO.git

# Subir el código
git branch -M main
git push -u origin main
```

## Paso 3: Configurar Railway

1. Ve a [railway.app](https://railway.app)
2. Haz clic en "Start a New Project"
3. Selecciona "Deploy from GitHub repo"
4. Autoriza a Railway para acceder a tu GitHub (si es la primera vez)
5. Selecciona el repositorio `delta-amacuro-web`

## Paso 4: Configuración del Despliegue

Railway detectará automáticamente el `Dockerfile` y comenzará el despliegue:

1. Espera a que termine el despliegue (verás un indicador de progreso)
2. Una vez completado, verás un mensaje de éxito
3. Haz clic en "Settings" en tu proyecto
4. Ve a la sección "Networking"
5. Haz clic en "Generate Domain"
6. Railway generará una URL pública como: `https://tu-proyecto.up.railway.app`

## Paso 5: Verificar el Despliegue

1. Haz clic en la URL generada
2. Deberías ver tu landing page funcionando correctamente
3. Prueba la responsividad en diferentes dispositivos
4. Verifica que todas las imágenes cargan correctamente

## Paso 6: Generar el Código QR

1. Copia la URL completa de tu sitio (ejemplo: `https://delta-amacuro.up.railway.app`)
2. Ve a uno de estos sitios para generar el QR:
   - [QR Code Generator](https://www.qr-code-generator.com/)
   - [QRCode Monkey](https://www.qrcode-monkey.com/)
   - [QR Code Generator (español)](https://es.qr-code-generator.com/)

3. Pasos en el generador:
   - Selecciona "URL" como tipo
   - Pega tu URL de Railway
   - Personaliza el diseño (opcional):
     - Agrega colores que combinen con tu página
     - Puedes agregar un logo en el centro
   - Descarga el QR en alta calidad (PNG o SVG)

4. Guarda el archivo como `qr-code.png` en la carpeta `images/` de tu proyecto

## Paso 7: Actualizar la Página con el QR Real

1. Abre `index.html` en tu editor
2. Busca la sección del código QR:
   ```html
   <img src="images/qr-placeholder.svg" alt="Código QR del proyecto" class="qr-code">
   ```
3. Cámbialo por:
   ```html
   <img src="images/qr-code.png" alt="Código QR del proyecto" class="qr-code">
   ```
4. Guarda el archivo

## Paso 8: Actualizar el Despliegue

```bash
# Agregar los cambios
git add .

# Crear un commit
git commit -m "Añadir código QR real del proyecto"

# Subir los cambios
git push
```

Railway detectará los cambios automáticamente y redesplegar tu sitio en unos minutos.

## Solución de Problemas

### El sitio no carga

- Verifica los logs en Railway (pestaña "Deployments" → clic en el último despliegue → "View Logs")
- Asegúrate de que el Dockerfile esté en la raíz del proyecto

### Las imágenes no cargan

- Verifica que las URLs de las imágenes externas sean correctas
- Si descargas imágenes localmente, asegúrate de que estén en la carpeta `images/`

### Error de despliegue

- Revisa que todos los archivos necesarios estén en el repositorio
- Verifica que el Dockerfile no tenga errores de sintaxis

### El código QR no funciona

- Verifica que la URL del QR sea exactamente la misma que Railway generó
- Asegúrate de que la URL comience con `https://`
- Prueba el QR con diferentes aplicaciones de lectura

## Mantenimiento

### Actualizar el Contenido

Cada vez que hagas cambios en el proyecto:

```bash
git add .
git commit -m "Descripción de los cambios"
git push
```

Railway redesplegar automáticamente.

### Ver Estadísticas

Railway te permite ver:
- Número de visitas
- Uso de recursos
- Logs de acceso

Ve a la pestaña "Metrics" en tu proyecto de Railway.

## Dominio Personalizado (Opcional)

Si tienes un dominio propio (ejemplo: `deltaAmacuro.com`):

1. Ve a Settings → Networking en Railway
2. Haz clic en "Custom Domain"
3. Ingresa tu dominio
4. Configura los registros DNS según las instrucciones de Railway

## Plan Gratuito de Railway

Railway ofrece:
- **$5 USD de crédito mensual gratis**
- **500 horas de ejecución al mes**
- Suficiente para proyectos escolares de bajo tráfico

Para proyectos educativos, el plan gratuito suele ser más que suficiente.

## Recursos Adicionales

- [Documentación de Railway](https://docs.railway.app/)
- [Soporte de Railway](https://railway.app/help)
- [Guías de Docker](https://docs.docker.com/get-started/)

---

¡Listo! Ahora tu proyecto está en línea y accesible mediante código QR. Perfecto para presentaciones y exposiciones escolares.
