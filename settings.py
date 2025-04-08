"""
Filename: settings.py
"""

from numba import njit
import numpy as np
from pyglm import glm
import math

# Window resolution
WINDOW_RES = glm.vec2(800, 600)

# Timing
FPS = 60

# Colors
BACKGROUND_COLOR = glm.vec3(0.1, 0.146, 0.25)
