"""
This script defines the class that will help you for
the rendering part of the engine.
"""

import sys

import pygame


class Renderer:
    """
    This class will help you for the rendering part of the engine.
    """

    def __init__(self, width=800, height=600, title="Renderer Window"):
        """
        Initializes the render window using pygame.

        :param width: Window width in pixels.
        :param height: Window height in pixels.
        :param title: Window title.
        """
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption(title)
        self.clock = pygame.time.Clock()
        self.bg_color = (0, 0, 0)  # Default background color (black)
        self.clear()
        self.update()

    def clear(self, color=None):
        """
        Clears the screen by filling it with the specified color.

        :param color: Fill color as an RGB tuple.
                      If None, uses the default background color.
        """
        if color is None:
            color = self.bg_color
        self.screen.fill(color)

    def draw_point(self, x, y, color=(255, 255, 255), radius=2):
        """
        Draws a point on the 2D plane at position (x, y) with the given color.

        :param x: x-coordinate of the point.
        :param y: y-coordinate of the point.
        :param color: RGB tuple representing the point's color.
        :param radius: Radius of the drawn point (for better visibility).
        """
        # Convert coordinates to integers
        pos = (int(x), int(y))
        pygame.draw.circle(self.screen, color, pos, radius)

    def draw_grid(self, cell_width, cell_height, color=(128, 128, 128)):
        """
        Draws a grid on the 2D plane with cells of specified width and height.

        :param cell_width: Width of each grid cell in pixels.
        :param cell_height: Height of each grid cell in pixels.
        :param color: RGB tuple representing the grid line color (default is grey).
        """
        # Draw vertical grid lines
        for x in range(0, self.width, cell_width):
            pygame.draw.line(self.screen, color, (x, 0), (x, self.height))
        # Draw horizontal grid lines
        for y in range(0, self.height, cell_height):
            pygame.draw.line(self.screen, color, (0, y), (self.width, y))

    def update(self):
        """
        Updates the display window (flips the screen buffer).
        """
        pygame.display.flip()

    def handle_events(self):
        """
        Handles pygame events to allow for proper window closure.
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


if __name__ == "__main__":
    # Example usage of the Renderer class
    renderer = Renderer(800, 600, "Renderer Example")

    # Example: draw some points and a grid
    running = True
    while running:
        renderer.handle_events()
        renderer.clear()
        # Draw grid with cells of 50x50 pixels
        renderer.draw_grid(50, 50, (100, 100, 100))
        # Draw a red, green, and blue point
        renderer.draw_point(100, 100, (255, 0, 0))  # Red
        renderer.draw_point(200, 150, (0, 255, 0))  # Green
        renderer.draw_point(300, 200, (0, 0, 255))  # Blue
        renderer.update()
        renderer.clock.tick(60)
