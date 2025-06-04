import pygame, sys, random,time
from utils.atoms import Atom, generate_vertical_wall,generate_circular_atoms
from utils.neutrinos import Neutrino
import pandas as pd
import matplotlib.pyplot as plt

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 20)

neutrinos = []
interactions = []
atom_types = ["H", "C", "O"]

start_time = time.time()
# atoms = generate_vertical_wall(x=700, init_y_range=50, final_y_range=600, spacing=15, atom_types=atom_types) # x~position wall-detector,
# atoms = generate_circular_atoms(center=[150,200], radius=10, n_atoms=10, atom_types=atom_types)
atoms = generate_circular_atoms(center=[400,300], radius=200, n_atoms=50, atom_types=atom_types)
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
                    # interactions.append((n.x, n.y))
                    timestamp = time.time() - start_time
                    interactions.append((timestamp, atom.atom_type))
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
# sys.exit()


# if interactions:

#     df = pd.DataFrame(interactions, columns=["Time", "Type"])
#     fig, ax = plt.subplots()
#     for atom_type in df["Type"].unique():
#         subset = df[df["Type"] == atom_type]
#         ax.plot(subset["Time"], range(1, len(subset) + 1), label=f"{atom_type}")

#     ax.set_xlabel("Time (s)")
#     ax.set_ylabel("Cumulative Interactions")
#     ax.set_title("Time vs Interaction Count per Atom Type")
#     ax.legend()
#     plt.show()
if interactions:
    df = pd.DataFrame(interactions, columns=["Time", "Type"])
    df = df.sort_values(by="Time")  # Sort globally by time, optional

    fig, ax = plt.subplots(figsize=(8, 5))

    for atom_type in df["Type"].unique():
        subset = df[df["Type"] == atom_type].sort_values(by="Time").reset_index(drop=True)
        subset["CumulativeCount"] = subset.index + 1

        ax.step(subset["Time"], subset["CumulativeCount"], where="post", label=atom_type)
        ax.scatter(subset["Time"], subset["CumulativeCount"], s=30)

    ax.set_xlabel("Time (s)")
    ax.set_ylabel("Cumulative Interactions")
    ax.set_title("Time vs Interaction Count per Atom Type")
    ax.legend(title="Atom Type")
    ax.grid(True)
    plt.tight_layout()
    plt.show()
