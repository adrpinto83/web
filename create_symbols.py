#!/usr/bin/env python3
"""
Script para crear la bandera y escudo de Delta Amacuro
"""

from PIL import Image, ImageDraw, ImageFont
import os

def create_bandera_delta():
    """Bandera del Estado Delta Amacuro"""
    width, height = 600, 400
    img = Image.new('RGB', (width, height), (255, 255, 255))
    draw = ImageDraw.Draw(img)

    stripe_height = height // 3

    # Franja superior - Azul (cielo y agua)
    draw.rectangle([0, 0, width, stripe_height], fill=(30, 144, 255))

    # Franja media - Blanca (paz)
    draw.rectangle([0, stripe_height, width, stripe_height * 2], fill=(255, 255, 255))

    # Franja inferior - Verde (selva)
    draw.rectangle([0, stripe_height * 2, width, height], fill=(34, 139, 34))

    # Estrella en el centro (blanca sobre la franja verde)
    center_x = width // 2
    center_y = stripe_height * 2 + stripe_height // 2

    # Dibujar estrella de 5 puntas
    import math
    outer_radius = 50
    inner_radius = 20
    points = []

    for i in range(10):
        angle = math.pi / 2 + i * math.pi / 5
        if i % 2 == 0:
            radius = outer_radius
        else:
            radius = inner_radius
        x = center_x + radius * math.cos(angle)
        y = center_y - radius * math.sin(angle)
        points.append((x, y))

    draw.polygon(points, fill=(255, 255, 255))

    return img

