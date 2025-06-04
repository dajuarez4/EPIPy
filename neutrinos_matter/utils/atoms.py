import pygame, random, math
from utils.config import x_detec, y_detect,prob_atom_type1, prob_atom_type2,prob_atom_type3

class Atom:
    def __init__(self, x, y, atom_type):
        self.rect = pygame.Rect(x, y, x_detec, y_detect) #size detectors
        self.type = atom_type
        self.color = self.get_color()
        self.interaction_prob = self.get_interaction_probability()

    def get_color(self):
        colors = {
            "H": (255, 255, 255), 
            "C": (100, 100, 100),
            "O": (0, 0, 255),
        } # color atoms detect rgb
        return colors.get(self.type, (200, 200, 200))

    def get_interaction_probability(self):
        probs = {
            "H": prob_atom_type1,
            "C": prob_atom_type2,
            "O": prob_atom_type3,
        }
        return probs.get(self.type, 0.001)

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)


def generate_circular_atoms(center, radius, n_atoms, atom_types):
    atoms = []
    for i in range(n_atoms):
        angle = 2 * math.pi * i / n_atoms
        x = int(center[0] + radius * math.cos(angle))
        y = int(center[1] + radius * math.sin(angle))
        t = random.choice(atom_types)
        atoms.append(Atom(x, y, t))
    return atoms


def generate_vertical_wall(x,init_y_range, final_y_range, spacing, atom_types):
    atoms = []
    for y in range(init_y_range, final_y_range, spacing):
        t = random.choice(atom_types)
        atoms.append(Atom(x, y, t))
    return atoms
