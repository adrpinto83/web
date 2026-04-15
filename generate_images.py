#!/usr/bin/env python3
"""
Script para generar imágenes PNG genéricas para el proyecto Delta Amacuro
"""

from PIL import Image, ImageDraw, ImageFont
import os

def create_gradient(width, height, color1, color2, direction='vertical'):
    """Crea un gradiente entre dos colores"""
    base = Image.new('RGB', (width, height), color1)
    draw = ImageDraw.Draw(base)

    if direction == 'vertical':
        for i in range(height):
            r = int(color1[0] + (color2[0] - color1[0]) * i / height)
            g = int(color1[1] + (color2[1] - color1[1]) * i / height)
            b = int(color1[2] + (color2[2] - color1[2]) * i / height)
            draw.line([(0, i), (width, i)], fill=(r, g, b))
    else:  # horizontal
        for i in range(width):
            r = int(color1[0] + (color2[0] - color1[0]) * i / width)
            g = int(color1[1] + (color2[1] - color1[1]) * i / width)
            b = int(color1[2] + (color2[2] - color1[2]) * i / width)
            draw.line([(i, 0), (i, height)], fill=(r, g, b))

    return base

def add_text(image, text, position='center', font_size=40, color=(255, 255, 255)):
    """Añade texto a una imagen"""
    draw = ImageDraw.Draw(image)

    try:
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", font_size)
    except:
        font = ImageFont.load_default()

    # Obtener el tamaño del texto
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]

    width, height = image.size

    if position == 'center':
        x = (width - text_width) / 2
        y = (height - text_height) / 2
    elif position == 'bottom':
        x = (width - text_width) / 2
        y = height - text_height - 30
    else:
        x, y = position

    # Sombra del texto
    draw.text((x + 2, y + 2), text, font=font, fill=(0, 0, 0, 128))
    # Texto principal
    draw.text((x, y), text, font=font, fill=color)

    return image

def create_delta_orinoco():
    """Delta del Orinoco - paisaje con agua y vegetación"""
    img = create_gradient(1200, 800, (135, 206, 235), (176, 224, 230))  # Cielo azul
    draw = ImageDraw.Draw(img)

    # Agua (parte inferior)
    for i in range(400, 800):
        ratio = (i - 400) / 400
        r = int(46 + (30 - 46) * ratio)
        g = int(139 + (94 - 139) * ratio)
        b = int(87 + (49 - 87) * ratio)
        draw.line([(0, i), (1200, i)], fill=(r, g, b))

    # Vegetación (manchas verdes)
    for i in range(5):
        x = 100 + i * 250
        draw.ellipse([x, 350, x + 150, 450], fill=(34, 139, 34, 180))

    # Sol
    draw.ellipse([1000, 80, 1100, 180], fill=(255, 215, 0))

    add_text(img, "Delta del Orinoco", 'bottom', 50, (255, 255, 255))

    return img

def create_viviendas_warao():
    """Viviendas Warao - palafitos"""
    img = create_gradient(1200, 800, (135, 206, 235), (70, 130, 180))
    draw = ImageDraw.Draw(img)

    # Agua
    for i in range(500, 800):
        draw.line([(0, i), (1200, i)], fill=(70, 130, 180))

    # Palafitos (casas sobre pilotes)
    palafitos = [(200, 350), (500, 330), (850, 360)]

    for x, y in palafitos:
        # Pilotes
        for px in [x, x + 50, x + 100, x + 150]:
            draw.line([(px, y), (px, y + 180)], fill=(101, 67, 33), width=8)

        # Plataforma
        draw.rectangle([x - 10, y - 10, x + 160, y + 10], fill=(139, 69, 19))

        # Casa
        draw.rectangle([x, y - 80, x + 150, y], fill=(210, 105, 30))

        # Techo
        draw.polygon([(x - 20, y - 80), (x + 75, y - 140), (x + 170, y - 80)], fill=(139, 115, 85))

    add_text(img, "Palafitos Warao", 'bottom', 50, (255, 255, 255))

    return img

def create_sancocho():
    """Sancocho de pescado"""
    img = Image.new('RGB', (800, 600), (245, 245, 220))
    draw = ImageDraw.Draw(img)

    # Mesa
    draw.rectangle([0, 450, 800, 600], fill=(139, 69, 19))

    # Plato
    draw.ellipse([150, 150, 650, 400], fill=(255, 255, 255))
    draw.ellipse([170, 165, 630, 385], fill=(255, 140, 66))  # Caldo

    # Vapor
    for x in [300, 400, 500]:
        for y_offset in range(0, 60, 15):
            draw.ellipse([x - 5, 100 - y_offset, x + 5, 110 - y_offset],
                        fill=(200, 200, 200, 100))

    add_text(img, "Sancocho de Pescado", 'bottom', 45, (51, 51, 51))

    return img

