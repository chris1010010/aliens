# Aliens
Boot.dev personal project.

Essentially a classic snake game with Alien(s) theme.

## Usage
- Uses UV virtual environment
- Currently hard-coded to 3200 x 1800 window size
- Start with `python3 main.py`
- Controls: cursor keys

## Game Logic
- The player is a pack of xenomorphs (the snake equivalent)
- Humans are spawned from openings at the edge of the arena
- Consume a human to get faster
- If a human touches an alien egg at the edge of the arena, a face hugger will attach itself
- Infected humans turn into xenomorphs
- Bump into a xenomorph to add it to your pack (you grow)
- Most humans are civilians and can't harm you
- Some humans are colonial marines
- If a colonial marine gets too close, you lose one xenomorph (you shrink) and the marine dies
- The game ends if you collide with the wall, collide with yourself, or you have no xenomorphs left in your pack
