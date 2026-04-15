# Guía de Imágenes del Proyecto

## Imágenes Generadas

Este proyecto incluye **11 imágenes PNG** optimizadas creadas con Python PIL (Pillow), totalmente compatibles con todos los navegadores modernos y antiguos.

### Características de las Imágenes

✅ **Formato PNG** - Compatible con JPG/PNG (navegadores antiguos)
✅ **Tamaño optimizado** - Entre 4KB y 20KB cada una
✅ **Sin dependencias externas** - No requieren conexión a internet
✅ **Carga rápida** - Total: ~150KB (vs varios MB de imágenes externas)
✅ **Generadas con código** - Reproducibles y personalizables

## Inventario de Imágenes

### Símbolos Regionales
- `bandera-delta.png` (4 KB) - Bandera tricolor del estado
- `escudo-delta.png` (8 KB) - Escudo con palma, río y estrellas

### Geografía y Cultura
- `delta-orinoco.png` (16 KB) - Paisaje del delta con vegetación
- `viviendas-warao.png` (16 KB) - Palafitos sobre el agua

### Gastronomía Tradicional
- `sancocho.png` (12 KB) - Plato de sancocho con vapor
- `lau-lau.png` (8 KB) - Pescado frito dorado
- `gusanos-moriche.png` (16 KB) - Gusanos sobre hoja de plátano

### Fauna del Delta
- `jaguar.png` (16 KB) - Jaguar con rosetas en la selva
- `guacamayas.png` (16 KB) - Dos guacamayas multicolores
- `peces-orinoco.png` (20 KB) - Cardumen bajo el agua
- `manati.png` (20 KB) - Manatí nadando

### Branding
- `logo-warao.svg` (2 KB) - Logo del proyecto (vectorial)
- `qr-placeholder.svg` (3 KB) - Placeholder para código QR

## Cómo Funcionan

### Compatibilidad

Las imágenes PNG son compatibles con:
- ✅ Todos los navegadores modernos (Chrome, Firefox, Safari, Edge)
- ✅ Navegadores antiguos (IE 6+, versiones antiguas de Chrome/Firefox)
- ✅ Navegadores móviles (iOS Safari, Android Chrome)
- ✅ Lectores de QR (carga rápida en dispositivos móviles)

### Comparación con SVG

| Característica | PNG (Actual) | SVG (Anterior) |
|---------------|--------------|----------------|
| Compatibilidad | ✅ Universal | ⚠️ Limitada en navegadores antiguos |
| Tamaño total | ~150 KB | ~17 MB |
| Carga | Instantánea | Lenta |
| Escalabilidad | Buena (optimizadas para web) | Perfecta |
| Edición | Requiere regenerar | Editable como texto |

## Regenerar Imágenes

Si necesitas modificar las imágenes:

### 1. Editar el Script

```bash
# Editar colores, tamaños o contenido
nano generate_images.py
```

### 2. Regenerar

```bash
# Generar imágenes principales
python3 generate_images.py

# Generar símbolos regionales
python3 create_symbols.py
```

### 3. Personalización

En `generate_images.py` puedes modificar:

- **Colores**: Cambia los valores RGB en cada función
  ```python
  draw.rectangle([0, 0, 800, 600], fill=(R, G, B))
  ```

- **Tamaños**: Ajusta width y height
  ```python
  img = Image.new('RGB', (ancho, alto), color_fondo)
  ```

- **Texto**: Modifica los mensajes
  ```python
  add_text(img, "Tu texto aquí", 'bottom', 50, (255, 255, 255))
  ```

## Optimización

### Tamaño de Archivo

Las imágenes están optimizadas con:
```python
img.save(filepath, 'PNG', optimize=True)
```

### Reducir Aún Más

Si necesitas imágenes más pequeñas:

```bash
# Instalar pngquant (opcional)
sudo apt install pngquant

# Comprimir PNGs
pngquant --quality=65-80 images/*.png --ext .png --force
```

## Conversión a JPG

Si prefieres JPG para algunas imágenes:

```python
from PIL import Image

# Convertir PNG a JPG
img = Image.open('images/delta-orinoco.png')
rgb_img = img.convert('RGB')
rgb_img.save('images/delta-orinoco.jpg', 'JPEG', quality=85, optimize=True)
```

## Versiones SVG

Aunque el proyecto usa PNG por defecto, se mantienen versiones SVG de algunos elementos:

- `logo-warao.svg` - Logo (se mantiene SVG por ser pequeño y escalable)
- `qr-placeholder.svg` - Placeholder QR (se mantiene SVG)
- `bandera-delta.svg` - Versión vectorial de la bandera
- `escudo-delta.svg` - Versión vectorial del escudo

Puedes usar SVG si tu audiencia usa solo navegadores modernos:

```html
<!-- Cambiar de PNG a SVG -->
<img src="images/delta-orinoco.svg" alt="Delta del Orinoco">
```

## Créditos

- **Generación**: Python PIL (Pillow)
- **Diseño**: Creado específicamente para este proyecto
- **Licencia**: Uso libre para fines educativos

## Soporte

Si tienes problemas con las imágenes:

1. Verifica que los archivos PNG existan en `images/`
2. Confirma que el navegador soporta PNG (todos lo hacen)
3. Revisa la consola del navegador por errores 404
4. Regenera las imágenes con los scripts Python

---

**Última actualización**: Abril 2026
**Proyecto**: Delta Amacuro - U.E. Industrial Juan Crisóstomo Falcón