def create_lau_lau():
    """Lau-Lau frito"""
    img = Image.new('RGB', (800, 600), (255, 248, 220))
    draw = ImageDraw.Draw(img)

    # Mesa
    draw.rectangle([0, 450, 800, 600], fill=(139, 69, 19))

    # Plato
    draw.ellipse([100, 150, 700, 450], fill=(255, 255, 255))

    # Pescado (forma ovalada dorada)
    draw.ellipse([200, 220, 600, 380], fill=(218, 165, 32))

    # Cola
    draw.polygon([(600, 300), (680, 260), (680, 340)], fill=(184, 134, 11))

    # Aletas
    draw.polygon([(300, 210), (320, 180), (340, 210)], fill=(205, 133, 63))
    draw.polygon([(450, 210), (470, 180), (490, 210)], fill=(205, 133, 63))

    # Ojo
    draw.ellipse([240, 280, 260, 300], fill=(255, 255, 255))
    draw.ellipse([245, 285, 255, 295], fill=(0, 0, 0))

    add_text(img, "Lau-Lau Frito", 'bottom', 45, (51, 51, 51))

    return img

def create_gusanos_moriche():
    """Gusanos de moriche"""
    img = Image.new('RGB', (800, 600), (250, 250, 245))
    draw = ImageDraw.Draw(img)

    # Mesa
    draw.rectangle([0, 450, 800, 600], fill=(139, 69, 19))

    # Plato
    draw.ellipse([100, 150, 700, 450], fill=(255, 255, 255))

    # Hoja de plátano
    draw.ellipse([150, 200, 650, 400], fill=(34, 139, 34))

    # Gusanos (formas ovaladas amarillas)
    gusanos = [(250, 260), (400, 280), (320, 320), (480, 300), (350, 350)]
    for x, y in gusanos:
        draw.ellipse([x, y, x + 80, y + 25], fill=(255, 235, 59))
        # Segmentos
        for seg in range(x + 10, x + 70, 10):
            draw.line([(seg, y), (seg, y + 25)], fill=(240, 200, 30), width=1)

    add_text(img, "Gusanos de Moriche", 'bottom', 40, (51, 51, 51))

    return img

def create_jaguar():
    """Jaguar"""
    img = create_gradient(1000, 700, (45, 80, 22), (26, 48, 16))  # Selva oscura
    draw = ImageDraw.Draw(img)

    # Rama
    draw.rectangle([100, 400, 900, 430], fill=(101, 67, 33))

    # Cuerpo del jaguar
    draw.ellipse([300, 320, 500, 420], fill=(210, 180, 140))

    # Cabeza
    draw.ellipse([480, 300, 600, 400], fill=(218, 165, 32))

    # Orejas
    draw.ellipse([490, 280, 520, 310], fill=(205, 133, 63))
    draw.ellipse([570, 280, 600, 310], fill=(205, 133, 63))

    # Ojos
    draw.ellipse([520, 330, 540, 350], fill=(144, 238, 144))
    draw.ellipse([525, 335, 535, 345], fill=(0, 0, 0))
    draw.ellipse([560, 330, 580, 350], fill=(144, 238, 144))
    draw.ellipse([565, 335, 575, 345], fill=(0, 0, 0))

    # Manchas (rosetas)
    for x, y in [(340, 350), (380, 360), (420, 350), (360, 380), (400, 390)]:
        draw.ellipse([x, y, x + 20, y + 20], outline=(0, 0, 0), width=2)

    # Patas
    draw.rectangle([350, 410, 370, 480], fill=(184, 134, 11))
    draw.rectangle([430, 410, 450, 480], fill=(184, 134, 11))

    add_text(img, "Jaguar (Panthera onca)", 'bottom', 45, (255, 215, 0))

    return img

def create_guacamayas():
    """Guacamayas"""
    img = create_gradient(1000, 700, (135, 206, 235), (176, 224, 230))
    draw = ImageDraw.Draw(img)

    # Rama
    draw.rectangle([50, 400, 950, 430], fill=(101, 67, 33))

    # Guacamaya 1 (roja)
    # Cuerpo
    draw.ellipse([250, 280, 320, 400], fill=(220, 20, 60))
    # Cabeza
    draw.ellipse([300, 250, 350, 300], fill=(220, 20, 60))
    # Ala azul
    draw.ellipse([220, 300, 260, 380], fill=(30, 144, 255))
    # Cola
    draw.rectangle([275, 395, 295, 500], fill=(220, 20, 60))
    draw.rectangle([280, 395, 300, 500], fill=(30, 144, 255))
    # Pico
    draw.polygon([(350, 270), (380, 275), (350, 280)], fill=(50, 50, 50))

    # Guacamaya 2 (azul-amarilla)
    # Cuerpo
    draw.ellipse([650, 300, 720, 420], fill=(30, 144, 255))
    # Cabeza
    draw.ellipse([700, 270, 750, 320], fill=(30, 144, 255))
    # Ala amarilla
    draw.ellipse([720, 320, 760, 400], fill=(255, 215, 0))
    # Cola
    draw.rectangle([675, 415, 695, 520], fill=(30, 144, 255))
    draw.rectangle([680, 415, 700, 520], fill=(255, 215, 0))
    # Pico
    draw.polygon([(750, 290), (780, 295), (750, 300)], fill=(50, 50, 50))

    add_text(img, "Guacamayas", 'bottom', 50, (220, 20, 60))

    return img

