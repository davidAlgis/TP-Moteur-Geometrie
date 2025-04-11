"""
This script defines the class that will help you for
the rendering part of the engine.
"""

import sys

import pygame


class Renderer:
    """This class will help you for the rendering part of the engine."""

    def __init__(
        self,
        width=800,
        height=600,
        title="Renderer Window",
        bg_color=(255, 255, 255),
    ):
        """
        Initialize the render window using pygame.

        :param width: Window width in pixels.
        :param height: Window height in pixels.
        :param title: Window title.
        :param bg_color: Background color as an RGB tuple (default is white).
        """
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption(title)
        self.clock = pygame.time.Clock()
        self.bg_color = bg_color  # Background color (white by default)
        self.running = True  # Flag to control the main loop
        self.clear()
        self.update()

    def clear(self, color=None):
        """
        Clear the screen by filling it with the specified color.

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
        pos = (int(x), int(y))
        pygame.draw.circle(self.screen, color, pos, radius)

    def draw_grid(self, cell_width, cell_height, color=(128, 128, 128)):
        """
        Draws a grid on the 2D plane with cells of specified width and height.

        :param cell_width: Width of each grid cell in pixels.
        :param cell_height: Height of each grid cell in pixels.
        :param color: RGB tuple representing the
        grid line color (default is grey).
        """
        for x in range(0, self.width, cell_width):
            pygame.draw.line(self.screen, color, (x, 0), (x, self.height))
        for y in range(0, self.height, cell_height):
            pygame.draw.line(self.screen, color, (0, y), (self.width, y))

    def draw_segment(self, start, end, color=(255, 255, 255), width=1):
        """
        Draws a line segment from the start position to the end position.

        :param start: Tuple (x1, y1) for the start point.
        :param end: Tuple (x2, y2) for the end point.
        :param color: RGB tuple representing the line's color.
        :param width: The thickness of the line.
        """
        start_int = (int(start[0]), int(start[1]))
        end_int = (int(end[0]), int(end[1]))
        pygame.draw.line(self.screen, color, start_int, end_int, width)

    def draw_triangle(self, p1, p2, p3, color=(255, 255, 255), width=1):
        """
        Draws a triangle by connecting three points with segments.

        :param p1: Tuple (x, y) for the first point.
        :param p2: Tuple (x, y) for the second point.
        :param p3: Tuple (x, y) for the third point.
        :param color: RGB tuple representing the triangle's color.
        :param width: The thickness of the triangle's segments.
        """
        self.draw_segment(p1, p2, color, width)
        self.draw_segment(p2, p3, color, width)
        self.draw_segment(p3, p1, color, width)

    def draw_circle(self, center, radius, color=(255, 255, 255), width=1):
        """
        Draws a circle with the specified center and radius.

        :param center: Tuple (x, y) for the circle's center.
        :param radius: Radius of the circle.
        :param color: RGB tuple representing the circle's color.
        :param width: The thickness of the circle's outline.
                      If set to 0, the circle will be filled.
        """
        center_int = (int(center[0]), int(center[1]))
        pygame.draw.circle(self.screen, color, center_int, int(radius), width)

    def draw_text(
        self, text, position, font_name=None, font_size=20, color=(0, 0, 0)
    ):
        """
        Draws text on the screen with the specified font, size and color.

        :param text: The string to be displayed.
        :param position: Tuple (x, y) indicating the position
        (top-left corner) where the text will appear.
        :param font_name: Name or path to the font file.
        If None, uses the default pygame font.
        :param font_size: Font size (default is 20).
        :param color: RGB tuple representing the text color (default is black).
        """
        font = pygame.font.Font(font_name, font_size)
        text_surface = font.render(text, True, color)
        self.screen.blit(text_surface, (int(position[0]), int(position[1])))

    def update(self):
        """Update the display window (flips the screen buffer)."""
        pygame.display.flip()

    def handle_events(self):
        """
        Handle pygame events to allow for proper window closure.
        Instead of exiting immediately, this sets a flag to stop the main loop.
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def quit(self):
        """Quit the pygame application gracefully."""
        pygame.quit()


if __name__ == "__main__":
    renderer = Renderer(800, 600, "Renderer Example")
    triangle_points = ((100, 500), (300, 400), (200, 550))
    circle_center = (600, 150)
    circle_radius = 50

    while renderer.running:
        renderer.handle_events()
        renderer.clear()
        renderer.draw_grid(50, 50, (100, 100, 100))
        renderer.draw_triangle(
            triangle_points[0],
            triangle_points[1],
            triangle_points[2],
            color=(0, 255, 0),
            width=2,
        )
        renderer.draw_circle(
            circle_center, circle_radius, color=(255, 0, 255), width=2
        )
        renderer.draw_point(400, 300, (255, 255, 0), radius=4)
        renderer.draw_text("Hello world", (350, 50), font_size=30)
        renderer.update()
        renderer.clock.tick(60)

    # Once the loop is broken, quit pygame gracefully
    renderer.quit()
