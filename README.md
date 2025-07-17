# Peano Curve Animation

This project visualizes and animates the construction of the **Peano Curve**, a classic space-filling fractal, using Python and Pygame. The animation smoothly increases the fractal's iteration, adds color gradients, and allows interactive zooming and panning for an engaging fractal exploration experience.

## Features

- **Animated Peano Curve Construction:** Watch the fractal build up through increasing iterations.
- **Colorful Visualization:** Dynamic color gradients and glow effects for a visually appealing display.
- **Interactive Controls:** Zoom and pan the fractal in real time using your keyboard.
- **Fullscreen Display:** Automatically adapts to your screen size for an immersive experience.

## Requirements

- Python 3.x
- [Pygame](https://www.pygame.org/)

Install Pygame with:
```bash
pip install pygame
```

## Usage

Run the animation with:
```bash
python peano.py
```

The program will launch in fullscreen mode and begin animating the Peano Curve.

## Controls

- **Zoom In:** Up Arrow (↑)
- **Zoom Out:** Down Arrow (↓)
- **Move Left:** A
- **Move Right:** D
- **Move Up:** W
- **Move Down:** S
- **Exit:** ESC

## How It Works

- The program recursively generates the points of the Peano Curve for each iteration.
- The animation automatically increases the fractal's iteration up to a maximum (default: 4).
- Color gradients are applied along the curve for a smooth, glowing effect.
- You can zoom and pan to explore different parts of the fractal in detail.

## Customization

You can adjust parameters such as:
- `max_iterations` (default: 4) — Maximum depth of the Peano Curve.
- `animation_speed` — How quickly the animation progresses.
- `scale_factor`, `zoom_speed`, `move_speed` — Control zoom and pan sensitivity.

These can be found and modified in the `PeanoCurve` class in the script.

## Credits

- Fractal generation and animation by [blakealmon](https://github.com/blakealmon).
- Built with [Pygame](https://www.pygame.org/).