def create_peces_orinoco():
    """Peces del Orinoco"""
    img = create_gradient(1000, 700, (30, 136, 229), (13, 71, 161))
    draw = ImageDraw.Draw(img)

    # Rayos de luz
    for x in [200, 500, 800]:
        draw.polygon([(x, 0), (x + 30, 0), (x + 80, 700), (x + 50, 700)],
                    fill=(255, 255, 255, 30))

    # Plantas acuáticas
    for x in [80, 900]:
        draw.line([(x, 700), (x, 400)], fill=(46, 125, 50), width=10)
        draw.ellipse([x - 20, 380, x + 20, 420], fill=(67, 160, 71))

    # Peces
    peces = [
        (300, 200, (255, 165, 0)),   # Naranja
        (600, 300, (192, 192, 192)),  # Plateado
        (400, 450, (102, 187, 106)),  # Verde
        (700, 250, (255, 140, 0)),    # Naranja oscuro
        (250, 500, (169, 169, 169)),  # Gris
    ]

    for x, y, color in peces:
        # Cuerpo
        draw.ellipse([x, y, x + 120, y + 60], fill=color)
        # Cola
        draw.polygon([(x + 120, y + 30), (x + 160, y + 10), (x + 160, y + 50)], fill=color)
        # Ojo
        draw.ellipse([x + 10, y + 20, x + 20, y + 30], fill=(255, 255, 255))
        draw.ellipse([x + 13, y + 23, x + 17, y + 27], fill=(0, 0, 0))

    add_text(img, "Peces del Orinoco", 'bottom', 50, (255, 255, 255))

    return img

def create_manati():
    """Manatí"""
    img = create_gradient(1000, 700, (79, 195, 247), (2, 119, 189))
    draw = ImageDraw.Draw(img)

    # Ondas de superficie
    for y in [50, 80]:
        for x in range(0, 1000, 100):
            draw.arc([x, y, x + 50, y + 20], 0, 180, fill=(255, 255, 255), width=2)

    # Plantas acuáticas
    for x in [100, 850]:
        draw.line([(x, 700), (x, 500)], fill=(27, 94, 32), width=8)
        draw.ellipse([x - 15, 480, x + 15, 510], fill=(46, 125, 50))

    # Manatí
    # Cuerpo
    draw.ellipse([200, 300, 700, 500], fill=(141, 141, 141))
    # Cabeza
    draw.ellipse([650, 330, 800, 470], fill=(128, 128, 128))
    # Hocico
    draw.ellipse([770, 370, 850, 430], fill=(105, 105, 105))
    # Cola
    draw.ellipse([100, 360, 220, 440], fill=(115, 115, 115))
    # Aletas
    draw.ellipse([300, 480, 400, 540], fill=(128, 128, 128))
    draw.ellipse([550, 490, 650, 550], fill=(128, 128, 128))
    # Ojos
    draw.ellipse([720, 360, 735, 375], fill=(50, 50, 50))

    # Burbujas
    for x, y in [(250, 200), (400, 150), (650, 180)]:
        draw.ellipse([x, y, x + 15, y + 15], fill=(255, 255, 255, 100))

    add_text(img, "Manatí del Caribe", 'bottom', 50, (255, 255, 255))

    return img

# Diccionario de funciones de creación
images_to_create = {
    'delta-orinoco.png': create_delta_orinoco,
    'viviendas-warao.png': create_viviendas_warao,
    'sancocho.png': create_sancocho,
    'lau-lau.png': create_lau_lau,
    'gusanos-moriche.png': create_gusanos_moriche,
    'jaguar.png': create_jaguar,
    'guacamayas.png': create_guacamayas,
    'peces-orinoco.png': create_peces_orinoco,
    'manati.png': create_manati,
}

def main():
    output_dir = 'images'
    os.makedirs(output_dir, exist_ok=True)

    print("Generando imágenes PNG...")
    for filename, create_func in images_to_create.items():
        filepath = os.path.join(output_dir, filename)
        print(f"Creando {filename}...")
        img = create_func()
        img.save(filepath, 'PNG', optimize=True)
        print(f"✓ {filename} guardado ({os.path.getsize(filepath) // 1024} KB)")

    print(f"\n✓ Total: {len(images_to_create)} imágenes PNG creadas en '{output_dir}/'")

if __name__ == '__main__':
    main()