def create_escudo_delta():
    """Escudo del Estado Delta Amacuro"""
    width, height = 500, 600
    img = Image.new('RGB', (width, height), (240, 240, 240))
    draw = ImageDraw.Draw(img)

    # Contorno del escudo (forma de escudo clásico)
    shield_points = [
        (width // 2, 50),  # Punto superior
        (width - 50, 100),
        (width - 50, 350),
        (width // 2, height - 50),  # Punto inferior
        (50, 350),
        (50, 100)
    ]

    # Fondo del escudo - degradado azul a verde
    for i in range(100, 500):
        ratio = (i - 100) / 400
        r = int(30 + (34 - 30) * ratio)
        g = int(144 - (144 - 139) * ratio)
        b = int(255 - (255 - 34) * ratio)

        y_top = 50 + (i - 100) * 0.4
        y_bottom = min(i, 500)

        if y_bottom > y_top:
            draw.rectangle([50, y_top, width - 50, y_bottom], fill=(r, g, b))

    # Borde dorado
    draw.polygon(shield_points, outline=(218, 165, 32), width=8)

    # Símbolos en el escudo

    # Palma de moriche (centro superior)
    palm_x = width // 2
    palm_y = 150
    draw.rectangle([palm_x - 5, palm_y, palm_x + 5, palm_y + 80], fill=(139, 69, 19))

    # Hojas de palma
    for angle in [-60, -40, -20, 0, 20, 40, 60]:
        import math
        rad = math.radians(angle)
        end_x = palm_x + 40 * math.sin(rad)
        end_y = palm_y - 40 * math.cos(rad)
        draw.line([(palm_x, palm_y), (end_x, end_y)], fill=(34, 139, 34), width=4)

    # Río (ondulado en la parte inferior)
    for y_offset in [350, 370, 390]:
        draw.arc([80, y_offset, 180, y_offset + 30], 0, 180, fill=(135, 206, 250), width=6)
        draw.arc([170, y_offset, 270, y_offset + 30], 180, 360, fill=(135, 206, 250), width=6)
        draw.arc([260, y_offset, 360, y_offset + 30], 0, 180, fill=(135, 206, 250), width=6)
        draw.arc([350, y_offset, 450, y_offset + 30], 180, 360, fill=(135, 206, 250), width=6)

    # Curiara (canoa) en el centro
    canoa_y = 280
    draw.ellipse([150, canoa_y, 350, canoa_y + 30], fill=(139, 69, 19))
    draw.ellipse([155, canoa_y + 5, 345, canoa_y + 25], fill=(160, 82, 45))

    # Estrellas (representando municipios)
    star_positions = [(150, 120), (350, 120), (250, 450)]

    import math
    for star_x, star_y in star_positions:
        outer_radius = 15
        inner_radius = 6
        points = []

        for i in range(10):
            angle = math.pi / 2 + i * math.pi / 5
            if i % 2 == 0:
                radius = outer_radius
            else:
                radius = inner_radius
            x = star_x + radius * math.cos(angle)
            y = star_y - radius * math.sin(angle)
            points.append((x, y))

        draw.polygon(points, fill=(255, 215, 0))

    return img

def main():
    output_dir = 'images'
    os.makedirs(output_dir, exist_ok=True)

    print("Creando símbolos regionales...")

    # Bandera
    print("Creando bandera-delta.png...")
    bandera = create_bandera_delta()
    bandera_path = os.path.join(output_dir, 'bandera-delta.png')
    bandera.save(bandera_path, 'PNG', optimize=True)
    print(f"✓ bandera-delta.png guardado ({os.path.getsize(bandera_path) // 1024} KB)")

    # Escudo
    print("Creando escudo-delta.png...")
    escudo = create_escudo_delta()
    escudo_path = os.path.join(output_dir, 'escudo-delta.png')
    escudo.save(escudo_path, 'PNG', optimize=True)
    print(f"✓ escudo-delta.png guardado ({os.path.getsize(escudo_path) // 1024} KB)")

    # También crear versiones SVG simples
    print("\nCreando versiones SVG...")
    create_bandera_svg()
    create_escudo_svg()

    print("\n✓ Símbolos regionales creados exitosamente")

def create_bandera_svg():
    """Crear SVG de la bandera"""
    svg_content = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 400">
  <!-- Franja azul -->
  <rect width="600" height="133.33" fill="#1e90ff"/>

  <!-- Franja blanca -->
  <rect y="133.33" width="600" height="133.33" fill="#ffffff"/>

  <!-- Franja verde -->
  <rect y="266.66" width="600" height="133.34" fill="#228b22"/>

  <!-- Estrella blanca -->
  <path d="M 300 283.33 L 315.45 318.18 L 353.63 323.51 L 326.82 349.49 L 332.91 387.51 L 300 369.77 L 267.09 387.51 L 273.18 349.49 L 246.37 323.51 L 284.55 318.18 Z"
        fill="#ffffff"/>
</svg>'''

    with open('images/bandera-delta.svg', 'w') as f:
        f.write(svg_content)
    print("✓ bandera-delta.svg creado")

def create_escudo_svg():
    """Crear SVG del escudo"""
    svg_content = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 600">
  <defs>
    <linearGradient id="shieldGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" style="stop-color:#1e90ff;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#228b22;stop-opacity:1" />
    </linearGradient>
  </defs>

  <!-- Forma del escudo -->
  <path d="M 250 50 L 450 100 L 450 350 L 250 550 L 50 350 L 50 100 Z"
        fill="url(#shieldGrad)" stroke="#daa520" stroke-width="8"/>

  <!-- Palma de moriche -->
  <rect x="245" y="150" width="10" height="80" fill="#8b4513"/>
  <g stroke="#228b22" stroke-width="4" fill="none">
    <line x1="250" y1="150" x2="220" y2="120"/>
    <line x1="250" y1="150" x2="230" y2="125"/>
    <line x1="250" y1="150" x2="240" y2="130"/>
    <line x1="250" y1="150" x2="250" y2="110"/>
    <line x1="250" y1="150" x2="260" y2="130"/>
    <line x1="250" y1="150" x2="270" y2="125"/>
    <line x1="250" y1="150" x2="280" y2="120"/>
  </g>

  <!-- Río (ondas) -->
  <path d="M 80 360 Q 130 350, 180 360 T 280 360 T 380 360 T 460 360"
        stroke="#87ceeb" stroke-width="6" fill="none"/>
  <path d="M 80 380 Q 130 370, 180 380 T 280 380 T 380 380 T 460 380"
        stroke="#87ceeb" stroke-width="6" fill="none"/>

  <!-- Curiara -->
  <ellipse cx="250" cy="295" rx="100" ry="15" fill="#8b4513"/>
  <ellipse cx="250" cy="292" rx="95" ry="12" fill="#a0522d"/>

  <!-- Estrellas -->
  <path d="M 150 120 L 157 137 L 175 140 L 162 152 L 165 170 L 150 162 L 135 170 L 138 152 L 125 140 L 143 137 Z"
        fill="#ffd700"/>
  <path d="M 350 120 L 357 137 L 375 140 L 362 152 L 365 170 L 350 162 L 335 170 L 338 152 L 325 140 L 343 137 Z"
        fill="#ffd700"/>
  <path d="M 250 450 L 257 467 L 275 470 L 262 482 L 265 500 L 250 492 L 235 500 L 238 482 L 225 470 L 243 467 Z"
        fill="#ffd700"/>
</svg>'''

    with open('images/escudo-delta.svg', 'w') as f:
        f.write(svg_content)
    print("✓ escudo-delta.svg creado")

if __name__ == '__main__':
    main()
