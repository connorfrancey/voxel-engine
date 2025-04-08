"""
Filename: settings.py
"""

from numba import njit
import numpy as np
from pyglm import glm
import math

# Window resolution
WINDOW_RES = glm.vec2(800, 600)

# Chunk
CHUNK_SIZE = 32
H_CHUNK_sIZE = CHUNK_SIZE // 2
CHUNK_AREA = CHUNK_SIZE * CHUNK_SIZE
CHUNK_VOL = CHUNK_AREA * CHUNK_SIZE

# Camera
ASPECT_RATIO = WINDOW_RES.x / WINDOW_RES.y
FOV_DEG = 50
V_FOV = glm.radians(FOV_DEG)    # Vertical FOV
H_FOV = 2 * math.atan(math.tan(V_FOV * 0.5) * ASPECT_RATIO) # Horizontal FOV
NEAR = 0.1
FAR = 2000.0
PITCH_MAX = glm.radians(89)

# Player
PLAYER_SPEED = 0.008
PLAYER_ROT_SPEED = 0.003
PLAYER_POS = glm.vec3(H_CHUNK_sIZE, CHUNK_SIZE, 1.5 * CHUNK_SIZE)
MOUSE_SENSITIVITY = 0.002

# Timing
FPS = 60

# Colors
BACKGROUND_COLOR = glm.vec3(0.1, 0.146, 0.25)
