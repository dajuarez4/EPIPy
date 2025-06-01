import pygame
import sys

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Fundamental Forces Picker")
font = pygame.font.SysFont("Arial", 20)

# Define forces
forces = {
    "1": ("Electromagnetic Force", (0, 0, 255)),
    "2": ("Weak Force", (255, 0, 0)),
    "3": ("Strong Force", (0, 255, 0))
}

# Game state
current_screen = "menu"  # can be "menu" or one of the force names
selected_force = None

def draw_menu():
    screen.fill((10, 10, 30))
    title = font.render("Choose a Fundamental Force:", True, (255, 255, 255))
    screen.blit(title, (20, 20))

    y = 80
    for key, (name, _) in forces.items():
        label = font.render(f"{key}: {name}", True, (200, 200, 200))
        screen.blit(label, (40, y))
        y += 40

def draw_force_screen(name, color):
    screen.fill((0, 0, 0))
    label = font.render(f"{name}", True, color)
    back_text = font.render("Press 'B' to go back", True, (180, 180, 180))
    pygame.draw.circle(screen, color, (300, 220), 60)

    screen.blit(label, (20, 20))
    screen.blit(back_text, (20, 360))


def draw_force_screen(name, color):
    screen.fill((0, 0, 0))

    # Load text file
   # filename = name.lower().replace(" ", "_").replace("force", "") + ".txt"
   # filename = name.lower().replace(" ", "_").replace("force", "") + ".txt"
    filename_map = {
    "Electromagnetic Force": "electromagnetic.txt",
    "Weak Force": "weak.txt",
    "Strong Force": "strong.txt"
}
    filename = filename_map.get(name, "missing.txt")

    try:
        with open(filename, "r") as f:
            lines = f.readlines()
    except FileNotFoundError:
        lines = ["Description file not found."]

    # Render text
    title = font.render(name, True, color)
    screen.blit(title, (20, 20))

    back_text = font.render("Press 'B' to go back", True, (180, 180, 180))
    screen.blit(back_text, (20, 360))

    y = 80
    for line in lines:
        text = font.render(line.strip(), True, (255, 255, 255))
        screen.blit(text, (20, y))
        y += 30

import os

def draw_force_screen(name, color):
    screen.fill((0, 0, 0))

    # --- 1. Cargar texto ---
    filename_map = {
        "Electromagnetic Force": "electromagnetic.txt",
        "Weak Force": "weak.txt",
        "Strong Force": "strong.txt"
    }
    filename = filename_map.get(name, None)

    try:
        if filename:
            with open(filename, "r") as f:
                lines = f.readlines()
        else:
            lines = ["Descripción no disponible."]
    except FileNotFoundError:
        lines = ["Archivo de texto no encontrado."]

    # --- 2. Cargar imagen ---
    image_file = name.lower().split()[0] + ".png"  # Ej: electromagnetic.png
    if os.path.exists(image_file):
        try:
            img = pygame.image.load(image_file)
            img = pygame.transform.scale(img, (180, 180))  # Redimensionar si es necesario
            screen.blit(img, (400, 50))  # Mostrar imagen en pantalla
        except Exception as e:
            print("Error cargando imagen:", e)

    # --- 3. Título y texto ---
    title = font.render(name, True, color)
    screen.blit(title, (20, 20))

    y = 80
    for line in lines:
        text = font.render(line.strip(), True, (255, 255, 255))
        screen.blit(text, (20, y))
        y += 30

    # --- 4. Botón de regreso ---
    back_text = font.render("Presiona 'B' para regresar", True, (180, 180, 180))
    screen.blit(back_text, (20, 360))








# Main loop
while True:
    if current_screen == "menu":
        draw_menu()
    else:
        draw_force_screen(*selected_force)

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        elif event.type == pygame.KEYDOWN:
            key = pygame.key.name(event.key)

            if current_screen == "menu":
                if key in forces:
                    selected_force = forces[key]
                    current_screen = "force"
            elif current_screen == "force":
                if key.lower() == 'b':
                    current_screen = "menu"

