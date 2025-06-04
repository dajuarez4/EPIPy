# EPIPy  
Elemental Particles Interaction Interactive game  
---

This is an interactive Pygame-based simulation where particles interact with other particles or atoms (e.g., H, C, O). It's a fun way to visualize particle interactions and collect data for analysis.

## How to Run the Game:

### 1. Clone the Repository

``` git clone https://github.com/dajuarez4/EPIPy ```

-----
### 2. Set up a conda environment including the following libraries:
- Pygame  
- Pandas  
- Matplotlib  

### 3. Finally run main.py 

## Description:

This game/simulator includes three utility files located inside the `utils/` directory:

- `atoms.py`: Contains the class to generate the detectors ('atoms').
- `neutrinos.py`: Contains the class where the incoming particles ('neutrinos') are generated.
- `config.py`: A configuration file where you can customize properties such as:
  - radius
  - shape
  - velocity
  - probabilities of interaction (hit)
  - etc.
