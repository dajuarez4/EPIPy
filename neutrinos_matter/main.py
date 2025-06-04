import pygame, sys, random
from utils.atoms import Atom, generate_vertical_wall,generate_circular_atoms
from utils.neutrinos import Neutrino

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 20)

neutrinos = []
interactions = []
atom_types = ["H", "C", "O"]


atoms = generate_vertical_wall(x=700, init_y_range=50, final_y_range=600, spacing=15, atom_types=atom_types) # x~position wall-detector,
# atoms = generate_circular_atoms(center=[150,200], radius=10, n_atoms=10, atom_types=atom_types)
# atoms = generate_circular_atoms(center=[250,200], radius=10, n_atoms=10, atom_types=atom_types)
# print(atoms)
# atoms = []
# for circ in range(4):
#     c = generate_circular_atoms(center=[300,150*circ+100], radius=50, n_atoms=20, atom_types=atom_types)
#     atoms.append(c)
# print(atoms)

running = True
while running:
    screen.fill((10, 10, 30))

    if random.random() < 0.02:
        neutrinos.append(Neutrino())

    for atom in atoms:
        atom.draw(screen)

    for n in neutrinos[:]:
        n.move()
        n.draw(screen)

        rect = pygame.Rect(n.x - n.radius, n.y - n.radius, n.radius * 2, n.radius * 2)

        for atom in atoms:
            if rect.colliderect(atom.rect):
                if random.random() < atom.interaction_prob:
                    pygame.draw.circle(screen, (255, 0, 0), (n.x, n.y), 10)
                    interactions.append((n.x, n.y))
                    neutrinos.remove(n)
                    break

        if n.x > 800:
            neutrinos.remove(n)

    text = font.render(f"Detected interactions: {len(interactions)}", True, (255, 255, 255))
    screen.blit(text, (10, 10))

    pygame.display.flip()
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
sys.exit()
