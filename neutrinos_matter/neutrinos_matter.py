import pygame, random, sys
import math

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

neutrinos = []
# atoms = [pygame.Rect(x, 300, 10, 10) for x in range(50, 800, 50)]
interactions = []
class Atom:
    def __init__(self, x, y, atom_type):
        self.rect = pygame.Rect(x, y, 10, 10)
        self.type = atom_type
        self.color = self.get_color()
        self.interaction_prob = self.get_interaction_probability()
    
    def get_color(self):
        colors = {
            "H": (255, 255, 255),   # blanco
            "C": (100, 100, 100),   # gris
            "O": (0, 0, 255),       # azul
        }
        return colors.get(self.type, (200, 200, 200))

    def get_interaction_probability(self):
        probs = {
            "H": 0.002,
            "C": 0.0005,
            "O": 0.0001,
        }
        return probs.get(self.type, 0.001)
    
    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
# atoms = []
# atom_types = ["H", "C", "O"]

# for x in range(50, 800, 40):
#     for y in range(280, 340, 20):
#         t = random.choice(atom_types)
#         atoms.append(Atom(x, y, t))

#circles

atoms = []
atom_types = ["H", "C", "O"]

# Circle parameters
cx, cy = 400, 300  # center of circle
radius = 150
n_atoms = 30

# for i in range(n_atoms):
#     angle = 2 * math.pi * i / n_atoms  # angle in radians
#     x = int(cx + radius * math.cos(angle))
#     y = int(cy + radius * math.sin(angle))
#     t = random.choice(atom_types)
#     atoms.append(Atom(x, y, t))

# #-----right side 

for i in range(n_atoms):
    x = 600
    for y in range(0, 600, 15):
        t = random.choice(atom_types)
        atoms.append(Atom(x, y, t))



class Neutrino:
    def __init__(self):
        self.x = 0 #origin
        self.y = random.randint(100, 600)
        self.radius = 10
        self.color = (0, 255, 255)
        self.vx = 2
    
    def move(self):
        self.x += self.vx
    
    def draw(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)
# rect = pygame.Rect(n.x - n.radius, n.y - n.radius, n.radius*2, n.radius*2)

while True:
    screen.fill((10, 10, 30))

    if random.random() < 0.02:
        neutrinos.append(Neutrino())

    # for atom in atoms:
    #     pygame.draw.rect(screen, (150, 150, 150), atom)
    
    for atom in atoms:
        atom.draw(screen)

    for n in neutrinos[:]:
        n.move()
        n.draw()
        rect = pygame.Rect(n.x - n.radius, n.y - n.radius, n.radius*2, n.radius*2)

        # for atom in atoms:
        #     rect = pygame.Rect(n.x - 5, n.y - 5, 10, 10)
        #     if rect.colliderect(atom):
        #         if random.random() < 0.01:  # low chance of interaction
        #             pygame.draw.circle(screen, (255, 0, 0), (n.x, n.y), 10)  # show interaction
        #             interactions.append((n.x, n.y))
        #             neutrinos.remove(n)
        #             break

        for atom in atoms:
            # rect = pygame.Rect(n.x - 5, n.y - 5, 10, 10)
            if rect.colliderect(atom.rect):
                 if random.random() < atom.interaction_prob:
                    pygame.draw.circle(screen, (255, 0, 0), (n.x, n.y), 10)
                    interactions.append((n.x, n.y))
                    neutrinos.remove(n)
                    break

        
        if n.x > 800:
            neutrinos.remove(n)

    font = pygame.font.SysFont("Arial", 20)
    text = font.render(f"Detected interactions: {len(interactions)}", True, (255, 255, 255))
    screen.blit(text, (10, 10))

    pygame.display.flip()
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
