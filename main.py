"""
Filename: main.py
"""

from settings import *
import moderngl as mgl
import pygame as pg
import sys

from shader_program import ShaderProgram
from scene import Scene
from player import Player
from textures import Textures


class VoxelEngine:
    def __init__(self):
        # Initialize pygame and configure OpenGL
        pg.init()
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MAJOR_VERSION, 4)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MINOR_VERSION, 6)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_PROFILE_MASK, pg.GL_CONTEXT_PROFILE_CORE)
        pg.display.gl_set_attribute(pg.GL_DEPTH_SIZE, 24)

        # Set up the window and create the moderngl context
        pg.display.set_mode(WINDOW_RES, flags=pg.OPENGL | pg.DOUBLEBUF)
        self.ctx = mgl.create_context()

        # Configure the moderngl flags and set the OpenGL garbage collection mode to automatic
        self.ctx.enable(flags=mgl.DEPTH_TEST | mgl.CULL_FACE | mgl.BLEND)
        self.ctx.gc_mode = 'auto'

        # Objects to help track time
        self.clock = pg.time.Clock()
        self.delta_time = 0
        self.time = 0

        # Lock and hide the mouse cursor
        pg.event.set_grab(True)
        pg.mouse.set_visible(False)

        self.is_running = True
        self.on_init()

    def on_init(self):
        self.textures = Textures(self)
        self.player = Player(self)
        self.shader_program = ShaderProgram(self)
        self.scene = Scene(self)

    def update(self):

        # Update the player
        self.player.update()

        # Update the shader program
        self.shader_program.update()

        # Update the scene
        self.scene.update()

        # Calculate delta time
        self.delta_time = self.clock.tick(FPS)
        self.time = pg.time.get_ticks() * 0.001

        # Update the window title to display the FPS
        pg.display.set_caption(f'Voxel Engine - FPS: {str(int(self.clock.get_fps()))}')

    def render(self):
        # Clear the screen
        self.ctx.clear(color=BACKGROUND_COLOR)

        # Render the scene
        self.scene.render()

        # Flip the display buffer
        pg.display.flip()

    def handle_events(self):
        # Check for any events
        for event in pg.event.get():
            # Quit the game
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                self.is_running = False
            # Handle player events
            self.player.handle_event(event=event)

    def run(self):
        # Main game loop
        while self.is_running:
            self.handle_events()
            self.update()
            self.render()
        pg.quit()
        sys.exit()


if __name__ == '__main__':
    app = VoxelEngine()
    app.run()
